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

MethodA(0)

# これなんだ？
if __name__ == '__main__':
    pass

