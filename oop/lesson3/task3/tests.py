from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] != "@classmethod":  # TODO: your condition here
        failed("Error, use decorator for class method")

    if placeholders[1] != "@staticmethod":  # TODO: your condition here
        failed("Error, use decorator for static method")
    if placeholders[0] == "@classmethod" and placeholders[1] == "@staticmethod":
        passed("Congratulations!!! Now you know how to define static- and classmethods")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


