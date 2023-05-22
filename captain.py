class Captain:
    def __init__(self, strength=1, experince=1, dict=None):
        self.strength = strength
        self.experince = experince
        self.dict = {
            "captains_level_1": 0,
            "captains_level_2": 0,
            "captains_level_3": 0,
            "captains_level_4": 0,
            "captains_level_5": 0
        }


    def all_captains_strength(self):
        self.strength = self.dict["captains_level_5"] * 3 * 5 + self.dict["captains_level_4"] * 3 * 4 + self.dict[
            "captains_level_3"] * 3 * 3 + self.dict["captains_level_2"] * 3 * 2 + self.dict["captains_level_1"]*3
        return self.strength

    def buy_captains(self, amount):
        self.dict["captains_level_1"] += amount

    def captains_promotion_from_corporals(self, amount):
        self.dict["captains_level_1"] += amount

    def captains_promotion_level_1(self, amount):
        self.dict["captains_level_2"] += amount
        self.dict["captains_level_1"] -= amount

    def captains_promotion_level_2(self, amount):
        self.dict["captains_level_3"] += amount
        self.dict["captains_level_2"] -= amount

    def captains_promotion_level_3(self, amount):
        self.dict["captains_level_4"] += amount
        self.dict["captains_level_3"] -= amount

    def captains_promotion_level_4(self, amount):
        self.dict["captains_level_5"] += amount
        self.dict["captains_level_4"] -= amount

    def captains_promotion_level_5(self, amount):
        self.dict["captains_level_5"] -= amount

    def captains_downgread(self):
        self.dict["captains_level_1"] -= self.dict["captains_level_2"]
        self.dict["captains_level_2"] -= self.dict["captains_level_3"]
        self.dict["captains_level_3"] -= self.dict["captains_level_4"]
        self.dict["captains_level_4"] -= self.dict["captains_level_5"]
        self.dict["captains_level_5"] = 0
