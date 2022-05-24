class MainClass:

    def get_local_number(self):
        return 14


class TestMainClass:

    def test_get_local_number(self):
        main_class = MainClass()
        assert 14 == main_class.get_local_number(), "Not Success"