class Corporal:
    def __init__(self, strength=1, experince=1, dict=None):
        self.strength = strength
        self.experince = experince
        self.dict = {
            "corporals_level_1": 0,
            "corporals_level_2": 0,
            "corporals_level_3": 0,
            "corporals_level_4": 0,
            "corporals_level_5": 0
        }



    def all_corporals_strength(self):
        self.strength = self.dict["corporals_level_5"] * 2 * 4 + self.dict[
            "corporals_level_3"] * 2 * 3 + self.dict["corporals_level_2"] * 2 * 2 + self.dict["corporals_level_1"]*2
        return self.strength

    def buy_corporals(self, amount):
        self.dict["corporals_level_1"] += amount

    def corporals_promotion_from_privates(self,amount):
        self.dict["corporals_level_1"] += amount

    def corporals_promotion_level_1(self,amount):
        self.dict["corporals_level_2"] += amount
        self.dict["corporals_level_1"] -= amount

    def corporals_promotion_level_2(self, amount):
        self.dict["corporals_level_3"] += amount
        self.dict["corporals_level_2"] -= amount

    def corporals_promotion_level_3(self, amount):
        self.dict["corporals_level_4"] += amount
        self.dict["corporals_level_3"] -= amount

    def corporals_promotion_level_4(self, amount):
        self.dict["corporals_level_5"] += amount
        self.dict["corporals_level_4"] -= amount

    def corporals_promotion_level_5(self, amount):
        self.dict["corporals_level_5"] -= amount

    def corporals_downgread(self):
        self.dict["corporals_level_1"] -= self.dict["corporals_level_2"]
        self.dict["corporals_level_2"] -= self.dict["corporals_level_3"]
        self.dict["corporals_level_3"] -= self.dict["corporals_level_4"]
        self.dict["corporals_level_4"] -= self.dict["corporals_level_5"]
        self.dict["corporals_level_5"] = 0

