principal_amount = int(input("What is the principal amount? "))
interest_rate = float(input("What is the rate? "))
number_of_years = int(input("What is the number of years? "))
compounds_per_year = int(input("What is the number of times the interest is compounded per year? "))

accumulated_sum = round(principal_amount * (1 + (interest_rate / 100.0)/compounds_per_year) ** (compounds_per_year * number_of_years), 2)

print("${} invested at {}% for {} years compounded {} times per year is ${}.".format(principal_amount, interest_rate, number_of_years, compounds_per_year, accumulated_sum))