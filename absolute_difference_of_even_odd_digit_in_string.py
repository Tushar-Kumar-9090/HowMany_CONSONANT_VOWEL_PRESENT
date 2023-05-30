
## WAP to print absolute difference of a even and odd digits in a given string???

s=input("Enter A String: ")
se=0
so=0
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            se+=int(i)
        else:
            so+=int(i)
if se>so:
    print(se-so)
else:
    print(so-se)
