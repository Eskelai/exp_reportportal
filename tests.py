import pytest


@pytest.mark.random
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected, rp_logger):
    """
    Evaluate sum (example from parametrize)
    """
    rp_logger.info(f"{test_input} = {expected}")
    assert eval(test_input) == expected


@pytest.mark.tc_id("ISSUE-123")
def test_case_id_decorator():
    assert True


@pytest.mark.gui_test
def test_gui(rp_logger):
    """
    Docstring about test

    Args:
        rp_logger (_type_): _description_
    """
    rp_logger.info("Case1. Step1")
    x = "this"
    rp_logger.info("x is: %s", x)
    assert "not in" in x

    # Message with an attachment.
    import subprocess

    free_memory = subprocess.check_output("free -h".split())
    rp_logger.info(
        "Case1. Memory consumption",
        attachment={
            "name": "free_memory.txt",
            "data": free_memory,
            "mime": "application/octet-stream",
        },
    )

    # This debug message will not be sent to the Report Portal.
    rp_logger.debug("Case1. Debug message")
    rp_logger.error("Error log message")


@pytest.mark.api_test
def test_api():
    print("API Test")
    pass
