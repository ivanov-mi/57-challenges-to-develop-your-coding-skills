import re

def validate_name(name, type_of_name):
    if not name:
        return f"The {type_of_name} name must be filled in."
    elif len(name) < 2:
        return f'"{name}" is not a valid {type_of_name} name. It is too short.'
    else:
        return ''

def validate_zip_code(zip):
    if zip.isnumeric():
        return ''
    else:
        return 'The ZIP code must be numeric.'

def validate_employee_id(employee_id):
    regex = '^[A-Za-z]{2}-[0-9]{3,4}'
    if re.match(regex, employee_id):
        return ''
    else:
        return f'{employee_id} is not a valid ID.'

def validate_input(first_name, last_name, zip_code, employee_id):
    results = [validate_name(first_name, "first"), validate_name(last_name, "second"), validate_zip_code(zip_code), validate_employee_id(employee_id)]
    validation_errors = list(filter(None, results))

    return 'There were no errors found.' if len(validation_errors) == 0 else '\n'.join(validation_errors)


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
zip_code = input('Enter your zip code: ')
employee_id = input('Enter your employee id: ')
print(validate_input(first_name, last_name, zip_code, employee_id))