# -*-coding:utf-8 -*-
# x=靴代 y=比較する靴代 c=割引代
x=int(input())
m=int(input())
y=int(input())
c=int(input())
a=1
# 税込計算 関数にxとyの値を入れる
def tax(b):
    b=b*1.1
    return b
x=tax(x)
y=tax(y)
# 個数×値段を求める
while a<=m:
    x=x*a
    a=a+1
# 比較計算
if x-c>y:
    print(str((x-c)-y)+'円お得ですよ')
elif x-c<y:
    print(str(y-(x-c))+'円損してまうよ')

