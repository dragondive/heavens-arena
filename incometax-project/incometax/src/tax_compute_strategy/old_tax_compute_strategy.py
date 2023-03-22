import math
import pandas


class OldTaxComputeStrategy:
    def __init__(self) -> None:
        self.tax_brackets = pandas.DataFrame(
            [  # TODO: Accept this data from yaml file so user can configure it
                (0, 2_50_000, 0, 0),
                (2_50_000, 5_00_000, 5, 12_500),
                (5_00_000, 10_00_000, 20, 1_12_500),
                (10_00_000, 0, 30, 0),
            ],
            columns=["Lower_Limit", "Upper_Limit", "Percent", "Maximum_Tax"],
        )

    def compute(self, income):
        income = math.floor(
            income
        )  # Ignore fractional part just as Income Tax website does.

        # Determine brackets whose lower limit is lower than specified income.
        # The highest among them will be the matching bracket.
        # As per Income Tax rule, only the income in excess of lower limit in that bracket
        # will be taxed at the rate of that bracket. In addition, the income until the
        # lower limit will be taxed at the rates in earlier brackets.
        # The filtering is done in this manner to avoid filtering two times (once for the
        # matching bracket, once more for the previous bracket).
        filtered_brackets = self.tax_brackets[self.tax_brackets["Lower_Limit"] < income]

        matching_bracket = filtered_brackets.iloc[-1]
        matching_bracket_component = (
            (income - matching_bracket["Lower_Limit"])
            * matching_bracket["Percent"]
            / 100
        )

        try:
            previous_bracket = filtered_brackets.iloc[-2]
        except IndexError:
            # Special case when matching bracket is the lowest bracket.
            # Hence, there is no "previous" bracket.
            previous_bracket_component = 0
        else:
            # Income until lower limit is taxed according to previous brackets,
            # which would simply be the maximum tax in the previous bracket.
            previous_bracket_component = previous_bracket["Maximum_Tax"]

        # Income Tax website rounds off the computed tax.
        computed_tax = round(matching_bracket_component + previous_bracket_component)
        return computed_tax
