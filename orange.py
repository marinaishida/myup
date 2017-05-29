#!/usr/bin/env python
# -*-coding:utf-8 -*-
from random import randint
import itertools
tank_data=[("M3",1,2),("III",1,3),("八九式",1,4)]
def tank_data2(tup):
    return tup[1]+tup[2]
a=tank_data2(tank_data[0])
b=tank_data2(tank_data[1])
c=tank_data2(tank_data[2])
x=tank_data
x.sort(key=tank_data2,reverse=True)
e=dict([[a,"M3"],[b,"III"],[c,"八九式"]])
g=[a,b,c]
m=list(itertools.permutations(g,2))
n=dict([[m[0],"勝ち"],[m[1],"負け"],[m[2],"勝ち"],[m[3],"負け"],[m[4],"負け"],[m[5],"勝ち"]])
while True:
    pc=randint(3,5)
    print("好きな数字を入力してください")
    user=input(">> ")
    if user in(3,4,5):
        print("あなた"+e[user]+"コンピュータ"+e[pc])
        print(n[(user,pc)])
    elif user not in(3,4,5):
        break
    else:
        print("error")
        break