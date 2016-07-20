from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    if placeholders[0] != "Student(False)":  # TODO: your condition here
        failed("Student1 does not want to learn")
    if placeholders[1] != "Student(True)" and placeholders[1] != "Student()":  # TODO: your condition here
        failed("student2 want to learn")
    if placeholders[0] == "Student(False)" and (placeholders[1] == "Student(True)" or placeholders[1] == "Student()"):
        passed("Congratulations!!! Now you are know how to use class constructor!")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


