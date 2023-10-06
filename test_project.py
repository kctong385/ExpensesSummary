from project import check_date_format, isfloat, isint


def test_check_date_format():
    assert check_date_format("2023-01-01") == True
    assert check_date_format("2023-12-31") == True
    assert check_date_format("2023-00-01") == False
    assert check_date_format("2023-13-01") == False
    assert check_date_format("2023-01-00") == False
    assert check_date_format("2023-01-32") == False
    assert check_date_format("3023-01-01") == False
    assert check_date_format("0023-01-01") == False
    assert check_date_format("20023-01-01") == False
    assert check_date_format("2023-1-01") == False
    assert check_date_format("2023-01-1") == False


def test_isfloat():
    assert isfloat("1.1") == True
    assert isfloat("99.99") == True
    assert isfloat("1000.00") == True
    assert isfloat("1,000.00") == False
    assert isfloat("1.1.1") == False
    assert isfloat("cat") == False


def test_isint():
    assert isint("0") == True
    assert isint("9") == True
    assert isint("2023") == True
    assert isint("1.1") == False
    assert isint("cat") == False
    assert isint("1,000") == False
