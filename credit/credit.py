import re
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


def validate_credit(credit_number: int) -> bool:
    return False


def main():
    """
    Todo:
    - Validate if it's a valid credit card
    - Identify which company it belongs to
    """
    while True:
        try:
            credit_number: int = int(input("Number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
        else:
            break

    if not validate_credit(credit_number):
        print(CreditCard.INVALID.name)
        sys.exit(1)

    verdict: CreditCard = which_credit_card(credit_number)
    print(verdict.name)


class TestCredit(unittest.TestCase):
    def test_AMEX(self):
        self.assertEqual(which_credit_card(378282246310005), CreditCard.AMEX)
        self.assertEqual(which_credit_card(371449635398431), CreditCard.AMEX)

    def test_MASTERCARD(self):
        self.assertEqual(which_credit_card(5555555555554444), CreditCard.MASTERCARD)
        self.assertEqual(which_credit_card(5105105105105100), CreditCard.MASTERCARD)

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
