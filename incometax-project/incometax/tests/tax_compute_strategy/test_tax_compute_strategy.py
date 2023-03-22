from tax_compute_strategy.old_tax_compute_strategy import OldTaxComputeStrategy


def test_old_tax_compute_strategy_compute():
    old_tax_compute_strategy = OldTaxComputeStrategy()
    income = 200
    expected_tax = 200 # dummy test, will be fixed later
    assert old_tax_compute_strategy.compute(income) == expected_tax
