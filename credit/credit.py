import sys
import unittest
from enum import Enum


class CreditCard(Enum):
    AMEX = 1
    MASTERCARD = 2
    VISA = 3
    INVALID = 4


def which_credit_card(credit_number: int) -> CreditCard:
    pass


def main():
    """
    Todo:
    - Take user input
    - Validate user input
    - Validate if it's a valid credit card
    - Identify which company it belongs to
    """
    credit_number: int = int(input("Number: "))

    result: CreditCard = which_credit_card(credit_number)
    print(result.name)


class TestCredit(unittest.TestCase):
    def test_AMEX(self):
        self.assertEqual(which_credit_card(78282246310005), CreditCard.AMEX)
        self.assertEqual(which_credit_card(71449635398431), CreditCard.AMEX)
        self.assertEqual(which_credit_card(78734493671000), CreditCard.AMEX)
        self.assertEqual(which_credit_card(378282246310005), CreditCard.AMEX)
        self.assertEqual(which_credit_card(371449635398431), CreditCard.AMEX)

    def test_MASTERCARD(self):
        self.assertEqual(which_credit_card(2221000000000009), CreditCard.MASTERCARD)
        self.assertEqual(which_credit_card(2223000048400011), CreditCard.MASTERCARD)
        self.assertEqual(which_credit_card(2223016768739313), CreditCard.MASTERCARD)
        self.assertEqual(which_credit_card(5555555555554444), CreditCard.MASTERCARD)
        self.assertEqual(which_credit_card(5105105105105100), CreditCard.MASTERCARD)
        self.assertEqual(which_credit_card(5555555555554444), CreditCard.MASTERCARD)

    def test_VISA(self):
        self.assertEqual(which_credit_card(4111111111111111), CreditCard.VISA)
        self.assertEqual(which_credit_card(4012888888881881), CreditCard.VISA)

    def test_INVALID(self):
        self.assertEqual(which_credit_card(1234567890), CreditCard.INVALID)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        _ = unittest.main(argv=sys.argv[:1])
    else:
        main()
