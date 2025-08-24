import string
import random as r
'''def punction(temp):
    l=string.punctuation
    a=[]
    b=[]
    count=0
    for i in l:
        a.append(i)
    while count<=4:
            pun=r.choice(l)
            temp.append(pun)
            b.append(pun)
            count+=1'''
def punction(temp):
    l="!@#$%^&*-_=+;:/?.>,<|"
    a=[]
    b=[]
    count=0
    for i in l:
        a.append(i)
    while count<=4:
            pun=r.choice(l)
            temp.append(pun)
            b.append(pun)
            count+=1
def alphabet(temp):
    l=string.ascii_letters
    a=[]
    b=[]
    count=1
    for i in l:
        a.append(i)
    while count<=4:
            pun=r.choice(l)
            temp.append(pun)
            b.append(pun)
            count+=1
def torandomnumber(temp):
    count=1
    while count<=4:
        a=r.randint(0,9)
        temp.append(a)
        count+=1
def generate(pas):
     count=1
     while count<9:
            pun=r.choice(temp)
            pas.append(pun)
            count+=1          
def display(pas):
    for i in pas:
        print(i,end="")
    print()
temp=[]
pas=[]
punction(temp)
torandomnumber(temp)
alphabet(temp)
generate(pas)
print("------Random Password Generated---")
display(pas)
while True:
    choice=int(input("Enter 1--> for more\n 2-- No:\n"))
    if choice==1:
        print("------Random Password Generated---")
        punction(temp)
        torandomnumber(temp)
        alphabet(temp)
        generate(pas)
        display(pas)
    else:
         break