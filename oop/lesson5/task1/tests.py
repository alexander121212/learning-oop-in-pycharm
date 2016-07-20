from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] != "__new__":  # TODO: your condition here
        failed("Error! method for creation instance is wrong!")
    if placeholders[1] != "hasattr":  # TODO: your condition here
        failed("Error! func for checking is wrong!")
    if placeholders[2] != "super":  # TODO: your condition here
        failed("Error! func for getting  parents obj is wrong!")
    if placeholders[3] != "__init__":  # TODO: your condition here
        failed("Error! method for initializing is wrong!")
    if placeholders[4] != "id" or placeholders[5] != "id":  # TODO: your condition here
        failed("Error! func for getting is wrong!")

    if placeholders[0] == "__new__" and placeholders[1] == "hasattr" and\
        placeholders[2] == "super" and placeholders[3] == "__init__" and placeholders[4] == placeholders[5] == "id":
        passed("Congratulations!!! Now you know how to create singleton!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


