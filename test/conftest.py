#!/usr/bin/python3
# coding=utf-8
"""
Variables used across test modules, including the setup and teardown fixture
that is run before and after every test
"""
import os
import shutil
import pytest


tempdir = os.path.join(os.path.abspath("test"), "temp/")


def pytest_addoption(parser):
    parser.addoption(
        "--sequencer_ids",
        action="store",
        type=str,
        required=True,
    )
    parser.addoption(
        "--panels",
        action="store",
        type=str,
        required=True,
    )
    parser.addoption(
        "--tso_panels",
        action="store",
        type=str,
        required=True,
    )
    parser.addoption(
        "--dev_panno",
        action="store",
        type=str,
        required=True
    )
    parser.addoption(
        "--logdir",
        action="store",
        type=str,
        required=True,
    )


def pytest_configure(config):
    """
    Set environment variables used across test classes
    """
    os.environ["sequencer_ids"] = config.getoption("sequencer_ids")
    os.environ["panels"] = config.getoption("panels")
    os.environ["tso_panels"] = config.getoption("tso_panels")
    os.environ["dev_panno"] = config.getoption("dev_panno")
    data_dir = os.path.abspath("test/data/")
    os.environ["samplesheet_dir"] = f'{os.path.join(data_dir, "samplesheets")}'
    # Temporary directories to copy test files into and to contain outputs
    os.environ["temp_dir"] = tempdir


@pytest.fixture(scope="function", autouse=True)
def run_before_and_after_tests():
    """
    Setup and teardown before and after each test. Set up temp dir
    for logfiles. After testing is complete, remove temp dir
    """
    # SETUP - cleanup after each test
    if os.path.isdir(tempdir):
        # Remove dir and all flag files created
        shutil.rmtree(tempdir)
    # Create temporary dirs for testing
    os.makedirs(tempdir)
    yield  # Where the testing happens
    # TEARDOWN - cleanup after each test
    if os.path.isdir(tempdir):
        # Remove dir and all flag files created
        shutil.rmtree(tempdir)
