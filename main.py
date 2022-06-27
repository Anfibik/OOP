class UserMain:
    """Класс, определяющий пользователей"""
    __OLD = 56
    __YOUNG = 18

    @classmethod
    def __validate_age(cls, arg):
        return cls.__YOUNG <= arg <= cls.__OLD

    def __init__(self, name_user="User", fund_company=0, nation="--", age=40):
        if self.__validate_age(age):
            self.__name_user = name_user
            self.__fund_company = fund_company
            self.__nation = nation
            self.__age = age
        else:
            raise ValueError(f"Возраст вне допустимого диапозона: {self.__YOUNG} - {self.__OLD}")

    def set_info_user(self, name_user, fund_company, nation, age):
        if self.__validate_age(age):
            self.__name_user = name_user
            self.__fund_company = fund_company
            self.__nation = nation
            self.__age = age
        else:
            raise ValueError(f"Возраст вне допустимого диапозона: {self.__YOUNG} - {self.__OLD}")

    def get_volue_user(self):
        return self.__name_user, self.__fund_company, self.__nation, self.__age

    def show_info_user(self):
        print(f"Имя: {self.__name_user}, {self.__age} лет, "
              f"национальность: {self.__nation}. Капитал: {self.__fund_company} грн")


user1 = UserMain()
user1.show_info_user()
user1.set_info_user("Андрей", 34, "Украинец", 40)
user1.show_info_user()
print(user1.get_volue_user())

print(user1.__dict__)
