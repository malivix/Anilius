import string
import random

RANDOM_STRING_CHOICES = string.ascii_lowercase + string.digits
RANDOM_STRING_DIGITS_CHOICES = string.digits


def random_string(specific_len):
    return "".join(random.choice(RANDOM_STRING_CHOICES) for _ in range(specific_len))


def random_string_digits(specific_len):
    return "".join(
        random.choice(RANDOM_STRING_DIGITS_CHOICES) for _ in range(specific_len)
    )
