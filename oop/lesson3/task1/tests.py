from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] != "def":  # TODO: your condition here
        failed("Error, reserved word is wrong")
    if placeholders[1] != "play_truant":  # TODO: your condition here
        failed("Error, name of method is wrong")
    if placeholders[2] != "self":  # TODO: your condition here
        failed("Error, first attribute is wrong")
    if placeholders[3] != "victory_cry":  # TODO: your condition here
        failed("Error, name of second attribute is wrong")
    if placeholders[4] != "victory_cry":  # TODO: your condition here
        failed("Error, name of second attribute is wrong")
    if placeholders[5] != "play_truant":  # TODO: your condition here
        failed("Error, name of method is wrong")
    else:
        passed("Congratulations!!! Now you know, how to create class methods!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


