import os
import argparse
from .samplesheet_validator import SamplesheetCheck


def get_arguments():
    """
    Uses argparse module to define and handle command line input arguments
    and help menu
        :return argparse.Namespace (object):    Contains the parsed arguments
    """
    parser = argparse.ArgumentParser(
        description=(
            "Given an input samplesheet, will validate the samplesheet using "
            "seglh-naming conventions and output a logfile"
        ),
        usage="Used to validate a samplesheet using the seglh-naming conventions",
    )
    parser.add_argument(
        "-S",
        "--samplesheet_path",
        type=lambda x: is_valid_file(parser, x),
        required=True,
        help="Path to samplesheet requiring validation",
    )
    parser.add_argument(
        "-SI",
        "--sequencer_ids",
        type=str,
        required=True,
        help="Comma separated string of allowed sequencer IDS",
    )
    parser.add_argument(
        "-P",
        "--panels",
        type=str,
        required=True,
        help="Comma separated string of allowed panel numbers",
    )
    parser.add_argument(
        "-R",
        "--library_prep_names",
        type=str,
        required=True,
        help="Comma separated string of allowed library prep names",
    )
    parser.add_argument(
        "-T",
        "--tso_panels",
        type=str,
        required=True,
        help="Comma separated string of tso panels",
    )
    parser.add_argument(
        "-D",
        "--dev_panno",
        type=str,
        required=True,
        help="Development pan number",
    )
    parser.add_argument(
        "-L",
        "--logdir",
        type=lambda x: is_valid_dir(parser, x),
        required=True,
        help="Directory to save the output logfile to",
    )
    return parser.parse_args()


def is_valid_file(parser: argparse.ArgumentParser, file: str) -> str:
    """
    Check file path is valid
        :param parser (argparse.ArgumentParser):    Holds necessary info to parse cmd
                                                    line into Python data types
        :param file (str):                          Input argument
    """
    if not os.path.exists(file):
        parser.error(f"The file {file} does not exist!")
    else:
        return file


def is_valid_dir(parser: argparse.ArgumentParser, dir: str) -> str:
    """
    Check directory path is valid
        :param parser (argparse.ArgumentParser):    Holds necessary info to parse cmd
                                                    line into Python data types
        :param file (str):                          Input argument
    """
    if not os.path.isdir(dir):
        parser.error(f"The directory {dir} does not exist!")
    else:
        return dir


if __name__ == '__main__':
    parsed_args = get_arguments()
    sscheck_obj = SamplesheetCheck(
        parsed_args.samplesheet_path,
        parsed_args.sequencer_ids,
        parsed_args.panels,
        parsed_args.library_prep_names,
        parsed_args.tso_panels,
        parsed_args.dev_panno,
        parsed_args.logdir,
    )
    sscheck_obj.ss_checks()  # Carry out samplesheeet validation
