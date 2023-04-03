import re
def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dictionary indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """
    
    errors = {
        'length_error' : len(password) < 8,
        'digit_error' : re.search(r"\d", password) is None,
        'uppercase_error' : re.search(r"[A-Z]", password) is None,
        'lowercase_error' : re.search(r"[a-z]", password) is None,
        'symbol_error' : re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None
    }

    # overall result
    password_ok = not any(errors.values())

    return {
        'password_ok' : password_ok,
        **errors
    }

password = input("Enter a password: ")
check_result = password_check(password)
if check_result['password_ok']:
    print("The password is good to go!")
else:
    print("The password does not meet the following criteria:")
    for error, has_error in check_result.items():
        if has_error and error != 'password_ok':
            print("- " + error.replace("_", " "))
import re
def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dictionary indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """
    
    errors = {
        'length_error' : len(password) < 8,
        'digit_error' : re.search(r"\d", password) is None,
        'uppercase_error' : re.search(r"[A-Z]", password) is None,
        'lowercase_error' : re.search(r"[a-z]", password) is None,
        'symbol_error' : re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None
    }

    # overall result
    password_ok = not any(errors.values())

    return {
        'password_ok' : password_ok,
        **errors
    }

password = input("Enter a password: ")
check_result = password_check(password)
if check_result['password_ok']:
    print("The password is good to go!")
else:
    print("The password does not meet the following criteria:")
    for error, has_error in check_result.items():
        if has_error and error != 'password_ok':
            print("- " + error.replace("_", " "))
