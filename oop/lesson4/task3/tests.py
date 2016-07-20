from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] != "Student":  # TODO: your condition here
        failed("Error, your base class is wrong!")
    if placeholders[1] != "sleep_sweety":  # TODO: your condition here
        failed("Error, your new method name is wrong!")
    if placeholders[2] != "super":  # TODO: your condition here
        failed("Error, your method for getting base class is wrong!")
    if placeholders[3] != "StudentOfRadik":  # TODO: your condition here
        failed("Error, your name of this class is wrong!")
    if placeholders[4] != "play_truant":  # TODO: your condition here
        failed("Error, your override method is wrong!")
    if placeholders[0] == "Student" and placeholders[1] == "sleep_sweety" and \
        placeholders[2] == "super" and placeholders[3] == "StudentOfRadik" and placeholders[4] == "play_truant":
        passed("Congratulations!!! Now you know how inheritance works, how override method and use base class "
               "members in child")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


