from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholders[0] != "del":  # TODO: your condition here
        failed("Error! Try more efficient")
    if placeholders[1] != "delattr":  # TODO: your condition here
        failed("Error! Try dynamic attribute deleting")
    if placeholders[0] == "del" and placeholders[1] == "delattr":
        passed("Congratulations!!! Now you know how to delete class attributes!!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


