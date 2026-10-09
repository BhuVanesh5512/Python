# def add(a,b):
#         return a + b
# def subtract(a,b):
#         return a - b

# if __name__ != "__main__":
#     print("This will print when imported also from calculate.py")

# if __name__ == "__main__":
#     print("Calculator module executed directly,this will print only when this file is executed")

def add(a,b):
        return a + b
    
print("Calculator loaded")
if __name__ == "__main__":
    print("Running calculator directly")
    print(add(10,20))