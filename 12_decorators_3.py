
# function decorators - függvény dekorátorok - 3. rész

import time

def main_decorator(state):
    def validate_form(func):
        def wrapper(password, email):
            print(state)
            time.sleep(3)
            if len(password) < 6:
                return "Week password, at least 6 characters!"
            if "@" not in email:
                return "Not valid email!"
            return func(password, email)
        return wrapper
    return validate_form

@main_decorator("validating...")
def form(password, email):
    return "Your password is strong and you have a valid email!"

print(form("123456", "atti"))
print(form("1234", "atti@mail.hu"))
print(form("123456", "atti@mail.hu"))