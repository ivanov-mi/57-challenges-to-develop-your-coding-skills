length_feet = int(input("What is the length of the room in feet? "))
width_feet = int(input("What is the width of the room in feet? "))

print("You entered dimensions of {} feet by {} feet.".format(length_feet, width_feet))

conversion_factor = 0.09290304
area_feet = length_feet * width_feet
area_metric = area_feet * conversion_factor

print("The area is\n{} square feet\n{:.3f} square meters".format(area_feet, area_metric))

