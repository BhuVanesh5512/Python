# import calculator as calc

# try :
#     addition_value = calc.add(25,15)
#     subtract_value = calc.subtract(25,15)
#     # addition_value2 = calc.add("25",15) 
#     print(addition_value)
#     print(subtract_value)
# except ValueError as error:
#     print(error)
# except TypeError:
#         raise TypeError("Invalid input")

import calculator as calc
result = calc.add(3,4)
print(f"Addition of 3,4 gives : {result} ")