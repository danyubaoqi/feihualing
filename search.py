import time

opFile=open("data3.txt","r",encoding="utf-8")
data=opFile.readlines()
while True:
    zi = input("请输入字")
    number = int(input("请输入第几个"))
    for i in data:
        if ( len(i)>2and number<=len(i) and i[number-1]==zi):
            print(i)
            if (input("") == "guo"):
                break
            else:
                continue

opFile.close()


