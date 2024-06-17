import re


def check_password_strength(password):
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    if not re.match(pattern, password):
        return False
    return True


password_not_strong_enough_message = (
    "Password must contain at least 8 characters, at least 1 digit and at least 1 "
    "letter"
)
