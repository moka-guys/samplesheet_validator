# Samplesheet Validator

This tool is designed to validate NGS samplesheets prior to downstream processing by performing a series of checks.

It can be used as a standalone process but was designed for integration into automated workflows through instantiation of the SamplesheetCheck class, which records validation outcome in a boolean flag Attribute (self.errors) and errors in a dict (self.errors_dict).

## Use case

The tool has been designed for:
1. Illumina sequencing runs with Samplesheets expected to end in "_SampleSheet.csv".
2. AVITI runs.

Expect run types include:
1. Panel based NGS testing
2. TSO500
3. Oncodeep
4. Archer
5. MSK

**Please note** this tool has been specifically designed for the Genome Informatics Service at Synnovis (including the use of the [seglh-naming](https://github.com/moka-guys/seglh-naming/) library) and therefore might require modifications for integration into alternative workflows.


## Protocol

Samplesheet validation is carried out in a series of consecutive steps with any errors identified recorded in the log file as per the [config file](samplesheet_validator/config.py).

Checks:
1. Samplesheet path provided is valid.
2. Samplesheet matches expected naming:
    - Illumina: checked against[seglh-naming](https://github.com/moka-guys/seglh-naming/) library
    - AVITI: samplesheet name matches run folder name.
3. The sequencer_id is in the allowed/validated list of sequencers for that run type.
4. The samplesheet is not empty (>10 bytes)
5. If the run is a development run. **N.B.** If the run is a dev run no further samplesheet validation is performed. Further checks are only carried out for clinical runs.
6. Samplesheet contains the minimum expected section headers
7. Content in columns "Sample_ID" and "Sample_Name" match for each sample in the samplesheet
8. Samplesheet doesn't contain any illegal characters
9. Sample name matches expected naming convention for all samples. Assessed against [seglh-naming](https://github.com/moka-guys/seglh-naming/) library.
10. The test code (pannumber) for each sample is in the list of expected test codes for the run type.
11. Whether any TSO samples have been included on the run - Sets Boolean Attribute to true
12. Whether any OKD samples are included on the run - Sets Boolean Attribute to true


## Installation & Usage

### From Python package

1. Clone a copy of the repository locally

    `git clone https://github.com/moka-guys/samplesheet_validator.git`

2. cd in to the project root directory

3. Install from python package

    `python3 setup.py install`

    NB's: Requires setuptools to be installed; Use the --user flag or install into an virtualenv/pipenv if not installing globally.

4. Execute functionality from within a python script.

    ```python

    from samplesheet_validator.samplesheet_validator import SamplesheetCheck

    sscheck_obj = SamplesheetCheck(
        samplesheet_path,  # str
        sequencer_ids,  # list
        panels,  # list
        tso_panels,  # list
        okd_panels, # list
        dev_pannos,  # list
        logdir,  # str
        illumina, # bool
        runname, # str
    )
    sscheck_obj.ss_checks()  # Carry out samplesheeet validation

    print(sscheck_obj.errors_dict)  # View the dictionary of error messages
    ```

### Command line

To use the validator from the command line set up an environment as below:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

The script can then be executed as follows:
```bash
usage: Used to validate a samplesheet using the seglh-naming conventions

Given an input samplesheet, will validate the samplesheet using seglh-naming conventions and output a logfile

options:
  -h, --help            show this help message and exit
  -S SAMPLESHEET_PATH, --samplesheet_path SAMPLESHEET_PATH
                        Path to samplesheet requiring validation
  -SI SEQUENCER_IDS, --sequencer_ids SEQUENCER_IDS
                        Comma separated string of allowed sequencer IDS
  -P PANELS, --panels PANELS
                        Comma separated string of allowed panel numbers
  -T TSO_PANELS, --tso_panels TSO_PANELS
                        Comma separated string of tso panels
  -O OKD_PANELS, --okd_panels OKD_PANELS
                        Comma separated string of okd panels
  -D DEV_PANNOS, --dev_pannos DEV_PANNOS
                        Comma separated development pan numbers
  -L LOGDIR, --logdir LOGDIR
                        Directory to save the output logfile to
  -NSH NO_STREAM_HANDLER, --no_stream_handler NO_STRAM_HANDLER
                        Provide flag when we dont want a stream handler (prevents
                        duplication of log messages to terminal if using another
                        logging instance)
  -R RUN_FOLDER_NAME, --runname RUN_FOLDER_NAME
                        Str for processed folder name
```

## Testing

This repository currently has **93% test coverage**.

Test datasets are stored in [/test/data](../test/data). The script has a full test suite:
* [test_samplesheet_validator.py](../test/test_samplesheet_validator.py)

See [test/README.md](test/README.md) for details about test cases.

These tests should be run before pushing any code to ensure all tests in the GitHub Actions workflow pass. These can be run as follows:

```bash
python3 -m pytest
```
**N.B. Tests and test cases/files MUST be maintained and updated accordingly in conjunction with script development. This includes ensuring that the arguments passed to pytest in the [pytest.ini](pytest.ini) file are kept up to date**


## Logging

Logging is performed by [ss_logger](samplesheet_validator/ss_logger.py). The directory to save the log file to is supplied as an argument. The output log file is named by the script as follows:
- `$LOGFILE_DIR/$RUNFOLDER_NAME_$TIMESTAMP_samplesheet_validator.log`

The script also collects the error messages as it runs, which can be used by other scripts when this script is used as an import.


### Developed by the Synnovis Genome Informatics Team
