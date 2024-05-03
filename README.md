# Samplesheet Validator

Checks sample sheet naming and contents. Carries out a series of checks on the sample sheet and collects any errors 
that it identifies (SamplesheetCheck.errors_list). It also identifies whether or not a run is a TSO run from the sample 
sheet (SamplesheetCheck.tso).

## Protocol

Runs a series of checks on the sample sheet, collects any errors identified. Checks whether: 
* Sample sheet exists
* Samplesheet name is valid (validates using the [seglh-naming](https://github.com/moka-guys/seglh-naming/) library)
* Sequencer ID is in the list of allowed sequencer IDs supplied to the script
* Samplesheet is not empty (>10 bytes)
* Samplesheet is for a development run, using the development pan number supplied to the script
* Samplesheet contains the minimum expected `[Data]` section headers: `Sample_ID, Sample_Name, index`
* `Sample_ID` and `Sample_Name` match for each sample in the data section of the samplesheet
* Sample name does not contain any illegal characters
* Sample name is valid (validates using the [seglh-naming](https://github.com/moka-guys/seglh-naming/) library)
* Pan numbers are in the list of allowed pan numbers supplied to the script
* Samplesheet contains any TSO samples

## Usage

### Python package

The repository provides a python package which can be installed with:

`python3 setup.py install`

NB: Use the --user flag or install into an virtualenv/pipenv if not installing globally.

```python

from samplesheet_validator.samplesheet_validator import SamplesheetCheck

sscheck_obj = SamplesheetCheck(
    samplesheet_path,  # str
    sequencer_ids,  # list
    panels,  # list
    tso_panels,  # list
    dev_panno,  # str
    logdir,  # str
)
sscheck_obj.ss_checks()  # Carry out samplesheeet validation

print(sscheck_obj.errors_dict)  # View the dictionary of error messages
```

### Command line

The environment must be set up as follows:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

The script can then be used as follows:
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
  -D DEV_PANNO, --dev_panno DEV_PANNO
                        Development pan number
  -L LOGDIR, --logdir LOGDIR
                        Directory to save the output logfile to
  -NSH NO_STREAM_HANDLER, --no_stream_handler NO_STRAM_HANDLER
                        Provide flag when we don't want a stream handler (prevents
                        duplication of log messages to terminal if using another
                        logging instance)
```

### Testing

This repository currently has **92% test coverage**.

Test datasets are stored in [/test/data](../test/data). The script has a full test suite:
* [test_samplesheet_validator.py](../test/test_samplesheet_validator.py)

See [test/README.md](test/README.md) for details about test cases.

These tests should be run before pushing any code to ensure all tests in the GitHub Actions workflow pass. These can be run as follows:

```bash
python3 -m pytest
```
**N.B. Tests and test cases/files MUST be maintained and updated accordingly in conjunction with script development**
**N.B. This includes ensuring that the arguments passed to pytest in the [pytest.ini](pytest.ini) file are kept up to date**


## Logging

Logging is performed by [ss_logger](samplesheet_validator/ss_logger.py). The directory to save the log file to is supplied as an argument. The output log file is named by the script as follows:
- `$LOGFILE_DIR/$RUNFOLDER_NAME_$TIMESTAMP_samplesheet_validator.log`

The script also collects the error messages as it runs, which can be used by other scripts when this script is used as an import.


### Developed by the Synnovis Genome Informatics Team
