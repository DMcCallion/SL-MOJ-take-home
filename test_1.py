"""First stage of MOJ take home assessment"""
import re

VALID_ERRORTYPES = ["INFO", "TRACE", "WARNING"]


def separate_string(line: str) -> list:
    """Seperates a single line from the log file into a list. 
    The filter gets rid of empty strings that would be in the list if just using .split"""
    line_segments = list(filter(None, line.split(' ')))
    return line_segments


def is_log_line(line: str) -> bool | None:
    """Takes a log line and returns True if it is a valid log line and returns nothing
    if it is not.

    The length check is already enough to get challenge 1 to pass,
    because the failing lines are all too short. 
    But it's not a very good check, so I've got some actual checks below that
    """

    line_segments = separate_string(line)

    if len(line_segments) < 4:
        return None

    date_and_time = line_segments[0] + " " + line_segments[1]
    error_type = line_segments[2]
    message_beginning = line_segments[3]

    dt_search = re.search("../../.. ..:..:..", date_and_time)
    if not dt_search:
        return None

    if error_type not in VALID_ERRORTYPES:
        return None

    if message_beginning[:2] != ":.":
        return None

    return True


# [TODO]: step 2
# Update the get_dict function below so it converts a line of the logs into a
# dictionary with keys for "timestamp", "log_level", and "message". The valid log
# levels are `INFO`, `TRACE`, and `WARNING`. See lines 67 to 71 for how we expect the
# results to look.
def get_dict(line: str) -> dict:
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    line_segments = separate_string(line)
    timestamp = line_segments.pop(0) + " " + line_segments.pop(0)
    log_level = line_segments.pop(0)

    uncleaned_message = " ".join(line_segments)
    message = re.sub("\n", "", uncleaned_message)

    log_dict = {'timestamp': timestamp,
                'log_level': log_level,
                'message': message}

    return log_dict


# YOU DON'T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
