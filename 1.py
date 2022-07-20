import random
import os
import time

ju = 0
fs = 0
dfs = 0
gz = ('''
    游戏规则:
        这是一个关于石头剪刀布的游戏
        战胜对方加一分；
        对战10局后分数多者获胜；
        如果十局后分数想等，则加赛至分数多于对方两分胜利；
        超过二十局仍未结束时，分数多者胜利；
        分数仍然想等则双方平局。

        ps：中途退出者自动判负。
    ''')
print(gz)


def yx():
    global fs
    global dfs
    os.system('cls')
    jq = ''
    print('石头剪刀布')
    print('请输入你要出什么')
    print('''
    \'1\'或者\'石头\'表示石头
    \'2\'或者\'剪刀\'表示剪刀
    \'3\'或者 \'布\' 表示布
    \'4\'或者 \'规则\' 查看规则
    \'5\'或者 \'退出\' 退出游戏
    \'6\'或者 \'比分\' 显示分数
    ''')
    global su, cw
    su = str(input('》'))
    if su == '1' or su == '石头':
        su = '石头'
        ss = 1
        cw = 1
    elif su == '2' or su == '剪刀':
        su = '剪刀'
        ss = 2
        cw = 1
    elif su == '3' or su == '布':
        su = '布'
        ss = 3
        cw = 1
    elif su == '4' or su == '规则':
        os.system('cls')
        global gz
        print(gz)
        input('按下任意建回车返回')
        return
    elif su == '5' or su == '退出':
        os.system('cls')
        return
    elif su == '6' or su == '比分':
        print(f'''你的分数为{fs}
对方的分数为{dfs}
        ''')
        input('按下任意建回车返回')
        return
    else:
        print('您输入错误，请重新输入')
        time.sleep(0.5)
        return
    js = random.randint(1, 3)
    if js == 1:
        jq = '石头'
    elif js == 2:
        jq = '剪刀'
    elif js == 3:
        jq = '布'
    if ss == js:
        print('你出的是%s' % su)
        print('对方出的是%s' % jq)
        print('平局')
    elif (ss == 1 and js == 2) or (ss == 2 and js == 3) or (ss == 3 and js == 1):
        print('你出的是%s' % su)
        print('对方出的是%s' % jq)
        print("恭喜你，你赢了！！！")
        fs += 1
    else:
        print('你出的是%s' % su)
        print('对方出的是%s' % jq)
        print("很遗憾，你输了。")
        dfs += 1
    time.sleep(1)
    os.system('cls')


cw = 0
su = ''
while su != '5':
    if ju < 10:
        yx()
        if cw == 1:
            ju += 1
            cw = 0
    elif ju == 10:
        if fs > dfs:
            print('恭喜你，你赢了！！！')
            break
        elif fs < dfs:
            print("很遗憾，你输了。")
            break
        else:
            yx()
            if cw == 1:
                ju += 1
                cw = 0
    elif ju < 20:
        if fs - dfs >= 2:
            print('恭喜你，你赢了！！！')
            break
        elif dfs - fs >= 2:
            print("很遗憾，你输了。")
            break
        else:
            yx()
            if cw == 1:
                ju += 1
                cw = 0
    elif ju == 20:
        if fs > dfs:
            print("恭喜你，你赢了！！！")
            break
        elif dfs > fs:
            print("很遗憾，你输了。")
            break
        else:
            print('平局，你们旗鼓相当')
            break