amount = round(float(input("What is the order amount? ")), 2)
state = input("What is the state? ")

tax = 0.0
result = ""

if state == "WI":
    tax = round((amount * 0.055), 2)
    result = "The subtotal is ${:.2f}.\nThe tax is ${:.2f}.\n".format(amount, tax)

total = amount + tax
result += "The total is ${:.2f}.".format(total)

print(result)
