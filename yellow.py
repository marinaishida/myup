#!/usr/bin/env python
# -*-coding:utf-8 -*-
pref_dict={(43,141):"北海道",(40,142):"青森",(39,140):"岩手"}
nearest_dist=1000
nearest_cap=''
print("緯度と経度を入力してください")
user=input()
for cnt,item in enumerate(pref_dict):
    dist=(user[0]-item[0])**2+(user[1]-item[1])**2
    if nearest_dist>dist:
        nearest_dist=dist
        nearest_cap=pref_dict[item]
    elif nearest_dist<=dist:
        print("数値が大きすぎます")
        continue
    else:
        break
print("一番近い都市は"+nearest_cap+"です")
dist_2=str(dist)
print("距離は"+dist_2+"です")