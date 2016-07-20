from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] != "__init__" or placeholders[1] != "__class__" or placeholders[2] != "__dict__" \
            or placeholders[3] != "__hash__" or placeholders[4] != "__delattr__" or placeholders[5] != "__setattr__":  # TODO: your condition here
        failed("Error, see theory and try again!")
    if placeholders[0] == "__init__" and placeholders[1] == "__class__" and placeholders[2] == "__dict__" \
            and placeholders[3] == "__hash__" and placeholders[4] == "__delattr__" and placeholders[5] == "__setattr__":
        passed('Congratulations!!! Now you are know how to use some special attributes of instances!')


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


