from setuptools import setup
from samplesheet_validator.git_tag import git_tag

setup(
    name="samplesheet_validator",
    version=git_tag(),
    description="Python library for samplesheet validation",
    url="https://github.com/moka-guys/samplesheet_validator/tree/feature/fix_stream_handler",
    author="Rachel Duffin",
    author_email="rachel.duffin2@nhs.net",
    license="Apache License, Version 2.0",
    packages=["samplesheet_validator"],
    install_requires=[],
    zip_safe=False,
)
