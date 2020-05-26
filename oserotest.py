# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:19:42 2019

@author: yuichiro
"""

import numpy as np

def start():#盤の初期配置を返す
    board = np.zeros((8,8))
    board[3][3]=1
    board[4][4]=1
    board[3][4]=2
    board[4][3]=2
    return board


def move(num,myplace):
    lst=myplace
    if num==1:
        ls = [lst[0],lst[1]-1]
    elif num==2:
        ls = [lst[0]-1,lst[1]-1]
    elif num==3:
        ls = [lst[0]-1,lst[1]]
    elif num==4:
        ls = [lst[0]-1,lst[1]+1]
    elif num==5:
        ls = [lst[0],lst[1]+1]
    elif num==6:
        ls = [lst[0]+1,lst[1]+1]
    elif num==7:
        ls = [lst[0]+1,lst[1]]
    elif num==8:
        ls = [lst[0]+1,lst[1]-1]#lst[]を別の文字で置いてからやったほうがよかった
    
    
    if onboard(ls)==0:#盤から出るとき
        ls=[-1,-1]
    
    return ls
##########################################################################
def onboard(ls):
    a=1
    if ls[0]<0 or ls[0]>7 or ls[1]<0 or ls[1]>7:#盤から出るとき
       a=0
    return a
##########################################################################
def search(num,place,board):
    a=list(range(1,9))#方向を定めるリスト
    myplace=place#置いた石の座標
    lst=[]#返すリスト
    
    if num==1:#stone:置いた石と逆の色の石
        stone=2
    elif num==2:
        stone=1
    
    for i in a:#すべての方向において隣の石が何かを確認
        ls=move(i,myplace)
        if onboard(ls)==1:#移動方向が盤上
            a=ls[0]
            b=ls[1]
            if board[a][b]==stone:#隣の石が自分と違う色であるとき、その方向を返す
                lst.append(i)
    
    return lst#おいてはいけない場所の時は空になる
#########################################################################
def search2(num,myplace,lst,board):
    if num==1:#stone:置いた石と逆の色の石
        stone=2
    elif num==2:
        stone=1
    ls=[]#返すリスト
    ls3=[]#移動先の座標を格納
    
    for i in lst:
        my=myplace
        num2=0
        ls2=[]#仮置きりスト(可能性のある座標を仮置きして、挟まれていたらlsに追加)
        while num2==0:#自分と同じ色の石が出てくるか、石がなくなるか、盤から出ない限りループ
            ls3=move(i,my)#移動先の座標
            if onboard(ls3)==1:
                if board[ls3[0]][ls3[1]]==stone:#移動先が自分と違う色の石
                    ls2.append(ls3)
                elif board[ls3[0]][ls3[1]]==num:#移動先が自分と同じ色の石、searchより少なくとも一つの石はひっくり返せる
                    ls.extend(ls2)
                    num2=1
                elif board[ls3[0]][ls3[1]]==0:#移動した先に自分の石がなかった
                    num2=1
            else:
                num2=1
            my=ls3
    return ls
###################################################################################
def reverse(num,myplace,lst,board):
    ln=len(lst)#lstの要素数を調べる(len([[1,2],[3,4]])=2となる)
    
    for i in range(ln):
        y=lst[i][0]
        x=lst[i][1]
        
        board[y][x]=num#石をひっくり返す
        if i==0:
            board[myplace[0]][myplace[1]]=num
    return board
####################################################################################
def testboard(board):
    for i in [1,2]:
        board[i][3]=1
    return board
##################################################################################
def putstone():
    ok=0#置く場所が盤上：1 盤外：０
    while ok==0:
        a = input("石の座標を入力 x,y :")#str型
        
        b=a.split(",")
        ytemp=b[1]
        xtemp=b[0]
        
        y=int(ytemp)
        x=int(xtemp)
        
        list=[y,x]
        
        if onboard(list)==1:
            ok=1
        elif onboard(list)==0:
            ok=0
            print("その場所に置くことはできません")
    return list
####################################################################################
def turn(num,board):
    startboard=board#初期盤面
    ok=1
    while ok==1:#ひっくり返せる石がなかった時に戻るためのループ
        place=putstone()#place:石を置いた場所
        maymove=search(num,place,startboard)
        turnplace=search2(num,place,maymove,startboard)
        if len(turnplace)==0:#ひっくり返す石がない
            print("その場所に置くことはできません")
            continue
        newboard=reverse(num,place,turnplace,startboard)
        ok=2
    return newboard
####################################################################################
####################################################################################
#def log():#待ったができるように、盤面の推移を記録する
###################################################################################
def judge(num,board):
    a=2#a:1置く場所発見
    
    for i in range(8):
        for j in range(8):
            if board[i][j]==0:
                place=[i,j]
                print(place)
                maymove=search(num,place,board)
                turnplace=search2(num,place,maymove,board)
                if len(turnplace)!=0:#ひっくり返せる石があった
                    a=2
                    break
        if a==2:
            break
    
    return a
####################################################################################
def Game():
    board = start()
    print(board)
    
    play=1

##################################################################################
if __name__ == "__main__":
    board = start()
    print(board)
    

            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    