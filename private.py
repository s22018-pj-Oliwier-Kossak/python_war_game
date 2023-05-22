class Private:
    def __init__(self, strength=1, experince=1,amount=0, dict=None):
        self.strength = strength
        self.experince = experince
        self.amount = amount
        self.dict = {
            "privates_level_1": 0,
            "privates_level_2": 0,
            "privates_level_3": 0,
            "privates_level_4": 0,
            "privates_level_5": 0
        }



    def all_privates_strength(self):
        self.strength = self.dict["privates_level_5"] * 5 + self.dict["privates_level_4"] * 4 + self.dict[
            "privates_level_3"] * 3 + self.dict["privates_level_2"] * 2 + self.dict["privates_level_1"]
        return self.strength

    def buy_privates(self, amount):
        self.dict["privates_level_1"] += amount

    def privates_promotion_level_1(self,amount):
        self.dict["privates_level_2"] += amount
        self.dict["privates_level_1"] -= amount

    def privates_promotion_level_2(self,amount):
        self.dict["privates_level_3"] += amount
        self.dict["privates_level_2"] -= amount

    def privates_promotion_level_3(self,amount):
        self.dict["privates_level_4"] += amount
        self.dict["privates_level_3"] -= amount

    def privates_promotion_level_4(self,amount):
        self.dict["privates_level_5"] += amount
        self.dict["privates_level_4"] -= amount

    def privates_promotion_level_5(self, amount):
        self.dict["privates_level_5"] -= amount

    def privates_downgread(self):
        self.dict["privates_level_1"] -= self.dict["privates_level_2"]
        self.dict["privates_level_2"] -= self.dict["privates_level_3"]
        self.dict["privates_level_3"] -= self.dict["privates_level_4"]
        self.dict["privates_level_4"] -= self.dict["privates_level_5"]
        self.dict["privates_level_5"] = 0




