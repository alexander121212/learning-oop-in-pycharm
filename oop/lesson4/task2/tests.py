from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholders[0] != "_cookies":  # TODO: your condition here
        failed("Error, you can't find cookies that way")
    if placeholders[1] != "_Student__coffee":  # TODO: your condition here
        failed("Error, you can't find coffee that way")
    if placeholders[0] == "_cookies" and placeholders[1] == "_Student__coffee":
        passed("Congratulations!!! Now you know how to steal cookies and what is python encapsulation")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


