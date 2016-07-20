from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] != "pass_one_subject":  # TODO: your condition here
        failed("Error, name of method is wrong")
    if placeholders[1] != "self.subject_count":  # TODO: your condition here
        failed("Error, name of attribute is wrong")
    else:
        passed("Congratulations!!! Now you know how describe and use class methods")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


