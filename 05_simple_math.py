first_number_string = input("What is the first number? ")
second_number_string = input("What is the second number? ")

first_number = int(first_number_string)
second_number = int(second_number_string)

addition = "{} + {} = {}".format(first_number, second_number, (first_number + second_number))
subtraction = "{} - {} = {}".format(first_number, second_number, (first_number - second_number))
multiplication = "{} * {} = {}".format(first_number, second_number, (first_number * second_number))
division = "{} / {} = {}".format(first_number, second_number, (first_number // second_number))

print("{}\n{}\n{}\n{}".format(addition, subtraction, multiplication, division))