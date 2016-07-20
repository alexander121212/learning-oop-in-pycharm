from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] == placeholders[1] == placeholders[3] == "student" and placeholders[2] == "pass_all_debts":  # TODO: your condition here
        passed("Congratulations!!! Now you can create objects of the class and use it methods")
    elif placeholders[0] != placeholders[1] != placeholders[3] != "student":
        failed("Error, name is wrong")
    elif placeholders[2] != "pass_all_debts":
        failed("method is wrong")



if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


