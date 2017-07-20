from wxpy import *
from random import shuffle,randint

kaishi = 0
bot = Bot(cache_path=True)
fhlG = bot.groups().search("飞花令")[0]
number = 1
zanshi1 = []
zi = ""
opFile = open("shicidata.txt", "r", encoding="utf-8")
data = opFile.readlines()
opFile.close()
leixing = 0
lenD=len(data)
dict={}
for i in range(10):
    dict[i]=data[0+i*600000:600000+i*600000]
dict[10]=data[6000000:lenD]

def isShi(juzi):
    for i in data:
        if juzi == i or juzi in i:
            return 1
    return 0


def chushihua():
    global number, zanshi1, zi, kaishi,leixing
    number = 1
    zanshi1 = []
    zi = ""
    kaishi = 0
    leixing = 0


def help_FHL(msg):
    global number, zi, kaishi, dict
    ranNum=randint(0,10)
    if kaishi == 1:
        if leixing==1:
            for i in dict[ranNum]:
                if zi in i:
                    if (i not in zanshi1):
                        zanshi1.append(i)
                        msg.reply(str(i))
                    break
        else:
            number-=1
            for i in dict[ranNum]:
                if len(i) > 2 and number < len(i) and i[number] == zi:
                    if (i not in zanshi1):
                        zanshi1.append(i)
                        msg.reply(str(i))
                    number += 2
                    break

    else:
        msg.reply("伦家让你先说嘛")


def start_FHL(juzi, msg):
    global number, kaishi, zi,dict
    if number == 1:
        zi = juzi[0]
    elif zi != juzi[number - 1]:
        msg.reply("大笨蛋")
        return 0
    if (number == 7):
        chushihua()
        msg.reply("飞花令已结束")
    zanshi1.append(juzi)
    ranNum = randint(0, 10)
    if isShi(juzi):
        for i in dict[ranNum]:
            if len(i) > 2 and number < len(i) and i[number] == zi:
                if (i not in zanshi1):
                    zanshi1.append(i)
                    msg.reply(str(i))
                number += 2
                break
    else:
        msg.reply("这不是诗")
    shuffle(dict[ranNum])


def start_FHL_easy(juzi, msg):

    global number, kaishi, zi, dict
    if number == 1:
        zi = juzi[0]
        number = 0
    if zi not in juzi:
        msg.reply("嘿嘿嘿")
        return 0
    if juzi in zanshi1:
        msg.reply("你说过了")
    else:
        zanshi1.append(juzi)
    ranNum=randint(0,10)
    if isShi(juzi):
        for i in dict[ranNum]:
            if zi in i:
                if (i not in zanshi1):
                    zanshi1.append(i)
                    msg.reply(str(i))
                    break
    else:
        msg.reply("这不是诗")
    shuffle(dict[ranNum])


def function_find(txt, msg):
    global leixing, kaishi, number, zanshi1
    print(msg)
    if txt == "开始飞花令":
        chushihua()
        msg.reply("飞花令已开始,请输入类型 无限 或者 有限")
        kaishi = 1
    elif txt == "终止":
        chushihua()
        msg.reply("飞花令已终止")
    elif txt == "无限":
        msg.reply("请输入第一句诗")
        leixing = 1
    elif txt == "有限":
        msg.reply("请输入第一句诗")
        leixing = 2
    elif txt=="帮助":
        help_FHL(msg)
    elif kaishi == 1:
        if leixing == 1:
            juzi = txt
            start_FHL_easy(juzi, msg)
        else:
            juzi = txt
            start_FHL(juzi, msg)


@bot.register()
def find_FHL(msg):
    if msg.sender == fhlG:
        function_find(msg.text, msg)


# 堵塞线程，并进入 Python 命令行
embed()
