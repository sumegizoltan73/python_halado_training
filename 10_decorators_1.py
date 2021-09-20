
# function decorators - függvény dekorátorok - 1. rész

def validate_div(func):
    def wrapper(value1, value2):
        if value2 == 0:
            return "Can not divide by zero!"
        return func(value1, value2)
    return wrapper

@validate_div
def divide(value1, value2):
    return value1 / value2

print(divide(4, 0))
print(divide(7, 9))
print(divide(25, 5))
print(divide(36, 0))

def validate_form(func):
    def wrapper(password, email):
        if len(password) < 6:
            return "Week password, at least 6 characters!"
        if "@" not in email:
            return "Not valid email!"
        return func(password, email)
    return wrapper

@validate_form
def form(password, email):
    return "Your password is strong and you have a valid email!"

print(form("1234", "atti"))
print(form("123456", "atti@mail.hu"))

