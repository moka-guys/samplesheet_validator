# coding=utf-8
"""
Script for checking sample sheet naming and contents.

Uses the seglh-naming library. And adds further lab-specific checks e.g. whether sequencer IDs 
match those in lists of allowed IDs. Collects all errors in an errors list (SamplesheetCheck.errors_dict)
Contains the following classes:

- SamplesheetCheck
    Runs the checks. Called by webapp for uploaded samplesheets (uses name of file being uploaded), and
    called for runs not yet demultiplexed (uses path of expected samplesheet from demultiplex script)
"""
import os
import re
from typing import Union
from . import config
from .ss_logger import SSLogger, shutdown_logs
from seglh_naming.sample import Sample
from seglh_naming.samplesheet import Samplesheet


class SamplesheetCheck:
    """
    Runs the checks. Called by webapp for uploaded samplesheets (uses name of file being uploaded), and
    called for runs not yet demultiplexed (uses path of expected samplesheet from demultiplex script)

    Attributes:
        samplesheet_path (str):         Path to samplesheet
        logdir (str):                   Log file directory
        logger (obj):                   Logger object
        ss_obj (False | obj):           seglh-naming samplesheet object
        development_run (bool):         True if run is a development run, else False
        pannumbers (list):              Panel numbers in the sample sheet
        tso (bool):                     True if samplesheet contains any TSO samples
        samples (dict):                 Dictionary of sample IDs and sample names from the samplesheet
        errors (bool):                  True if samplesheet errors encountered, False if not
        errors_dict (dict):             Stores identifiers for any types of errors encountered
        data_headers (list):            Populated with headers from data section
        missing_headers (list):         Populated with missing data headers
        expected_data_headers (list):   Headers expected to be present in samplesheet
        sequencer_ids (list):           Valid sequencer IDs
        panels (list):                  Valid pan numbers
        tso_panels (list):              Valid TSO pannumbers
        development_panels (list):      Development pan numbers

    Methods:
        get_logger()
            Get logger for the class
        ss_checks()
            Run checks at samplesheet and sample level
        check_ss_present()
            Checks samplesheet exists
        add_msg_to_error_dict()
            Add error message to error dictionary
        check_ss_name()
            Validate samplesheet names using seglh-naming Samplesheet module
        check_sequencer_id()
            Check element 2 of samplesheet (sequencer name matches list of allowed names
            in self.sequencer_ids)
        check_ss_contents()
            Check samplesheet not empty (<10 bytes)
        get_data_section()
            Parse data section of samplesheet from file
        development_run()
            Check if the run is a development run, by determining if the run contains
            any development pan numbers
        check_expected_headers()
            Check [Data] section has expected headers, against self.expected_data_headers list
        comp_samplenameid()
            Check whether names match between Sample_ID and Sample_Name in data section
            of samplesheet
        check_illegal_chars(sample, column)
            Returns true if illegal characters present
        check_sample(sample, column)
            Validate sample names using seglh-naming Sample module.
        check_pannos(sample, column, sample_obj)
            Check sample names contain allowed pan numbers from self.panels number list
        check_tso()
            Assigns self.tso as True if TSO run
        log_summary()
            Write summary of validator outcome to log
    """

    def __init__(
        self,
        samplesheet_path: str,
        sequencer_ids: list,
        panels: list,
        tso_panels: list,
        dev_panno: str,
        logdir: str,
    ):
        """
        Constructor for the SamplesheetCheck class
            :param samplesheet_path (str):      Path to samplesheet
            :param sequencer_ids (list):        Allowed sequencer IDs
            :param panels (list):               Allowed pan numbers
            :param tso_panels (list):           TSO500 pan numbers
            :param dev_panno (str):             Development pan number
            :param logdir (str):                Log file directory
        """
        self.samplesheet_path = samplesheet_path
        self.logdir = logdir
        self.logger = False
        self.ss_obj = False
        self.pannumbers = []
        self.tso = False
        # Store sample IDs and sample names from samplesheet
        self.samples = {"Sample_ID": [], "Sample_Name": []}
        self.errors = False  # Switches to True if samplesheet errors encountered
        self.errors_dict = {}
        self.data_headers = []  # Populate with headers from data section
        self.missing_headers = []  # Populate with missing headers
        self.expected_data_headers = ["Sample_ID", "Sample_Name", "index"]
        self.sequencer_ids = sequencer_ids
        self.panels = panels
        self.tso_panels = tso_panels
        self.dev_panno = dev_panno

    def get_logger(self):
        """
        Get logger for the class
            :return (object):    Logger
        """
        runfolder_name = (self.samplesheet_path.split("/")[-1]).split(
            "_SampleSheet.csv"
        )[0]
        logfile_path = f"{os.path.join(self.logdir, runfolder_name)}_{config.TIMESTAMP}_samplesheet_validator.log"
        return SSLogger(logfile_path).get_logger()

    def ss_checks(self) -> None:
        """
        Run checks at samplesheet and sample level. Performs required extra checks for
        checks not included in seglh-naming
        """
        self.logger = self.get_logger()
        if self.check_ss_present():
            setattr(self, "ss_obj", self.check_ss_name())
            if self.ss_obj:
                self.check_sequencer_id()
                if self.check_ss_contents():
                    self.get_data_section()
                    if not self.development_run():
                        self.check_expected_headers()
                        # Check sample id or sample name columns are not missing before
                        # doing sample validation
                        self.comp_samplenameid()
                        for (
                            column,
                            samples,
                        ) in self.samples.items():  # Run checks at the sample level
                            for sample in samples:
                                self.check_illegal_chars(sample, column)
                                sample_obj = self.check_sample(sample, column)
                                if sample_obj:
                                    self.check_pannos(sample, column, sample_obj)
                        self.check_tso()
        self.log_summary()
        shutdown_logs(self.logger)

    def check_ss_present(self) -> Union[bool, None]:
        """
        Checks samplesheet exists.
        Appends info to dict. If samplesheet present returns true, else returns
        false.
            :return True | None:    True if samplesheet exists, else None
        """
        if os.path.isfile(self.samplesheet_path):
            self.logger.info(self.logger.log_msgs["ss_present"], self.samplesheet_path)
            return True
        else:
            self.logger.warning(
                self.logger.log_msgs["ss_absent"], self.samplesheet_path
            )
            self.errors = True
            self.add_msg_to_error_dict(
                "Samplesheet absent",
                self.logger.log_msgs["ss_absent"] % self.samplesheet_path,
            )

    def add_msg_to_error_dict(self, key: str, message) -> None:
        """
        Add error message to error dictionary
            :param key (str):       Key to add to dictionary
            :param message (str):   Message string to add to dictionary
        """
        if key in self.errors_dict:
            self.errors_dict[key].append(message)
        else:
            self.errors_dict[key] = [message]

    def check_ss_name(self) -> object:
        """
        Validate samplesheet names using seglh-naming Samplesheet module.
            :return ss_obj (obj):   seglh-naming samplesheet object
        """
        try:
            self.ss_obj = Samplesheet.from_string(self.samplesheet_path)
            self.logger.info(
                self.logger.log_msgs["ssname_valid"], self.samplesheet_path
            )
        except Exception as exception:
            self.errors = True
            self.add_msg_to_error_dict(
                "Samplesheet name invalid",
                self.logger.log_msgs["ssname_invalid"]
                % (self.samplesheet_path, exception),
            )
            self.logger.warning(
                self.logger.log_msgs["ssname_invalid"], self.samplesheet_path, exception
            )
        return self.ss_obj

    def development_run(self) -> Union[bool, None]:
        """
        Check if the run is a development run, by determining if the samplesheet contains
        any development pan numbers
            :param sscheck_obj (object):    Object created by
                                            samplesheet_validator.SampleheetCheck
            :return True | None:            True if contains dev pan numbers, None if does not
        """
        strings_to_check = self.samples["Sample_ID"] + self.samples["Sample_Name"]
        if any(self.dev_panno in sample_name for sample_name in strings_to_check):
            self.logger.info(
                self.logger.log_msgs["dev_run"],
                self.samplesheet_path,
            )
            setattr(self, "dev_run", True)
            return True
        else:
            self.logger.info(
                self.logger.log_msgs["not_dev_run"],
                self.samplesheet_path,
            )
            setattr(self, "dev_run", False)

    def check_sequencer_id(self) -> None:
        """
        Check element 2 of samplesheet (sequencer name matches list of
        allowed names in self.sequencer_ids)
            :return None:
        """
        if self.ss_obj.sequencerid not in self.sequencer_ids:
            self.errors = True
            self.add_msg_to_error_dict(
                "Sequencer ID invalid",
                self.logger.log_msgs["sequencer_id_invalid"]
                % (self.ss_obj, self.ss_obj.sequencerid),
            )
            self.logger.warning(
                self.logger.log_msgs["sequencer_id_invalid"]
                % (self.ss_obj, self.ss_obj.sequencerid)
            )
        else:
            self.logger.info(self.logger.log_msgs["sequencer_id_valid"])

    def check_ss_contents(self) -> Union[bool, None]:
        """
        Check samplesheet not empty (<10 bytes)
            :return (True | None): True if samplesheet not empty, else None
        """
        if os.stat(self.samplesheet_path).st_size < 10:
            self.logger.warning(self.logger.log_msgs["ss_empty"])
            self.errors = True
            self.add_msg_to_error_dict(
                "Samplesheet is empty", self.logger.log_msgs["ss_empty"]
            )
        else:
            self.logger.info(self.logger.log_msgs["ss_not_empty"])
            return True

    def get_data_section(self) -> None:
        """
        Parse data section of samplesheet from file. Read samplesheet in reverse order,
        collect sample ID and sample name
            :return None:
        """
        with open(self.samplesheet_path, "r") as samplesheet_stream:
            for line in reversed(samplesheet_stream.readlines()):
                # If line contains table headers, stop looping through the file
                if any(header in line for header in self.expected_data_headers):
                    self.extract_headers(line)
                    break
                elif len(line.split(",")[0]) < 2:
                    self.logger.info(self.logger.log_msgs["found_empty_line"])
                    pass  # Skip empty lines
                else:  # Contains sample
                    self.extract_sample_name_id(line)

    def extract_headers(self, line: str) -> None:
        """
        Extract headers from line
            :param line (str):  Line containing samplesheet headers
        """
        try:
            self.logger.info(self.logger.log_msgs["found_header_line"])
            self.data_headers = line.split(",")
        except Exception as exception:
            self.errors = True
            self.logger.warning(
                self.logger.log_msgs["error_extracting_headers"], exception
            )
            self.add_msg_to_error_dict(
                "Error extracting headers",
                self.logger.log_msgs["error_extracting_headers"] % exception,
            )

    def extract_sample_name_id(self, line: str) -> None:
        """
        Extract sample name and sample id from samplesheet line
            :param line (str):  Line containing sample details
        """
        self.logger.info(self.logger.log_msgs["found_sample_line"])
        for column_details in [("Sample_ID", 0), ("Sample_Name", 1)]:
            col_name, index = column_details
            try:
                self.samples[col_name].append(line.split(",")[index])
            except Exception as exception:
                self.errors = True
                self.logger.warning(
                    self.logger.log_msgs["col_extraction_error"],
                    col_name,
                    line,
                    exception,
                )
                self.add_msg_to_error_dict(
                    "Error extracting sample name and ID",
                    self.logger.log_msgs["col_extraction_error"]
                    % (col_name, line, exception),
                )

    def check_expected_headers(self) -> None:
        """
        Check [Data] section has expected headers, against self.expected_data_headers
        list
            :return None:
        """
        if not all(
            header in self.data_headers for header in self.expected_data_headers
        ):
            self.errors = True
            self.add_msg_to_error_dict(
                "Missing headers",
                self.logger.log_msgs["headers_err"] % self.missing_headers,
            )
            self.missing_headers = list(
                set(self.expected_data_headers).difference(self.data_headers)
            )
            self.logger.warning(
                self.logger.log_msgs["headers_err"], self.missing_headers
            )
        else:
            self.logger.info(self.logger.log_msgs["headers_as_expected"])

    def comp_samplenameid(self) -> None:
        """
        Check whether names match between Sample_ID and Sample_Name in data section of
        samplesheet
            :return None:
        """
        differences = ", ".join(
            map(
                str,
                (
                    list(
                        set(self.samples["Sample_ID"])
                        - set(self.samples["Sample_Name"])
                    )
                ),
            )
        )
        self.logger.info(self.logger.log_msgs["samplenames_match"])
        if differences:
            self.errors = True
            self.add_msg_to_error_dict(
                "Sample names do not match",
                self.logger.log_msgs["nonmatching_samplenames"] % differences,
            )
            self.logger.warning(
                self.logger.log_msgs["nonmatching_samplenames"], differences
            )

    def check_illegal_chars(self, sample: str, column: str) -> None:
        """
        Returns true if illegal characters present
            :param sample (str): Sample name
            :param column (str): Column header
            :return None:
        """
        valid_chars = "^[A-Za-z0-9_-]+$"
        if not re.match(valid_chars, sample):
            self.errors = True
            self.add_msg_to_error_dict(
                "Illegal characters",
                self.logger.log_msgs["illegal_chars"] % (column, sample),
            )
            self.logger.warning(self.logger.log_msgs["illegal_chars"], column, sample)
        else:
            self.logger.info(self.logger.log_msgs["no_illegal_chars"], sample, column)

    def check_sample(self, sample: str, column: str) -> Union[object, None]:
        """
        Validate sample names using seglh-naming Sample module. Checks run on
        Sample_Name and Sample_ID; Sample_Name is used by bcl2fastq2 and Sample_ID is
        used if Sample_Name is not present
            :param sample (str):               Sample name
            :param column (str):               Column header
            :return sample_obj (obj):   seglh-naming sample object
        """
        try:
            sample_obj = Sample.from_string(sample)
            self.logger.info(self.logger.log_msgs["sample_name_valid"], sample, column)
            return sample_obj
        except Exception as exception:
            self.errors = True
            self.add_msg_to_error_dict(
                "Sample name invalid",
                self.logger.log_msgs["sample_name_invalid"] % (column, exception),
            )
            self.logger.warning(
                self.logger.log_msgs["sample_name_invalid"],
                column,
                exception,
            )

    def check_pannos(self, sample: str, column: str, sample_obj: object) -> None:
        """
        Check sample names contain allowed pan numbers from self.panels number list
            :param sample (str):            Sample name
            :param column (str):            Column header
            :param sample_obj (object):     seglh-naming sample object
            :return None:
        """
        self.pannumbers.append(sample_obj.panelnumber)
        if sample_obj.panelnumber not in self.panels:
            self.errors = True
            self.add_msg_to_error_dict(
                "Pan number invalid",
                self.logger.log_msgs["invalid_panno"]
                % (sample_obj.panelnumber, column, sample),
            )
            self.logger.warning(
                self.logger.log_msgs["invalid_panno"],
                sample_obj.panelnumber,
                column,
                sample,
            )
        else:
            self.logger.info(
                self.logger.log_msgs["valid_panno"], sample_obj.panelnumber
            )

    def check_tso(self) -> None:
        """
        Assigns self.tso as True if TSO run
            :return None:
        """
        if set(self.pannumbers).intersection(set(self.tso_panels)):
            self.logger.info(self.logger.log_msgs["tso_run"])
            self.tso = True
        else:
            self.logger.info(self.logger.log_msgs["not_tso_run"])

    def log_summary(self) -> None:
        """
        Write summary of validator outcome to log
            :return None:
        """
        if self.errors:
            self.logger.warning(
                self.logger.log_msgs["sschecks_not_passed"], self.samplesheet_path
            )
        else:
            self.logger.info(
                self.logger.log_msgs["sschecks_passed"], self.samplesheet_path
            )
