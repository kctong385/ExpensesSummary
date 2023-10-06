import re

def check_date_format(text):
    if re.search(r"^[1|2]\d{3}-(0[1-9]|11|12)-(0[1-9]|[1-2]\d|30|31)$", text):
        return True
    else:
        return False


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False