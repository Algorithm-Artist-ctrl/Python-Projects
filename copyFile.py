def towrtite():
    f=open(name,"w")
    f.write(w)
    f.close()
def toappend():
    f=open(path,"a")
    f.write(more)
    f.close()
def read():
    f=open(path,"r")
    print(f.read())
    f.close()
def copy():
    f=open(path,"r+")
    file=f.read()
    newfile=open(name,"w")
    newfile.write(file)
    f.close()
while True:
    choice=int(input("Enter 1-->write\n 2-->read\n3-->copy\n4--Add More in a file:\n5--->Exist:\n"))
    if choice==5:
        break
    elif choice==1:
        #path=input("Enter the path of file which is exit:\n")
        name=input("Enter the file name with .txt as file extenstion:\n")
        w=input("Enter to write in a file:\n")
        towrtite()
        print("Date written success fully")
    elif choice==2:
         path=input("Enter the path of file which is exit:\n")
         #name=input("Enter the file name with .txt as file extenstion:\n")
         read()
    elif choice==3:
         path=input("Enter the path of file which is exit:\n")
         name=input("Enter the file name with .txt as file extenstion:\n")
         print("---DATA COPIED SUCCESSFULLY---")
         copy()
    elif choice==4:
        path=input("Enter the path of file which is exit:\n")
        #name=input("Enter the file name with .txt as file extenstion:\n")
        more=input("Enter to write in a file:\n")
        toappend()
    else:
        print("ENTER VALID CHOICE----")