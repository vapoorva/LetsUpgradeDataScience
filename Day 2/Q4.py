import math
def robot(n):
    l=[] #list having values
    x=0 # new position of x
    y=0 #new position of y
    for i in range (0,n):# STORE COMMAND VALUES IN LIST
        s=input()
        l.extend(s.split())

    for i in range(0,len(l)): #CHANGE CURRET position DEPENDING ON COMMAND
        if l[i].upper()=="UP":
            pos=int(l[i+1])
            y=y+pos
        if l[i].upper()=="DOWN":
            pos=int(l[i+1])
            y=y-pos
        if l[i].upper()=="RIGHT":
            pos=int(l[i+1])
            x=x+pos
        if l[i].upper()=="LEFT":
            pos=int(l[i+1])
            x=x-pos

    Location = math.sqrt(pow(x,2)+pow(y,2))
    print(int(Location))



n= int(input())
robot(n)
