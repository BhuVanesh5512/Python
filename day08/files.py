# with open("file_demo_environment_output.txt","r",encoding="utf-8") as file:
#     content = file.readline()
#     content2 = file.readline()
#     # content3 = file.read()
#     # content4 = file.readlines()
#     # print(repr(content))
#     file.seek(0)
#     content5 = file.readline()
#     file.seek(10)
#     content6 = file.readline()
#     print(content2)
#     print(repr(content5))
#     print(repr(content6))
#     '''AI Engineer Environment check

# '==============================\n'
# '====================\n' ''' #output before writes


with open("file_demo.txt","w",encoding="utf-8") as file:
    file.write("python\n")
    file.write("java\n")
    
# with open("file_demo.txt","r",encoding="utf-8") as file:
#     content = file.readline()
#     content2 = file.readline()
#     print(content)
#     print(content2)
    
lines = ["python\n","java","oracle"]
with open("file_demo.txt","w",encoding="utf-8") as file:
    file.writelines(lines)
    
 
with open("file_demo.txt","r",encoding="utf-8") as file:
    content = file.readlines()
    content2 = file.readline()
    print(content)
    


