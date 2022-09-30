import pytest


@pytest.mark.second_suit
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected, rp_logger):
    """
    Evaluate sum (example from parametrize)
    """
    rp_logger.info(f"{test_input} = {expected}")
    assert eval(test_input) == expected


@pytest.mark.second_suit
def test_not_api():
    print("Not api")
    pass


@pytest.mark.tc_id("shared-test")
def test_shared_between_suits(rp_logger):
    rp_logger.info("This test is located in first and second suits")
    pass
