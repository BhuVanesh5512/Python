# def get_data():
#     return input("Enter score with comma: ")

# def parse_numbers(data):
#     try:
#         numbers = [int(x.strip()) for x in data.split(",")]
#         return numbers

#     except ValueError:
#         raise ValueError("invalid value, score need to in integer values")
    
# def save_scores(score_list,filename):
#     with open(filename,"w",encoding = "utf-8") as file:
#             file.writelines( str(line)+"\n" for line in score_list)
#             return "Scores saved successfully"
    
    

    
# def read_scores(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         lines = file.readlines()

#     scores = [int(line.strip()) for line in lines]

#     return scores

# # try:
# #     numbers = get_data()
# #     scores = parse_numbers(numbers)
# #     print(save_scores(scores,"file_demo.txt"))
# # except ValueError as error:
# #     print(error)

# try :
#     scores = read_scores("file_demo.txt")
#     print(scores)
# except FileNotFoundError :
#     print("file does not exists")
    
def get_data():
    return input("Enter score with comma: ")


def parse_numbers(data):
    try:
        numbers = [int(x.strip()) for x in data.split(",")]
        return numbers
    except ValueError:
        raise ValueError("Invalid value, scores need to be integers")


def save_scores(filename, score_list):
    if not score_list:
        raise ValueError("Scores cannot be empty")

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(str(score) + "\n" for score in score_list)

    return "Scores saved successfully"


def read_scores(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return [int(line.strip()) for line in lines]


try:
    data = get_data()
    scores = parse_numbers(data)

    print(save_scores("file_demo.txt", scores))

    loaded_scores = read_scores("file_demo.txt")
    print("Loaded scores:", loaded_scores)

except ValueError as error:
    print("ValueError:", error)
    
    
def save_scores(filename,scores):
    if not scores:
        raise ValueError ("scores should not be empty")
    with open(filename,"w",encoding="utf-8")  as file:
        file.writelines(str(score)+"\n" for score in scores)
        return "scores saved successfully!"

def read_scores(filename):
    with open(filename,"r",encoding="utf-8") as file:
        content = file.readlines()
        return [int(x.strip()) for x in content]
    
try : 
    scores = [50,70,100]
    print(save_scores("file_demo.txt",scores))
    scores = read_scores("file_demo.txt")
    print(f"given scores  are {scores}")
except FileNotFoundError:
    print("file does not exists")
except ValueError as error:
    print(f"Error : {error}")
    
    
    
'''| Operation | Meaning |
|---|---|
| `"r"` | read |
| `"w"` | write/overwrite |
| `"a"` | append |
| `"x"` | create exclusively |
| `read()` | entire remaining content as string |
| `readline()` | one line |
| `readlines()` | remaining lines as list |
| `write()` | write string |
| `writelines()` | write multiple strings, **no automatic `\n`** |
| `with open(...)` | automatic resource cleanup |'''