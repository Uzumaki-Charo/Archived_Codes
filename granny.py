# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:48:37 2020

@author: DELL
"""
import math as m
def tour(friends, friend_towns, home_to_town_distances):
    sum=home_to_town_distances.get(friend_towns[0][1])
    friend_towns=[[friend, town] for friend,town in friend_towns if friend in friends]
    for i in range(1,len(friend_towns)):
        sum+=m.sqrt(home_to_town_distances.get(friend_towns[i][1])**2-home_to_town_distances.get(friend_towns[i-1][1])**2)
        print(sum)
        print(home_to_town_distances["X2"])
    return int(m.floor(sum+home_to_town_distances.get(friend_towns[len(friend_towns)-1][1])))
    

def find(x):
    z=x+1
    y=int(m.sqrt(z))
    s=0
    k=y
    while x>(z-y):
        s=m.sqrt(z**2-y**2)
        if x==s:
            return [y, z]
        else:
            y+=1
            k+=1
        if (z-y)==0:
            z+=1
            y=k
    
    
friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
bb=[['B1', 'Y1'], ['B2', 'Y2'], ['B3', 'Y3'], ['B4', 'Y4'], ['B5', 'Y5']]
ss={'Y1': 60.0, 'Y2': 80.0, 'Y3': 100.0, 'Y4': 110.0, 'Y5': 150.0}

print(tour(friends1, fTowns1, distTable1))
#print(find(3))