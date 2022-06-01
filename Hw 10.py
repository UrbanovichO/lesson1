s = input("Input number:")
len(s)
kounter = 0
for i in s:
    a = int(s)%10
    if a == 2:
        kounter+=1
    s = int(s)//10
if(kounter == 1):
    print("Yes")
else:
    print("No")