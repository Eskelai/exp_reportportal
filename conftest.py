import pytest
import logging

from reportportal_client import RPLogger


def pytest_addoption(parser):
    # Method to add the option to ini
    parser.addini("rp_uuid", "RP UUID value", type="string")
    parser.addini("rp_endpoint", "Endpoint to RP", type="string")
    parser.addini("rp_project", "Name of RP project", type="string")
    parser.addini("rp_launch", "Name of launch", type="string")


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger


@pytest.hookimpl()
def pytest_configure(config):
    marker = config.getoption("markexpr")

    # config.addinivalue_line("rp_uuid", "4409595e-a0df-4b51-a20d-83ec48ebc904")
    # NOTE: that func adds it as list, but we need a string

    config._inicache["rp_uuid"] = "4409595e-a0df-4b51-a20d-83ec48ebc904"
    config._inicache["rp_endpoint"] = "http://localhost:8080"
    config._inicache["rp_project"] = "superadmin_personal"

    if marker == "gui_test":
        config._inicache["rp_launch"] = "gui_test"
    elif marker == "api_test":
        config._inicache["rp_launch"] = "api_test"
    elif marker == "random":
        config._inicache["rp_rerun"] = "True"
        config._inicache["rp_launch"] = "random"
    else:
        config._inicache["rp_launch"] = "not_specified"
