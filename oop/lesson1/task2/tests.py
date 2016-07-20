from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if len(placeholders[0]) > 1 and placeholders[0].isalpha()\
            and placeholders[1] == ".__doc__":  # TODO: your condition here
        passed("Congratulations!!! Now you know how to use docstrings")
    else:
        failed("Error, try again")
        print(placeholders[0], type(placeholders[0]), placeholders[1])


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


