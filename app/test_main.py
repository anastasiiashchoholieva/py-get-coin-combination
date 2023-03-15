import pytest
from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents, result",
    [
        pytest.param(1, [1, 0, 0, 0], id="1 cent"),
        pytest.param(6, [1, 1, 0, 0], id="1 cent + 1 nickel"),
        pytest.param(17, [2, 1, 1, 0], id="2 pennies + 1 nickel + 1 dime"),
        pytest.param(50, [0, 0, 0, 2], id="2 quarters"),
    ]
)
def test_when_age_changes(
    cents: int,
    result: list
) -> None:
    assert (get_coin_combination(cents) == result)
