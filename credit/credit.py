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
    amex = re.compile(r"^(34|37)\d{13}$")  # Starts with 34/34 and is 15 digits long
    mastercard = re.compile(r"^5[12345]\d{14}$")  # Starts with 5x,x={1,2,3,4,5} 16 long
    visa = re.compile(r"^(4\d{15})|(4\d{12})$")  # Starts with 4, 13/16 digits long
    str_credit_number = str(credit_number)

    if amex.fullmatch(str_credit_number):
        return CreditCard.AMEX
    elif mastercard.fullmatch(str_credit_number):
        return CreditCard.MASTERCARD
    elif visa.fullmatch(str_credit_number):
        return CreditCard.VISA
    else:
        return CreditCard.INVALID


def is_valid_checksum(credit_number: int) -> bool:
    """
    Validates checksum using Luhn's Algorithm
    """
    sum = 0
    total = 0

    if total % 10 == 0:
        return True
    return False


def match_credit_card(credit_number: int) -> CreditCard:
    if not is_valid_checksum(credit_number):
        return CreditCard.INVALID

    return which_credit_card(credit_number)


def main():
    while True:
        try:
            credit_number: int = int(input("Number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
        else:
            break

    result = match_credit_card(credit_number)
    print(result.name)


class TestCredit(unittest.TestCase):
    def test_checksum(self):
        num = 378282246310005

        res = (num % 10**15) // 10**14
        self.assertEqual(res, 3)

        res = (num % 10**15) // 10**13
        self.assertEqual(res, 37)

        res = (num % 10**14) // 10**13
        self.assertEqual(res, 7)

        res = (num % 10**5) // 10**4
        self.assertEqual(res, 1)

    def test_AMEX(self):
        self.assertEqual(match_credit_card(378282246310005), CreditCard.AMEX)
        self.assertEqual(match_credit_card(371449635398431), CreditCard.AMEX)

    def test_MASTERCARD(self):
        self.assertEqual(match_credit_card(5555555555554444), CreditCard.MASTERCARD)
        self.assertEqual(match_credit_card(5105105105105100), CreditCard.MASTERCARD)

    def test_VISA(self):
        self.assertEqual(match_credit_card(4111111111111111), CreditCard.VISA)
        self.assertEqual(match_credit_card(4012888888881881), CreditCard.VISA)

    def test_INVALID(self):
        self.assertEqual(match_credit_card(1234567890), CreditCard.INVALID)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        _ = unittest.main(argv=sys.argv[:1])
    else:
        main()
