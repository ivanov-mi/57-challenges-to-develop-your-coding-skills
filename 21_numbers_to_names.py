month_number = int(input("Please enter the number of the month: "))

def number_to_string(month_number):
    match month_number:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "Octomber"
        case 11:
            return "November"
        case 12:
            return "December"
        case default:
            return "Not a month"

print("The name of the month is {0}.".format(number_to_string(month_number)))
