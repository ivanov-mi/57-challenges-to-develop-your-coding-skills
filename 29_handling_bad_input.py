
def get_rate_of_return():
    while True:
        try:
            rate_of_return = float(input('What is the rate of return? '))
            if rate_of_return > 0:
                return rate_of_return

            print('Sorry. Rate return should be larger than zero.')
        except ValueError:
            print('Sorry. That\'s not a valid input.')

def calculate_years(rate_of_return):
    return 72 / rate_of_return


rate_of_return = get_rate_of_return()
years = calculate_years(rate_of_return)
print(f'It will take {years} to double your initial investment.')