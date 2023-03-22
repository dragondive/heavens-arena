import argparse

from tax_compute_strategy.old_tax_compute_strategy import OldTaxComputeStrategy

parser = argparse.ArgumentParser(
    prog="incometax",
    description="Computes income tax according to Indian tax laws",
)
parser.add_argument(
    "--income_from_salary",
    required=True,
    type=int,
    help="Total income from salary, without excluding exemptions, deductions, etc.",
    metavar="Income from Salary",
)
args = parser.parse_args()
tax_compute_strategy = OldTaxComputeStrategy()
print(tax_compute_strategy.compute(args.income_from_salary))
