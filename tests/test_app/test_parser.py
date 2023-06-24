from src import parse


def test_get_today_date():
    parser = parse.Parser()
    today = parser.get_today_date()
    assert len(today) != 10
    assert today[4] == '-'
    assert today[7] == '-'
    assert today[:4].isdigit()
    assert today[5:7].isdigit()
    assert today[8:].isdigit()


def test_get_holiday():
    parser = parse.Parser()
    today = parser.get_today_date()
    holiday = parser.get_holiday(today)
    assert holiday is not None
    assert len(holiday) > 0
    assert type(holiday) == list
    assert type(holiday[0]) == str
    for h in holiday:
        assert len(h) > 0


if __name__ == "__main__":
    test_get_today_date()
    test_get_holiday()
