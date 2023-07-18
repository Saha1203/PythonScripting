# print("I'm good " +str(50) + " what about you")
calculation_to_units = 24
name_of_units = "hours"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days*calculation_to_units} {name_of_units}")
    print(custom_message)


def scope_check():
    print(name_of_units)
    

days_to_units(35, "everything looks good")
days_to_units(70, "not good")     
# days_to_units(96, "hey everyone") 


# print(f"60 days are {60* calculation_to_units} {name_of_units}")
# print(f"35 days are {35* calculation_to_units} {name_of_units}")
# print(f"96 days are {96* calculation_to_units} {name_of_units}")

