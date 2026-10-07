def get_numbers():
    data = input("Enter numbers with comma separator : ")
    return data

def prase_numbers(data):
    try :
        numbers = [int(x) for x in data.split(",")]
        return numbers
    except ValueError:
        return None
    
def display(result):
    if result is None:
        print("Enter numbers only")
    else :
        for i in result:
            print(i,end =" ")
        
data = get_numbers()
numbers = prase_numbers(data)
display(numbers)