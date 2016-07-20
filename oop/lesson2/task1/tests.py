from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] == placeholders[1] == placeholders[2] == "free_time":  # TODO: your condition here
        passed("Congratulations!!! You are good experimenter")
    else:
        failed("Error in name of attribute, try again")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


