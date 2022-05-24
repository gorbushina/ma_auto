class MainClass:
    __class_number = 20


    def get_local_number(self):
        return 14

    def get_class_number(self):
        return self.__class_number


class TestMainClass:
    main_class = MainClass()

    def test_get_local_number(self):
        assert 14 == self.main_class.get_local_number(), "Not Success"

    def test_get_class_number(self):
        assert self.main_class.get_class_number() > 45, "Not Success"