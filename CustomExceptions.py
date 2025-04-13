# Python code​​​​​​‌‌​‌​​‌​​​‌​​‌​‌‌‌​‌​​​​​ below
def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise NonIntArgumentException()
        return func(*args)
    return wrapper


class NonIntArgumentException(Exception):
    def __init__(self, message="All arguments must be integers"):
        super().__init__(message)
