
# function decorators - függvény dekorátorok - 2. rész

def validate_email(func):
    def wrapper(password, email):
        if "@" not in email:
            return "Not valid email!"
        return func(password, email)
    return wrapper

def validate_password(func):
    def wrapper(password, email):
        if len(password) < 6:
            return "Week password, at least 6 characters!"
        return func(password, email)
    return wrapper

@validate_email
@validate_password
def form(password, email):
    return "Your password is strong and you have a valid email!"

print(form("1234", "atti"))
print(form("123456", "atti@mail.hu"))