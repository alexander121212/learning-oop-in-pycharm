from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholders[0] != "__slots__":  # TODO: your condition here
        failed("Error! using correct definition of slots!")
    if placeholders[1] != "debts_count" and placeholders[1] != "desire_to_learn":
        failed("Error! Undefined attr!")
    if placeholders[2] != "debts_count" and placeholders[2] != "desire_to_learn":
        failed("Error! Undefined attr!")
    if placeholders[0] == "__slots__" and (placeholders[1] == 'debts_count'
                                                   and placeholders[2] == 'desire_to_learn' or placeholders[2] == 'debts_count'
                                                   and placeholders[1] == 'desire_to_learn'):
        passed("Congratulations!!! Now you know how to use slots")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


