PIECES_PER_PIZZA = 8

people = int(input("How many people? "))
pizzas = int(input("How many pizzas do you have? "))

print("{} people with {} pizzas".format(people, pizzas))

total_number_of_pieces = pizzas * PIECES_PER_PIZZA
pieces_per_person = total_number_of_pieces // people
leftover_pieces = total_number_of_pieces % people

print("Each person gets {} pieces of pizza.\nThere are {} leftover pieces.".format(pieces_per_person, leftover_pieces))