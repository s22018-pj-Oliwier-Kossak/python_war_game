class Private():
    """Class to create privates soldiers"""

    def __init__(self, money=0, dict=None):
        self.money = money
        self.dict = {
            "privates_level_1": 0,
            "privates_level_2": 0,
            "privates_level_3": 0,
            "privates_level_4": 0,
            "privates_level_5": 0
        }

    def display_all_units(self):
        """The function which display all privates"""
        i = 1
        for x, y in self.dict.items():
            print(f"Privates level {i}:", y)
            i += 1

    def display_strength_all_units(self):
        """The function which display strength of all privates"""
        strength_all_privates = self.dict["privates_level_1"] * 1 + self.dict["privates_level_2"] * 2 + self.dict[
            "privates_level_3"] * 3 + self.dict["privates_level_4"] * 4 + self.dict["privates_level_5"] * 5
        return strength_all_privates

    def buy_units_level_1(self):
        """The function allow to buy privates level 1"""
        while True:
            max_buy = self.money // 10
            print("Your money:", self.money)
            print("Max privates to buy:", max_buy)
            print("If want end buy privates enter 0")
            value_of_privates = int(input(("Enter amount of privates to buy: ")))
            if not isinstance(value_of_privates, int):
                print("incorrect type, money must be int type")
                print()
                continue

            if not 0 <= value_of_privates * 10 <= self.money:
                print("not enough money or negative value")
                print()
                continue


            elif value_of_privates == 0:
                break
            else:
                self.money -= value_of_privates * 10
                self.dict["privates_level_1"] += value_of_privates
            print()

    def training_level_1_units(self):
        print()
        """The function allow to train units level one"""

        if self.dict["privates_level_1"] == 0:
            print("You do not have units to train")

        else:
            while True:
                max_units_training = self.money
                print("Your money:", self.money)
                print("Max amount of privates to training: %s , Cost of training all privates: %s" % (
                max_units_training, max_units_training))
                print("If want end to training of privates enter 0")
                value_of_privates = int(input(("Enter amount of privates to training: ")))
                if not isinstance(value_of_privates, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_privates <= self.money:
                    print("not enough money or negative value")
                    print()
                    continue
                elif value_of_privates == 0:
                    break
                else:
                    self.money -= value_of_privates
                    self.dict["privates_level_1"] -= value_of_privates
                    self.dict["privates_level_2"] += value_of_privates
                print()

    def training_level_2_units(self):
        """The function allow to train units level two"""
        print()
        if self.dict["privates_level_2"] == 0:
            print("You do not have units to train")
        else:
            while True:
                max_units_training = self.money
                print("Your money:", self.money)
                print("Max amount of privates to training: %s , Cost of training all privates: %s" % (
                    max_units_training, max_units_training))
                print("If want end to training of privates enter 0")
                value_of_privates = int(input(("Enter amount of privates to training: ")))
                if not isinstance(value_of_privates, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_privates <= self.money:
                    print("not enough money or negative value")
                    print()
                    continue
                elif value_of_privates == 0:
                    break
                else:
                    self.money -= value_of_privates
                    self.dict["privates_level_2"] -= value_of_privates
                    self.dict["privates_level_3"] += value_of_privates
                print()

    def training_level_3_units(self):
        """The function allow to train units level three"""
        print()
        if self.dict["privates_level_3"] == 0:
            print("You do not have units to train")
        else:
            while True:
                max_units_training = self.money
                print("Your money:", self.money)
                print("Max amount of privates to training: %s , Cost of training all privates: %s" % (
                    max_units_training, max_units_training))
                print("If want end to training of privates enter 0")
                value_of_privates = int(input(("Enter amount of privates to training: ")))
                if not isinstance(value_of_privates, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_privates <= self.money:
                    print("not enough money or negative value")
                    print()
                    continue
                elif value_of_privates == 0:
                    break
                else:
                    self.money -= value_of_privates
                    self.dict["privates_level_3"] -= value_of_privates
                    self.dict["privates_level_4"] += value_of_privates
                print()

    def training_level_4_units(self):
        """The function allow to train units level four"""
        print()
        if self.dict["privates_level_4"] == 0:
            print("You do not have units to train")
        else:
            while True:
                max_units_training = self.money
                print("Your money:", self.money)
                print("Max amount of privates to training: %s , Cost of training all privates: %s" % (
                    max_units_training, max_units_training))
                print("If want end to training of privates enter 0")
                value_of_privates = int(input(("Enter amount of privates to training: ")))
                if not isinstance(value_of_privates, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_privates <= self.money:
                    print("not enough money or negative value")
                    print()
                    continue
                elif value_of_privates == 0:
                    break
                else:
                    self.money -= value_of_privates
                    self.dict["privates_level_4"] -= value_of_privates
                    self.dict["privates_level_5"] += value_of_privates
                print()