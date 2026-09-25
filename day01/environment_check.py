import sys
import platform

print("="*30)
print("AI Engineer Environment check")
print("="*30)

name = "P Bhuvanesh Chowdary"
training_goal = "AI Engineer"

print(f'Name : {name}')
print(f"Training Goal: {training_goal}")
print(f"Python Version : {sys.version}")
print(f"Operating System using : {platform.system()}")
print(f"Machine : {platform.machine()}")
print(f"Machine Architecture : {platform.architecture()[0]} ")
print("Status : Ready")
print("two imports your seeing are modules in python ,this are libraries, sys for python information,platform for machine information")


print("="*30)
print("Environment Check completed!")
