def read_file(filename):
    try :
        with open(filename,"r",encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise ValueError("File does not exist")
    
    #except FileNotFoundError:
    # raise FileNotFoundError(f"{filename} was not found")
    
try:
    content = read_file("file_demo.txt")
    print(content)
except ValueError as error:
    print("Error:", error)