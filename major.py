class Major:
    def __init__(self, strength=1, experince=1, dict=None):
        self.strength = strength
        self.experince = experince
        self.dict = {
            "majors_level_1": 0,
            "majors_level_2": 0,
            "majors_level_3": 0,
            "majors_level_4": 0,
            "majors_level_5": 0
        }


    def all_majors_strength(self):
        self.strength = self.dict["majors_level_5"] * 4 * 5 + self.dict["majors_level_4"] * 4 * 4 + self.dict[
            "majors_level_3"] * 4 * 3 + self.dict["majors_level_2"] * 4 * 2 + self.dict["majors_level_1"]*4
        return self.strength

    def buy_majors(self, amount):
        self.dict["majors_level_1"] += amount

    def majors_promotion_from_captains(self, amount):
        self.dict["majors_level_1"] += amount

    def majors_promotion_level_1(self, amount):
        self.dict["majors_level_2"] += amount
        self.dict["majors_level_1"] -= amount

    def majors_promotion_level_2(self, amount):
        self.dict["majors_level_3"] += amount
        self.dict["majors_level_2"] -= amount

    def majors_promotion_level_3(self, amount):
        self.dict["majors_level_4"] += amount
        self.dict["majors_level_3"] -= amount

    def majors_promotion_level_4(self, amount):
        self.dict["majors_level_5"] += amount
        self.dict["majors_level_4"] -= amount

    def majors_downgread(self):
        self.dict["majors_level_1"] -= self.dict["majors_level_2"]
        self.dict["majors_level_2"] -= self.dict["majors_level_3"]
        self.dict["majors_level_3"] -= self.dict["majors_level_4"]
        self.dict["majors_level_4"] -= self.dict["majors_level_5"]
        self.dict["majors_level_5"] = 0


