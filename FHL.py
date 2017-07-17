from wxpy import *

kaishi = 0
bot = Bot(cache_path=True)
fhlG = bot.groups().search("飞花令")[0]
number = 1
zanshi1 = []
zi = ""
opFile = open("data3.txt", "r", encoding="utf-8")
data = opFile.readlines()
opFile.close()

def isShi(juzi):
    for i in data:
        if juzi==i or juzi in i:
            return 1
    return 0



def chushihua():
    global number, zanshi1, zi, kaishi
    number = 1
    zanshi1 = []
    zi = ""
    kaishi = 0


def help_FHL(msg):
    global number,zi,kaishi
    if kaishi==1:
        number-=1
        for i in data:
            if len(i) > 2 and number < len(i) and i[number] == zi:
                if (i not in zanshi1):
                    zanshi1.append(i)
                    msg.reply(str(i))
                number += 2
                break
    else:
        msg.reply("伦家让你先说嘛")

def start_FHL(juzi, msg):
    global number, kaishi, zi
    if isShi(juzi)==0:
        msg.reply("大笨蛋，这不是诗")
    if number == 1:
        zi = juzi[0]
    elif zi != juzi[number - 1]:
        msg.reply("大笨蛋")
        return 0
    if (number == 7):
        chushihua()
        msg.reply("飞花令已结束")

    for i in data:
        if len(i) > 2 and number < len(i) and i[number] == zi:
            if (i not in zanshi1):
                zanshi1.append(i)
                msg.reply(str(i))
            number += 2
            break




def function_find(txt, msg):
    global kaishi, number, zanshi1
    print(msg)
    if txt == "开始飞花令":
        msg.reply("飞花令已开始,请输入第一句")
        kaishi = 1
    elif txt == "终止":
        chushihua()
        msg.reply("飞花令已终止")
    elif kaishi == 1:
        juzi = txt
        start_FHL(juzi, msg)
    elif txt=="帮助":
        help_FHL(msg)


@bot.register()
def find_FHL(msg):
    if msg.sender == fhlG:
        function_find(msg.text, msg)


# 堵塞线程，并进入 Python 命令行
embed()
