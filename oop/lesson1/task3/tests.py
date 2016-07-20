from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] != "debts_count":  # TODO: your condition here
        failed("Error, name of attributes is wrong!!! Try again or see hint")
        print(placeholders[0])
    if placeholders[1] != "0":  # TODO: your condition here
        failed("Error, we are good and clever students. Debts are evil!")
        print(placeholders[1])
    if placeholders[2] != placeholders[0]:  # TODO: your condition here
        failed("Error, check the current class attributes")
        print(placeholders[2])
    if placeholders[0] == "debts_count" and placeholders[1] == "0" and placeholders[2] == placeholders[0]:
        passed("Congratulations!!! Now you know how to use and check attributes!")



if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


