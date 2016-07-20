from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholders[0] == "__call__" and placeholders[1] == "student":  # TODO: your condition here
        passed("Congratulations!!! Now you know how look like functor!")
    else:
        failed("Error! Read and try again!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


