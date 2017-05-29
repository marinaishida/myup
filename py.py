# -*-coding:utf-8 -*-
from random import randint
hands={0:"グー",1:"チョキ",2:"パー"}
rules={(0,0):"あいこ",(0,1):"勝ち",(0,2):"負け",
       (1,0):"負け",(1,1):"あいこ",(1,2):"勝ち",
       (2,1):"勝ち",(2,2):"あいこ",(2,0):"負け"}
       
while True:
    pc=randint(0,2)
    print("0:グー 1:チョキ 2:パー 3:やめる")
    user=input(">> ")
    if user==3:
       break
    if user not in (0,1,2):
        continue
    print("you"+hands[user]+"computer"+hands[pc])
    print(rules[(user,pc)])