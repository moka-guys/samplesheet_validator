import datetime

TIMESTAMP = str(f"{datetime.datetime.now():%Y%m%d_%H%M%S}")

# Specifies the layout of log records in the final output
LOGGING_FORMATTER = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

LOG_MSGS = {
    "ss_present": "Samplesheet with supplied name exists (%s)",
    "ss_absent": "Samplesheet with supplied name does not exist (%s)",
    "ssname_valid": "Samplesheet name is valid (%s)",
    "ssname_invalid": "Samplesheet name is invalid (%s). Exception: %s",
    "sequencer_id_valid": "Sequencer ID in samplesheet name is valid",
    "sequencer_id_invalid": "Sequencer id not in allowed list (%s, %s)",
    "file_not_empty": "%s is (>10 bytes)",
    "file_empty": "%s is empty (<10 bytes)",
    "found_header_line": "Line %s in samplesheet identified as a header line",
    "found_sample_line": "Line %s in samplesheet identified as containing a sample",
    "error_extracting_headers": "An error was encountered when extracting headers from the samplesheet, from line %s: %s",
    "found_empty_line": "Line %s in samplesheet is an empty line",
    "col_extraction_error": "Exception raised while attempting to extract %s from sample line %s, %s: %s",
    "headers_as_expected": "Expected headers present in samplesheet",
    "headers_err": "Header(/s) missing from [Data] section: '%s'",
    "samplenames_match": "All sample names and sample IDS match",
    "nonmatching_samplenames": "The following Sample IDs do not match the corresponding Sample Name: (%s)",
    "no_illegal_chars": "Sample name %s contains no illegal characters in column %s",
    "illegal_chars": "Sample name contains invalid characters (%s: %s)",
    "sample_name_valid": "Sample name valid: %s (%s)",
    "sample_name_invalid": "Sample name invalid (%s). For Aviti, sample ID/name are in one col. Exception: %s",
    "valid_panno": "Pan no is valid: %s",
    "invalid_panno": "Pan no is invalid: %s (%s: %s)",
    "valid_library_prep_name": "Library prep name is valid: %s",
    "library_prep_name_err": "Library prep name not in allowed list (%s, %s)",
    "dev_run": "Samplesheet is from a development run: %s",
    "not_dev_run": "Samplesheet is not from a development run: %s",
    "tso_run": "Samplesheet is for a TSO run",
    "not_tso_run": "Samplesheet is not for a TSO run",
    "okd_run": "Samplesheet is for a OKD run",
    "not_okd_run": "Samplesheet is not for a OKD run",
    "masterdata_present": "Matching MasterDataFile with supplied name exists (%s)",
    "masterdata_absent": "MasterDataFile with supplied name does not exist (%s)",
    "sschecks_not_passed": "Samplesheet did not pass checks: %s",
    "sschecks_passed": "Samplesheet passed all checks %s",
    "Aviti match": "The run name from sample sheet matches Aviti run %s",
    "Aviti not match": "The run name from sample sheet does not match Aviti run %s"
}
