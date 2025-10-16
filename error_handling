def safe_divide(numerator,denominator):
    try:
        result=numerator/denominator
        print(f"The result of {numerator}/{denominator} is:{result}")
    except ZeroDivisionError:
        print("Error:Cannot divide by zero")
    except TypeError:
        print("Error:Invalid input")
    except Exception as e:
        print(f"An unexpected error occured:{e}")
safe_divide(15,5)
safe_divide(15,0)
safe_divide(15,"zz")

