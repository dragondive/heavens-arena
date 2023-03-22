import pytest

from tax_compute_strategy.old_tax_compute_strategy import OldTaxComputeStrategy


@pytest.mark.parametrize(
    "income,expected_tax",
    [
        (1_75_000.52, 0),  # check if float values are accepted
        (2_00_000, 0),  # lowest bracket
        (2_50_000, 0),  # upper limit of lowest bracket
        (2_50_001, 0),  # check roundoff near bracket limit
        (4_13_786, 8189),  # arbitrary number in middle of bracket
        (4_99_999, 12500),  # near bracket limit
        (5_00_000, 12500),  # bracket limit
        (5_00_001, 12500),  # near bracket limit
        (8_96_247.13, 91749),  # fractional part of tax is 0.4, should round down
        (8_96_248.83, 91750),  # fractional part of tax is 0.6, should round up
        (9_99_999, 112500),  # near bracket limit
        (10_00_000, 112500),  # bracket limit
        (10_00_001, 112500),  # near bracket limit
        (15_45_775, 276232),  # arbitrary number in top bracket
        (25_85_176, 588053),  # arbitrary number in top bracket
    ],
)
def test_old_tax_compute_strategy_compute(income, expected_tax):
    old_tax_compute_strategy = OldTaxComputeStrategy()
    assert old_tax_compute_strategy.compute(income) == expected_tax
