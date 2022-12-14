def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        # print("you cannot divide a? number")
        print(err)
    except TypeError as err:
        print("number must be int or floats")
    except:
        print("unexpected error")
   
# print(divide(10,0))
print(divide(10,'2'))