MINIMUM_DRIVING_AGE = 16

age = int(input("What is your age? "))
message = "You are old enough to legally drive." if age >= MINIMUM_DRIVING_AGE else "You are not old enough to legally drive."

print(message)