class CustomError(Exception):
    pass

def risk():
    raise CustomError("You have tapped into a risky function")

try:
    risk()
except CustomError as e:
    print(str(e))