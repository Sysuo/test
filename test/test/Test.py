'''
Created on 2013/05/30

@author: a_kurosawa
'''

print("hello" + " " + "world")

words = ['a', 'b', 'c', '', "d"]

for i in words:
    if i == '':
        break
    print("num:" +str(i))

print(len("test"))

while True:
    break

def MethodA(arg):
    print("i am MethodA.")
    return lambda a: 1 * 10

# これはダメ
#printHogeHoge()

MethodA(0)

def printHogeHoge():
    """
    これらの文字列は
    どう出るのか
    気になる。
    ドキュメンテーション文字列
    """

# これはOK
printHogeHoge()

# これなんだ？
if __name__ == '__main__':
    pass

