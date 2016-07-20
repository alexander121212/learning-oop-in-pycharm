from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] == "__new__" and placeholders[1] == "cls" and placeholders[2] == "cls" \
            and placeholders[3] == "super" and placeholders[4] == "Student" and placeholders[5] == "cls"\
            and placeholders[6] == "cls" and placeholders[7] == "__new__" and placeholders[8] == "cls"\
            and placeholders[9] == "return" and placeholders[10] == "cls" and placeholders[11] == "__init__"\
            and placeholders[12] == "self" and placeholders[13] == "self":  # TODO: your condition here
        passed("Congratulations!")
    else:
        failed("Error, try again!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


