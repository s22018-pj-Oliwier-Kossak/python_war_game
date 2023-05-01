from private import Private

mon = 1000

private2 = Private(mon)

private2.display_all_units()
print(private2.display_strength_all_units())
private2.buy_units_level_1()
private2.display_all_units()
private2.training_level_1_units()
private2.display_all_units()