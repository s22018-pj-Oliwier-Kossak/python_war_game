from colorama import Fore


class Major():
    """Class to create majors soldiers"""

    def __init__(self, money=0, dict=None):
        self.money = money
        self.dict = {
            "majors_level_1": 0,
            "majors_level_2": 0,
            "majors_level_3": 0,
            "majors_level_4": 0,
            "majors_level_5": 0
        }

    def display_all_majors(self):
        """The function which display all majors"""
        i = 1
        for x, y in self.dict.items():
            print(f"majors level {i}:", y)
            i += 1

    def display_strength_all_majors(self):
        """The function which display strength of all majors"""
        strength_all_majors = self.dict["majors_level_1"] * 1 * 4 + self.dict["majors_level_2"] * 2 * 4 + self.dict[
            "majors_level_3"] * 3 * 4 + self.dict["majors_level_4"] * 4 * 4 + self.dict["majors_level_5"] * 5 * 4
        return strength_all_majors

    def buy_majors_level_1(self):
        """The function allow to buy majors level 1"""
        while True:
            max_buy = self.money // 40
            print("Your money:", self.money)
            print("Max majors to buy:", max_buy)
            print("If want end buy majors enter 0")
            value_of_majors = int(input(("Enter amount of majors to buy: ")))
            print("value_of_majors", value_of_majors)
            if not isinstance(value_of_majors, int):
                print("incorrect type, money must be int type")
                print()
                continue

            if not 0 <= value_of_majors * 40 <= self.money:
                print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                print()
                continue

            if value_of_majors == 0:
                break
            else:
                self.money -= value_of_majors * 40
                self.dict["majors_level_1"] += value_of_majors
                break
            print()

    def training_level_1_majors(self):
        """The function allow to train majors level one"""
        print()

        if self.dict["majors_level_1"] == 0:
            print("You do not have majors to train")

        else:
            while True:
                max_majors_training = self.money // 4
                print("Your money:", self.money)
                print("Max amount of majors to training: %s , Cost of training all majors: %s" % (
                    max_majors_training * 4, max_majors_training * 4))
                print("If want end to training of majors enter 0")
                value_of_majors = int(input(("Enter amount of majors to training: ")))
                if not isinstance(value_of_majors, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_majors <= self.money // 4:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                if value_of_majors == 0:
                    break
                else:
                    self.money -= value_of_majors
                    self.dict["majors_level_1"] -= value_of_majors
                    self.dict["majors_level_2"] += value_of_majors
                break
                print()

    def training_level_2_majors(self):
        """The function allow to train majors level two"""
        print()
        if self.dict["majors_level_2"] == 0:
            print("You do not have majors to train")
        else:
            while True:
                max_majors_training = self.money // 4
                print("Your money:", self.money)
                print("Max amount of majors to training: %s , Cost of training all majors: %s" % (
                    max_majors_training * 4, max_majors_training * 4))
                print("If want end to training of majors enter 0")
                value_of_majors = int(input(("Enter amount of majors to training: ")))
                if not isinstance(value_of_majors, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_majors <= self.money // 4:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                elif value_of_majors == 0:
                    break
                else:
                    self.money -= value_of_majors
                    self.dict["majors_level_2"] -= value_of_majors
                    self.dict["majors_level_3"] += value_of_majors
                print()

    def training_level_3_majors(self):
        """The function allow to train majors level three"""
        print()
        if self.dict["majors_level_3"] == 0:
            print("You do not have majors to train")
        else:
            while True:
                max_majors_training = self.money // 4
                print("Your money:", self.money)
                print("Max amount of majors to training: %s , Cost of training all majors: %s" % (
                    max_majors_training * 4, max_majors_training * 4))
                print("If want end to training of majors enter 0")
                value_of_majors = int(input(("Enter amount of majors to training: ")))
                if not isinstance(value_of_majors, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_majors <= self.money // 4:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                elif value_of_majors == 0:
                    break
                else:
                    self.money -= value_of_majors
                    self.dict["majors_level_3"] -= value_of_majors
                    self.dict["majors_level_4"] += value_of_majors
                print()

    def training_level_4_majors(self):
        """The function allow to train majors level four"""
        print()
        if self.dict["majors_level_4"] == 0:
            print("You do not have majors to train")
        else:
            while True:
                max_majors_training = self.money // 4
                print("Your money:", self.money)
                print("Max amount of majors to training: %s , Cost of training all majors: %s" % (
                    max_majors_training * 4, max_majors_training * 4))
                print("If want end to training of majors enter 0")
                value_of_majors = int(input(("Enter amount of majors to training: ")))
                if not isinstance(value_of_majors, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_majors <= self.money // 4:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                elif value_of_majors == 0:
                    break
                else:
                    self.money -= value_of_majors
                    self.dict["majors_level_4"] -= value_of_majors
                    self.dict["majors_level_5"] += value_of_majors
                print()
