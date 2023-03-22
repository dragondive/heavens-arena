from tax_compute_strategy.old_tax_compute_strategy import OldTaxComputeStrategy


def test_old_tax_compute_strategy_compute():
    old_tax_compute_strategy = OldTaxComputeStrategy()
    expected_tax = 200
    assert old_tax_compute_strategy.compute() == expected_tax
