from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] == "student" and placeholders[1] == "Student":  # TODO: your condition here
        passed("Concratulations!!! Now you know difference between bound method, unbound method and function!")
    else:
        failed("Error, please try again!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


