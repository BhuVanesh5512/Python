for i in range(1,11):
    print(i,end=" ")

print("\n")
print("="*20)   
for i in range(1,11):
    if(i%2==0):
        print(i,end=" ")

print("\n")
print("="*20)    
x=5
while x>=1:
    print(x,end=" ")
    x-=1
print("\nBlast off!")
    
print("\n")
print("="*20)
for i in range(1,101):
    if(i==37):
        break
    print(i,end=" ")

print("\n")
print("="*20)

i=1
while (i<=20):
    if(i%3 == 0):
        i=i+1
        continue
    print(i,end=" ")
    i+=1
    
print("\n")
print("="*20)
for i in range(2, 21, 2):
    print(i)