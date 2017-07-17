需要python3.x环境
安装itchat，wxpy两个库

search.py为查询一个字在第几个位置的诗词的，输入guo则进入下次查询，输入其他任意字符则查找下一个吻合的诗词

可以跟人或者在群聊里头充当机器人
fhlG = bot.groups().search("飞花令")[0]
"飞花令"改成群聊名字，如果是跟人玩改成

fhlG = bot.friends().search("飞花令")[0]
"飞花令"改成朋友的微信名
运行程序的现实二维码，微信扫描登陆，对手机客户端的登录状态无影响，但是如果手机微信登出，则程序也会显示登出需重新登录
了解itchat，请访问 http://itchat.readthedocs.io/zh/latest/
了解wxpy，请访问 https://github.com/youfou/wxpy
