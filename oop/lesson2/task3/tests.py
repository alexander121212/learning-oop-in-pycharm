from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] != "__name__":  # TODO: your condition here
        failed("Error, read theory and try again")

    if placeholders[1] != "__module__":  # TODO: your condition here
        failed("Error, read theory and try again")

    if placeholders[2] != "__dict__":  # TODO: your condition here
        failed("Error, read theory and try again")

    if placeholders[3] != "__bases__":  # TODO: your condition here
        failed("Error, read theory and try again")

    if placeholders[4] != "__doc__":  # TODO: your condition here
        failed("Error, read theory and try again")

    if placeholders[0] == "__name__" and placeholders[1] == "__module__" and placeholders[2] == "__dict__"\
            and placeholders[3] == "__bases__" and placeholders[4] == "__doc__":
        passed("Congratulations!!! Now you now how to use special attribute of th classes")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


