from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] != "FridgeStorage":  # TODO: your condition here
        failed("Error! Name of descriptor is wrong!")

    if placeholders[1] != "__slots__":  # TODO: your condition here
        failed("Error! Slots definition is wrong!")

    if placeholders[2] != "__set__":  # TODO: your condition here
        failed("Error! Set definition is wrong!")

    if placeholders[3] != "__get__":
        failed("Error! Get definition is wrong!")

    if placeholders[4] != "FridgeStorage":
        failed("Error! Name of descriptor is wrong!")
    if placeholders[0] ==  placeholders[4] == "FridgeStorage" and placeholders[1] == "__slots__" and \
            placeholders[2] == "__set__" and placeholders[3] == "__get__":
        passed("Congratulations!!! Now you know how to create descriptor!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


