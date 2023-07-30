from challenge_1 import is_log_line, get_dict

# tests for step 1


def test_good_line():
    assert is_log_line(
        "03/11/21 08:51:01 INFO    :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf") == True


def test_bad_date():
    assert is_log_line(
        "03/11 08:51:01 INFO    :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf") == None


def test_bad_time():
    assert is_log_line(
        "03/11/21 081 INFO    :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf") == None


def test_bad_error_type():
    assert is_log_line(
        "03/11/21 08:51:01 ERROR    :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf") == None


def test_no_message():
    assert is_log_line(
        "03/11/21 08:51:01 ERROR ") == None

# tests for step 2


def test_valid_str():
    assert get_dict(
        "03/11/21 08:51:01 INFO    :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf")\
        == {'timestamp': "03/11/21 08:51:01",
            'log_level': "INFO",
            'message': ":...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf"}


def test_newline_in_string():
    assert get_dict(
        "03/11/21 08:51:01 INFO    :...loca\nte_configFile: Specif\nied \nconfiguration file: /u/use\nr10/rsvpd1.conf")\
        == {'timestamp': "03/11/21 08:51:01",
            'log_level': "INFO",
            'message': ":...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf"}
