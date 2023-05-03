from colorama import Fore


class Private():
    """Class to create captains soldiers"""

    def __init__(self, money=0, dict=None):
        self.money = money
        self.dict = {
            "captains_level_1": 0,
            "captains_level_2": 0,
            "captains_level_3": 0,
            "captains_level_4": 0,
            "captains_level_5": 0
        }

    def display_all_captains(self):
        """The function which display all captains"""
        i = 1
        for x, y in self.dict.items():
            print(f"captains level {i}:", y)
            i += 1

    def display_strength_all_captains(self):
        """The function which display strength of all captains"""
        strength_all_captains = self.dict["captains_level_1"] * 1*3 + self.dict["captains_level_2"] * 2*3 + self.dict[
            "captains_level_3"] * 3*3 + self.dict["captains_level_4"] * 4*3 + self.dict["captains_level_5"] * 5*3
        return strength_all_captains

    def buy_captains_level_1(self):
        """The function allow to buy captains level 1"""
        while True:
            max_buy = self.money // 30
            print("Your money:", self.money)
            print("Max captains to buy:", max_buy)
            print("If want end buy captains enter 0")
            value_of_captains = int(input(("Enter amount of captains to buy: ")))
            print("value_of_captains", value_of_captains)
            if not isinstance(value_of_captains, int):
                print("incorrect type, money must be int type")
                print()
                continue

            if not 0 <= value_of_captains * 30 <= self.money:
                print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                print()
                continue

            if value_of_captains == 0:
                break
            else:
                self.money -= value_of_captains * 30
                self.dict["captains_level_1"] += value_of_captains
                break
            print()

    def training_level_1_captains(self):
        """The function allow to train captains level one"""
        print()

        if self.dict["captains_level_1"] == 0:
            print("You do not have captains to train")

        else:
            while True:
                max_captains_training = self.money//3
                print("Your money:", self.money)
                print("Max amount of captains to training: %s , Cost of training all captains: %s" % (
                    max_captains_training *3, max_captains_training*3))
                print("If want end to training of captains enter 0")
                value_of_captains = int(input(("Enter amount of captains to training: ")))
                if not isinstance(value_of_captains, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_captains <= self.money//3:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                if value_of_captains == 0:
                    break
                else:
                    self.money -= value_of_captains
                    self.dict["captains_level_1"] -= value_of_captains
                    self.dict["captains_level_2"] += value_of_captains
                break
                print()

    def training_level_2_captains(self):
        """The function allow to train captains level two"""
        print()
        if self.dict["captains_level_2"] == 0:
            print("You do not have captains to train")
        else:
            while True:
                max_captains_training = self.money//3
                print("Your money:", self.money)
                print("Max amount of captains to training: %s , Cost of training all captains: %s" % (
                    max_captains_training*3, max_captains_training*3))
                print("If want end to training of captains enter 0")
                value_of_captains = int(input(("Enter amount of captains to training: ")))
                if not isinstance(value_of_captains, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_captains <= self.money//3:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                elif value_of_captains == 0:
                    break
                else:
                    self.money -= value_of_captains
                    self.dict["captains_level_2"] -= value_of_captains
                    self.dict["captains_level_3"] += value_of_captains
                print()

    def training_level_3_captains(self):
        """The function allow to train captains level three"""
        print()
        if self.dict["captains_level_3"] == 0:
            print("You do not have captains to train")
        else:
            while True:
                max_captains_training = self.money//3
                print("Your money:", self.money)
                print("Max amount of captains to training: %s , Cost of training all captains: %s" % (
                    max_captains_training * 3, max_captains_training*3))
                print("If want end to training of captains enter 0")
                value_of_captains = int(input(("Enter amount of captains to training: ")))
                if not isinstance(value_of_captains, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_captains <= self.money //3:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                elif value_of_captains == 0:
                    break
                else:
                    self.money -= value_of_captains
                    self.dict["captains_level_3"] -= value_of_captains
                    self.dict["captains_level_4"] += value_of_captains
                print()

    def training_level_4_captains(self):
        """The function allow to train captains level four"""
        print()
        if self.dict["captains_level_4"] == 0:
            print("You do not have captains to train")
        else:
            while True:
                max_captains_training = self.money //3
                print("Your money:", self.money)
                print("Max amount of captains to training: %s , Cost of training all captains: %s" % (
                    max_captains_training *3, max_captains_training *3))
                print("If want end to training of captains enter 0")
                value_of_captains = int(input(("Enter amount of captains to training: ")))
                if not isinstance(value_of_captains, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_captains <= self.money //3:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                elif value_of_captains == 0:
                    break
                else:
                    self.money -= value_of_captains
                    self.dict["captains_level_4"] -= value_of_captains
                    self.dict["captains_level_5"] += value_of_captains
                print()
