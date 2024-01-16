#!/usr/bin/python3
# coding=utf-8
""" samplesheet_validator.py pytest unit tests
"""
import itertools
import os
import argparse
import pytest
from samplesheet_validator.ss_logger import shutdown_logs
from samplesheet_validator import samplesheet_validator
from samplesheet_validator.__main__ import is_valid_dir, is_valid_file


def get_sscheck_obj(samplesheet: str) -> object:
    """
    Function to retrieve a samplesheet check object and carry out the
    samplesheet checks for a supplied samplesheet
        :param samplesheet (str):       Samplesheet path
        :return sscheck_obj (object:    SamplesheetCheck object
    """
    sscheck_obj = samplesheet_validator.SamplesheetCheck(
        samplesheet,
        os.getenv("sequencer_ids").split(","),
        os.getenv("panels").split(","),
        os.getenv("tso_panels").split(","),
        os.getenv("dev_panno"),
        os.getenv("temp_dir"),
    )
    sscheck_obj.ss_checks()
    return sscheck_obj


@pytest.fixture(scope="function")
def valid_dirs():
    """
    Directories that exist
    """
    return [os.getcwd(), os.getenv("samplesheet_dir")]


@pytest.fixture(scope="function")
def invalid_dirs():
    """
    Directories that do not exist
    """
    return ["/this/is/invalid/", "/also/is/invalid/"]


@pytest.fixture(scope="function")
def valid_dev_samplesheet():
    """
    Samplesheet for a development run
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "valid",
            "231012_M02631_0285_000000000-LBGMH_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def valid_custompanels_samplesheet():
    """
    Valid Custom Panels samplesheets
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "valid",
            "210917_NB551068_0409_AH3YNFAFX3_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def valid_lrpcr_samplesheet():
    """
    Valid LRPCR samplesheets
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "valid",
            "230309_M02631_0275_000000000-KRDLT_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def valid_tso_samplesheet():
    """
    Valid TSO samplesheets
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "valid",
            "221021_A01229_0145_BHGGTHDMXY_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def valid_wes_samplesheet():
    """
    Valid WES samplesheets
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "valid",
            "221024_A01229_0146_BHKGG2DRX2_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def valid_adx_samplesheet():
    """
    Valid ADX samplesheets
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "valid",
            "231201_NB552085_0291_AHVNWYAFX5_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def valid_snp_samplesheet():
    """
    Valid SNP samplesheets
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "valid",
            "231116_NB551068_0551_AHLCYNAFX5_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def valid_samplesheets_no_dev(
    valid_tso_samplesheet,
    valid_custompanels_samplesheet,
    valid_lrpcr_samplesheet,
    valid_wes_samplesheet,
    valid_adx_samplesheet,
    valid_snp_samplesheet,
):
    """
    Test cases with valid paths, files are populated, and valid samplesheet names, and
    contain:
        Expected headers, matching Sample_IDs and Sample_Names, valid samples, valid pan nos
    """
    return list(
        itertools.chain(
            valid_tso_samplesheet,
            valid_custompanels_samplesheet,
            valid_lrpcr_samplesheet,
            valid_wes_samplesheet,
            valid_adx_samplesheet,
            valid_snp_samplesheet,
        )
    )


@pytest.fixture(scope="function")
def valid_samplesheets_with_dev(
    valid_samplesheets_no_dev,
    valid_dev_samplesheet,
):
    """
    All valid samplesheets, including development run samplesheet
    """
    return list(
        itertools.chain(
            valid_samplesheets_no_dev,
            valid_dev_samplesheet,
        )
    )


@pytest.fixture(scope="function")
def not_tso_samplesheet(
    valid_custompanels_samplesheet,
    valid_lrpcr_samplesheet,
    valid_wes_samplesheet,
    valid_adx_samplesheet,
):
    """ """
    return list(
        itertools.chain(
            valid_custompanels_samplesheet,
            valid_lrpcr_samplesheet,
            valid_wes_samplesheet,
            valid_adx_samplesheet,
        )
    )


@pytest.fixture(scope="function")
def invalid_paths():
    """
    Collection of nonexistent samplesheets
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "210408_M02631_0186_000000000-JFMNN_SampleSheet.csv",
        ),
        os.path.join(
            os.getenv("samplesheet_dir"),
            "210918_NB551068_551068_0409_AH3YNFAFX3_SampleSheet.csv",
        ),
        os.path.join(
            os.getenv("samplesheet_dir"),
            "221021_A01229_0143_BHGGTHDMXY_SampleSheet.csv",
        ),
    ]


@pytest.fixture(scope="function")
def invalid_ss_date():
    """
    Samplesheet exists but has invalid date
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "21108_A01229_0040_AHKGTFDRXY_SampleSheet.csv",
        ),
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "21aA08_A01229_0040_AHKGTFDRXY_SampleSheet.csv",
        ),
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "2110915_M02353_0632_000000000-K242J_SampleSheet.csv",
        ),
    ]


@pytest.fixture(scope="function")
def invalid_ss_sequencerid():
    """
    Samplesheet exists but has invalid sequencer ID
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "211008_1229_0040_AHKGTFDRXY_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_ss_autoincrono():
    """
    Samplesheet exists but has invalid autoincrementing_number
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "211008_A01229_0_AHKGTFDRXY_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_ss_flowcellid():
    """
    Samplesheet with invalid flow cell ID
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "211008_A01229_0040_1AHK£lRXY_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_ss_samplesheetstr():
    """
    Samplesheet with invalid 'SampleSheet' string
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "211008_A01229_0040_AHKGTFDRXY_samplesheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_ss_wrong_naming_format():
    """
    Samplesheet with wrong naming format
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "211008_A01229_AHKGTFDRXY_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_ss_invalid_extension():
    """
    Samplesheet with wrong file extension
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "211008_A01229_AHKGTFDRXY_SampleSheet.abc",
        )
    ]


@pytest.fixture(scope="function")
def invalid_names(
    invalid_ss_date,
    invalid_ss_sequencerid,
    invalid_ss_autoincrono,
    invalid_ss_flowcellid,
    invalid_ss_samplesheetstr,
    invalid_ss_wrong_naming_format,
    invalid_ss_invalid_extension,
):
    """
    Collection of samplesheets with invalid names
    """
    return list(
        itertools.chain(
            invalid_ss_date,
            invalid_ss_sequencerid,
            invalid_ss_autoincrono,
            invalid_ss_flowcellid,
            invalid_ss_samplesheetstr,
            invalid_ss_wrong_naming_format,
            invalid_ss_invalid_extension,
        )
    )


@pytest.fixture(scope="function")
def empty_file():
    """
    Empty samplesheet with valid name
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "220413_A01229_0032_AHKGTFDRXY_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_headers():
    """
    Samplesheet containing invalid contents - invalid headers
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "230309_M02631_0123_000000000-KRDLT_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def non_matching_samplenames():
    """
    Samplesheet containing invalid contents - non matching sample names
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "230309_M02631_0123_000000000-ABCDE_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_sample_naming_format():
    """
    Samplesheet containing invalid contents - wrong naming format
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "210917_NB551068_0409_ABCDEFGJIK_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def too_few_sample_identifiers():
    """
    Samplesheet containing invalid contents - Not enough identifiers in sample name
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "231012_M02631_1234_000000000-LBGMH_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def tso_samplename_too_long():
    """
    Samplesheet containing invalid contents - TSO sample name too long
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "221021_A01229_0398_BHGGTHDMXY_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_libraryprep_name():
    """
    Samplesheet containing invalid contents - invalid library prep name (does not conform to seglh-naming)
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "221024_A01229_3746_BERIOG2DRX2_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_sample_count():
    """
    Samplesheet containing invalid contents - invalid sample count
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "210917_NB551068_9876_AH3YNFAFX3_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_dna_number():
    """
    Samplesheet containing invalid contents - specimen/DNA number invalid
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "230309_M02631_0345_000000000-KRDLT_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_secondary_identifier():
    """
    Samplesheet containing invalid contents - invalid secondary identifier
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "221021_A01229_0145_ZXYEORIUGI_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_initials():
    """
    Samplesheet containing invalid contents - invalid initials
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "230309_M02631_0275_000000000-ERTGL_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_sex():
    """
    Samplesheet containing invalid contents - invalid sex
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "220506_NB551068_0409_AH3YNFAFX3_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_panel_name():
    """
    Samplesheet containing invalid contents - invalid panel name
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "230309_M02631_4567_000000000-KRDLT_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_panel_number():
    """
    Samplesheet containing invalid contents - invalid panel number
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "231201_NB552085_0945_AHVNWYERYU_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_internal_chars():
    """
    Samplesheet containing invalid contents - invalid characters
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "221024_A01229_0345_BERTYG2DRX2_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def invalid_samplename(
    invalid_sample_naming_format,
    too_few_sample_identifiers,
    tso_samplename_too_long,
    invalid_libraryprep_name,
    invalid_sample_count,
    invalid_dna_number,
    invalid_secondary_identifier,
    invalid_initials,
    invalid_sex,
    invalid_panel_name,
    invalid_panel_number,
    invalid_internal_chars,
):
    """ """
    return list(
        itertools.chain(
            invalid_sample_naming_format,
            too_few_sample_identifiers,
            tso_samplename_too_long,
            invalid_libraryprep_name,
            invalid_sample_count,
            invalid_dna_number,
            invalid_secondary_identifier,
            invalid_initials,
            invalid_sex,
            invalid_panel_name,
            invalid_panel_number,
            invalid_internal_chars,
        )
    )


@pytest.fixture(scope="function")
def invalid_contents(
    invalid_headers,
    non_matching_samplenames,
    invalid_samplename,
):
    """
    Test cases covering invalid content errors
    """
    return list(
        itertools.chain(
            invalid_headers,
            non_matching_samplenames,
            invalid_samplename,
        )
    )


@pytest.fixture(scope="function")
def samplesheets_fail_parsing():
    """
    Samplesheets that should not be parsable to extract the data section
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "221024_A01229_0146_EIROFPWYJL_SampleSheet.csv",
        )
    ]


@pytest.fixture(scope="function")
def ss_with_disallowed_sserrs(
    empty_file,
    invalid_paths,
    invalid_names,
    invalid_contents,
    invalid_internal_chars,
    samplesheets_fail_parsing,
):
    """
    Samplesheets with disallowed errors in the more stringent set of requirements
    than the base samplesheet validator check. These lists have been imported from
    the test_samplesheet_validator test suite
    """
    return list(
        itertools.chain(
            empty_file,
            invalid_paths,
            invalid_names,
            invalid_contents,
            invalid_internal_chars,
            samplesheets_fail_parsing,
        )
    )


@pytest.fixture(scope="function")
def samplesheets_exist(
    valid_samplesheets_with_dev,
    empty_file,
    invalid_names,
    invalid_contents,
    invalid_internal_chars,
    samplesheets_fail_parsing,
):
    """
    Samplesheets that exist
    """
    return list(
        itertools.chain(
            valid_samplesheets_with_dev,
            empty_file,
            invalid_names,
            invalid_contents,
            invalid_internal_chars,
            samplesheets_fail_parsing,
        )
    )


@pytest.fixture(scope="function")
def samplesheets_multiple_errors():
    """
    Samplesheet containing multiple errors
    """
    return [
        os.path.join(
            os.getenv("samplesheet_dir"),
            "invalid",
            "230309_E02631_4297_000000000-KRDLT_SampleSheet.csv",
        )
    ]


def test_is_valid_file_valid(samplesheets_exist):
    """
    Test that is_valid_file correctly determines that file exists
    """
    for samplesheet in samplesheets_exist:
        parser = argparse.ArgumentParser()
        file = is_valid_file(parser, samplesheet)
        assert file == samplesheet


def test_is_valid_file_invalid(invalid_paths):
    """
    Test that is_valid_file correctly determines that file does not exist
    """
    for samplesheet in invalid_paths:
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            parser = argparse.ArgumentParser()
            file = is_valid_file(parser, samplesheet)
            assert not file
            assert pytest_wrapped_e.type == SystemExit
            assert pytest_wrapped_e.value.code == 1


def test_is_valid_dir_valid(valid_dirs):
    """
    Test that is_valid_dir correctly determines that directory exists
    """
    for dir in valid_dirs:
        parser = argparse.ArgumentParser()
        dir = is_valid_dir(parser, dir)
        assert dir == dir


def test_is_valid_dir_invalid(invalid_dirs):
    """
    Test that is_valid_dir correctly determines that directory does not exist
    """
    for dir in invalid_dirs:
        with pytest.raises(SystemExit) as pytest_wrapped_e:
            parser = argparse.ArgumentParser()
            dir = is_valid_dir(parser, dir)
            assert not dir
            assert pytest_wrapped_e.type == SystemExit
            assert pytest_wrapped_e.value.code == 1


class TestSamplesheetCheck(object):
    """
    Tests for the SamplesheetCheck class
    """

    def test_ss_checks_pass(self, valid_samplesheets_with_dev, caplog):
        """ """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_ss_checks_fail(self, ss_with_disallowed_sserrs, caplog):
        """ """
        for samplesheet in ss_with_disallowed_sserrs:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_ss_present_valid(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that the samplesheet is present
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Samplesheet with supplied name exists" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_ss_present_invalid(self, invalid_paths, caplog):
        """
        Test function is able to correctly identify that the samplesheet is absent
        """
        for samplesheet in invalid_paths:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "Samplesheet with supplied name does not exist" in caplog.text
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_ss_name_valid(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that sample names are valid
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Samplesheet name is valid" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_ss_name_invalid(self, invalid_names, caplog):
        """
        Test function is able to correctly identify that sample names are invalid
        """
        for samplesheet in invalid_names:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "Samplesheet name is invalid" in caplog.text
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_development_run_true(self, valid_dev_samplesheet, caplog):
        """
        Test function is able to correctly identify that the run is a development run
        """
        for samplesheet in valid_dev_samplesheet:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Samplesheet is from a development run" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_development_run_false(self, valid_tso_samplesheet, caplog):
        """
        Test function is able to correctly identify that the run is not a development run
        """
        for samplesheet in valid_tso_samplesheet:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Samplesheet is not from a development run" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_sequencer_id_valid(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that sequencer ids are valid
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Sequencer ID in samplesheet name is valid" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_sequencer_id_invalid(self, invalid_ss_sequencerid, caplog):
        """
        Test function is able to correctly identify that sequencer ids are invalid
        """
        for samplesheet in invalid_ss_sequencerid:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "Sequencer id not in allowed list" in caplog.text
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_ss_contents_populated(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that samplesheet is not empty
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Samplesheet is (>10 bytes)" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_ss_contents_empty(self, empty_file, caplog):
        """
        Test function is able to correctly identify that samplesheet is empty
        """
        for samplesheet in empty_file:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "Samplesheet empty (<10 bytes)" in caplog.text
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_get_data_section_pass(self, valid_samplesheets_with_dev, caplog):
        """ """
        for samplesheet in valid_samplesheets_with_dev:
            get_sscheck_obj(samplesheet)
            assert "WARNING" not in caplog.text

    def test_get_data_section_fail(self, samplesheets_fail_parsing, caplog):
        """ """
        for samplesheet in samplesheets_fail_parsing:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_extract_sample_name_id_pass(self, valid_samplesheets_with_dev, caplog):
        """ """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert (
                "Line in samplesheet identified as containing a sample" in caplog.text
            )
            shutdown_logs(sscheck_obj.logger)

    def test_extract_sample_name_id_fail(self, samplesheets_fail_parsing, caplog):
        """ """
        for samplesheet in samplesheets_fail_parsing:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert "Exception raised while attempting to extract" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_expected_headers_valid(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that samplesheet headers are valid
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Expected headers present in samplesheet" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_expected_headers_invalid(self, invalid_headers, caplog):
        """
        Test function is able to correctly identify that samplesheet headers are invalid
        """
        for samplesheet in invalid_headers:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "Header(/s) missing from [Data] section:" in caplog.text
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_comp_samplenameid_valid(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that samplename and sampleid match
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "All sample names and sample IDS match" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_comp_samplenameid_invalid(self, non_matching_samplenames, caplog):
        """
        Test function is able to correctly identify that samplename and sampleid do not
        match
        """
        for samplesheet in non_matching_samplenames:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert (
                "The following Sample IDs do not match the corresponding Sample Name"
                in caplog.text
            )
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_illegal_chars_valid(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that samplename does not contain
        invalid characters
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "contains no illegal characters in column" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def check_illegal_chars_invalid(self, invalid_internal_chars, caplog):
        """
        Test function is able to correctly identify that samplename contains invalid
        characters
        """
        for samplesheet in invalid_internal_chars:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "Sample name contains invalid characters" in caplog.text
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_sample_valid(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that sample name is valid
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Sample name valid" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_sample_invalid(self, invalid_samplename, caplog):
        """
        Test function is able to correctly identify that sample name is not valid
        """
        for samplesheet in invalid_samplename:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "Sample name invalid" in caplog.text
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_pannos_valid(self, valid_samplesheets_with_dev, caplog):
        """
        Test function is able to correctly identify that panel numbers are valid
        """
        for samplesheet in valid_samplesheets_with_dev:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.errors
            assert "Pan no is valid" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_pannos_invalid(self, invalid_panel_number, caplog):
        """
        Test function is able to correctly identify that panel numbers are not valid
        """
        for samplesheet in invalid_panel_number:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert "Pan no is invalid" in caplog.text
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_tso_true(self, valid_tso_samplesheet, caplog):
        """
        Test function is able to correctly identify that samples are TSO
        """
        for samplesheet in valid_tso_samplesheet:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.tso
            assert "Samplesheet is for a TSO run" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_check_tso_false(self, not_tso_samplesheet, caplog):
        """
        Test function is able to correctly identify that samples are not TSO
        """
        for samplesheet in not_tso_samplesheet:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert not sscheck_obj.tso
            assert "Samplesheet is not for a TSO run" in caplog.text
            assert "WARNING" not in caplog.text
            shutdown_logs(sscheck_obj.logger)

    def test_log_summary_noerrors(self, valid_samplesheets_with_dev, caplog):
        """
        Test log_summary correctly logs summary of no errors
        """
        for samplesheet in valid_samplesheets_with_dev:
            get_sscheck_obj(samplesheet)
            assert "Samplesheet passed all checks" in caplog.text

    def test_log_summary_errors(self, ss_with_disallowed_sserrs, caplog):
        """
        Test log_summary correctly logs summary of errors
        """
        for samplesheet in ss_with_disallowed_sserrs:
            get_sscheck_obj(samplesheet)
            assert "Samplesheet did not pass checks" in caplog.text

    def test_multiple_errors(self, samplesheets_multiple_errors, caplog):
        """
        Tests all expected errors are present at once - invalid sequencer id, invalid
        headers, invalid sample names, non-matching samplenames, invalid panel number,
        invalid runtype
        """
        msgs = [
            "Sequencer id not in allowed list",
            "Header(/s) missing from [Data] section",
            "The following Sample IDs do not match the corresponding Sample Name",
            "Sample name invalid",
            "Pan no is invalid",
        ]
        for samplesheet in samplesheets_multiple_errors:
            sscheck_obj = get_sscheck_obj(samplesheet)
            assert sscheck_obj.errors
            assert all(msg in caplog.text for msg in msgs)
            assert "WARNING" in caplog.text
            shutdown_logs(sscheck_obj.logger)
