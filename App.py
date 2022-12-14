from flask import Flask, render_template, request, redirect
from PIL import ImageColor
import board
import neopixel
import random
import numpy as np
import threading
import time

pxl=neopixel.NeoPixel(board.D18, 300, auto_write=False)
pxl.brightness=0.20
color='#ff0000'

arr=[[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12, 13,  14],
    [ 34,  33,  32,  31,  30,  29,  28,  27,  26,  25,  24,  23,  22, 21,  20],
    [ 40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52, 53,  54],
    [ 74,  73,  72,  71,  70,  69,  68,  67,  66,  65,  64,  63,  62, 61,  60],
    [ 80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92, 93,  94],
    [114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100],
    [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134],
    [154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140],
    [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174],
    [194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180],
    [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214],
    [234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224, 223, 222, 221, 220],
    [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254],
    [274, 273, 272, 271, 270, 269, 268, 267, 266, 265, 264, 263, 262, 261, 260],
    [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294]]
# arr=np.transpose(arr)[::-1]

alphabet=[[[0, 0, 0, 1, 1, 1, 1, 1, 1, 1],[0, 0, 1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 0, 0, 1, 1, 0, 0],[1, 1, 1, 0, 0, 0, 1, 1, 0, 0],[1, 1, 1, 0, 0, 0, 1, 1, 0, 0],[0, 1, 1, 1, 0, 0, 1, 1, 0, 0],[0, 0, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 1, 1, 1, 1, 1, 1, 1]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 0, 0, 1, 1, 1, 0]],
                    [[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 1, 0, 0, 0, 0, 1, 1, 1],[0, 1, 1, 0, 0, 0, 0, 1, 1, 0]],
                    [[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 1, 1, 1, 1, 1, 0]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1]],
                    [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]],
                    [[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 1, 1, 1, 1],[0, 1, 0, 0, 1, 1, 1, 1, 1, 0]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
                    [[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1]],
                    [[1, 1, 0, 0, 0, 0, 1, 1, 1, 0],[1, 1, 0, 0, 0, 0, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1, 1, 0, 0, 0],[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],[0, 1, 1, 1, 0, 0, 1, 1, 1, 0],[1, 1, 1, 0, 0, 0, 0, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],[0, 0, 1, 1, 1, 0, 0, 0, 0, 0],[0, 0, 0, 1, 1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
                    [[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 1, 1, 1, 1, 1, 0]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 0, 0, 0, 0],[0, 1, 1, 1, 1, 0, 0, 0, 0, 0]],
                    [[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 0, 0, 0, 1, 1, 0, 1, 1],[1, 1, 0, 0, 0, 1, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 1, 1, 1, 0, 1, 1]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 1, 1, 0, 0, 0, 0],[1, 1, 0, 0, 1, 1, 1, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 1, 1, 1, 1, 0, 1, 1, 1, 1]],
                    [[0, 1, 1, 1, 1, 0, 0, 1, 1, 0],[1, 1, 1, 1, 1, 1, 0, 1, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 1, 0, 1, 1, 1, 1, 1, 1],[0, 1, 1, 0, 0, 1, 1, 1, 1, 0]],
                    [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0, 0, 0]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[0, 0, 0, 0, 0, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 0]],
                    [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1, 1, 0],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],[0, 0, 0, 0, 0, 0, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 0, 0],[1, 1, 1, 1, 1, 1, 1, 0, 0, 0]],
                    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 1, 1, 1, 0],[0, 0, 0, 0, 0, 1, 1, 1, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
                    [[1, 1, 1, 0, 0, 0, 0, 1, 1, 1],[1, 1, 1, 1, 0, 0, 1, 1, 1, 1],[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],[0, 0, 0, 1, 1, 1, 0, 0, 0, 0],[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],[1, 1, 1, 1, 0, 0, 1, 1, 1, 1],[1, 1, 1, 0, 0, 0, 0, 1, 1, 1]],
                    [[1, 1, 1, 1, 1, 0, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 0, 0, 1, 1],[0, 0, 0, 0, 1, 1, 0, 0, 1, 1],[0, 0, 0, 0, 1, 1, 0, 0, 1, 1],[0, 0, 0, 0, 1, 1, 0, 0, 1, 1],[0, 0, 0, 0, 1, 1, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 0]],
                    [[1, 1, 0, 0, 0, 0, 0, 1, 1, 1],[1, 1, 0, 0, 0, 0, 1, 1, 1, 1],[1, 1, 0, 0, 0, 1, 1, 1, 1, 1],[1, 1, 0, 0, 1, 1, 1, 0, 1, 1],[1, 1, 0, 1, 1, 1, 0, 0, 1, 1],[1, 1, 1, 1, 1, 0, 0, 0, 1, 1],[1, 1, 1, 1, 0, 0, 0, 0, 1, 1],[1, 1, 1, 0, 0, 0, 0, 0, 1, 1]],
                    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]

app = Flask(__name__)

##initialization for the snake game
def intialize():
    global flag,rf,cf,r,c,lrc,chek
    flag=0
    rf,cf=random.randint(0,14),random.randint(0,14)
    pxl[arr[rf][cf]]=(0,255,0)
    pxl.show()
    print(rf,cf)
    r=c=0
    lrc=[[r,c]]
    chek ='here'
# intialize()
def ponginit():
    global tempr1,tempr2,sl
    tempr1=7
    tempr2=7
    sl=[8,7] #start location

def led(r,c,s=1):  ## To On and Off the leds to red
    if s==0:
        pxl[arr[r][c]]=(0,0,0)
        pxl.show()
    else:
        pxl[arr[r][c]]=(225,0,0)
        pxl.show()

def animation1():
    pxl.fill((0,0,0))
    pxl.show()
    for i in range (15):
        for j in range (15):
            pxl[arr[i][j]]=(0,0,255)
            pxl[arr[j][i]]=(0,0,255)
            pxl[arr[14-j][i]]=(0,0,255)
            pxl[arr[j][14-i]]=(0,0,255)
        pxl.show()
    for i in range (15):
        for j in range (15):
            pxl[arr[i][j]]=(0,0,0)
            pxl[arr[j][i]]=(0,0,0)
            pxl[arr[14-j][i]]=(0,0,0)
            pxl[arr[j][14-i]]=(0,0,0)
        pxl.show()

def pongpong():
    global gopong,sl
    # pxl.fill((0,0,0))
    # pxl.show()
    temptime=1.5
    casev=caseh=1
    gopong=1
    print('started')
    while gopong:
        pxl[arr[sl[0]][sl[1]]]=(0,255,0)
        pxl.show()
        time.sleep(temptime)
        pxl[arr[sl[0]][sl[1]]]=(0,0,0)
        pxl.show()
        if sl[0]>13:
            casev=-1
        elif sl[0]<1:
            casev=+1
        if sl[1]>13:
            if sl[0] in [5,7,9]:
                sl[1]=0
            else:
                caseh=-2
        elif sl[1]<1:
            temptime=0.8
            if sl[0] in [5,7,9]:
                sl[1]=14
            else:
                caseh=+2
        if checkup(sl):
            print('gameover')
            animation1()
            # ponginit()
            break
        sl[0]=sl[0]+casev
        sl[1]=sl[1]+caseh
   
def checkup(sl):
    global tempr1, tempr2
    print(tempr1,tempr2,sl)
    if (sl[1]==0 or sl[1]==14) and (sl[0] not in [tempr1,tempr1+1,tempr1-1,tempr2,tempr2+1,tempr2-1]):
        return(True)
    else:
        return(False)

def snakethread(intel):
    global r,c,lrc,chek,rf,cf,flag
    while (go):
        if intel=="up":
            r=r-1
        elif intel=="left":
            c=c+1
        elif intel=="right":
            c=c-1
        elif intel=="down":
            r=r+1
        else:
            break
            
        if c<0:
            c=c+15
        elif r<0:
            r=r+15
        elif c>14:
            c=c-15
        elif r>14:
            r=r-15

        pxl[arr[rf][cf]]=(0,255,0)
        pxl.show()

        cr,cc=lrc[-1]        
        if ((len(lrc)>1) and ([r,c] in lrc)):
            flag=1

        if flag==1:
            print("Game Over!")
            animation1()
            intialize()
            break

        lrc.insert(0,[r,c])
        led(lrc[0][0],lrc[0][1])
        led(cr,cc,0)
        lrc.pop()
                
        if (lrc[0]==[rf,cf]):
            rf,cf=random.randint(0,14),random.randint(0,14)
            print("food is {},{}".format(rf,cf))
            pxl[arr[rf][cf]]=(0,255,0)
            pxl.show()
            lrc.append([cr,cc])
            led(cr,cc)
        print(lrc)
        time.sleep(0.2)

@app.route('/')
def home():
    global go,gopong 
    go=gopong=0
    pxl.fill((0,0,0))
    pxl.show()
    return render_template('home.html')

@app.route('/snake', methods=['GET'])
def snake():
    intialize()
    return render_template('snake.html')   

@app.route('/snakegame/<string:intel>', methods=['GET'])
def snakegame(intel):
    global go, chek
    go=0
    time.sleep(0.3)
    if chek!=intel:
        go=1
        x=threading.Thread(target=snakethread ,args=(intel,))
        x.start()
    ##function end
    return render_template('snakegame.html')

# @app.route('/debug', methods=['GET'])
# def functioncheck():
#     pongpong()
#     return render_template('debug.html') 

@app.route('/pong', methods=['GET'])
def pong():
    ponginit()
    for i in range(3):
        pxl[arr[i+tempr1-1][0]]=(255,0,0)
        pxl[arr[i+tempr2-1][14]]=(0,0,255)
    pxl.show()
    y=threading.Thread(target=pongpong)
    y.start()
    # pongpong()
    return render_template('pongplayers.html') 

@app.route('/ponggame/player1/<string:move>', methods=['GET'])
def ponggame1(move):
    global arr,tempr1    
    if move=='left1':
        tempr1+=1
    elif move=='right1':
        tempr1-=1
    else:
        tempr1=tempr1
    if tempr1<2:
        tempr1=2
    elif tempr1>13:
        tempr1=13
    for j in range(15):
        pxl[arr[j][0]]=(0,0,0)
    pxl.show()
    for i in range(3):
        pxl[arr[i+tempr1-1][0]]=(255,0,0)
    pxl.show()
    time.sleep(0.005)
    return render_template('pong1.html')

@app.route('/ponggame/player2/<string:move>', methods=['GET'])
def ponggame2(move):
    global arr,tempr2
    if move=='left2':
        tempr2+=1
    elif move=='right2':
        tempr2-=1
    else:
        tempr2=tempr2
    if tempr2<2:
        tempr2=2
    elif tempr2>13:
        tempr2=13   
    for j in range(15):
        pxl[arr[j][14]]=(0,0,0)
    pxl.show()
    for i in range(3):
        pxl[arr[i+tempr2-1][14]]=(0,0,255)
        pxl.show()
    time.sleep(0.005)
    return render_template('pong2.html')



ButtonPressed=0
@app.route('/button', methods=["GET", "POST"])
def button():     
    global ButtonPressed
    if request.method == "POST":
        ButtonPressed+=1
        if ButtonPressed==5:
            return redirect('https://www.youtube.com/watch?v=eBGIQ7ZuuiU&ab_channel=YouGotRickRolled/autoplay=1')
        else:
            return render_template("button.html", ButtonPressed = ButtonPressed)
    ButtonPressed=0
    return render_template("button.html", ButtonPressed = ButtonPressed)

@app.route('/scroll', methods=["GET", "POST"])
def scroll():    
    global color 
    pxl.fill((0,0,0))
    pxl.show()
    def scrollfun(inpt,color):
        global arr,alphabet
        temparr=arr
        temparr=np.transpose(temparr)[::-1]
        text=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
        buffer=[0,0,0,0,0,0,0,0,0,0]
        # inpt='fuck you'
        inp=("  "+inpt+"  ").lower()
        reqcolor=ImageColor.getrgb(color)
        print(reqcolor)
        case={0:(0,0,0), 1:reqcolor}

        nowmat=[]
        for k in inp:
            for i in alphabet[text.index(k)]:
                nowmat.append(i)
            nowmat.append(buffer)
        templen=len(nowmat)

        while(templen>=15):
            for i in range(15):
                for j in range (10):
                    pxl[temparr[i][j+3]]=case[nowmat[i][j]]
            time.sleep(0.04)
            pxl.show()
            nowmat.pop(0)
            templen-=1
    ##end function
    
    if request.method == "POST":
        inpt=request.form['ptext']
        color=request.form.get('Color')
        scrollfun(inpt,color)
        return render_template("scroll.html", COLOR=color)
    return render_template("scroll.html", COLOR=color)


@app.route('/matrix', methods=['GET','POST'])    
def matrix():
    global color
    global arr
    pxl.fill((0,0,0))
    pxl.show()
    if request.method == "POST":
        selected=request.form.getlist('LED')
        color=request.form.get('Color')
        print("the value is {}".format(selected))
        for i in selected:
            i=i.strip('][').split(',')
            # print(arr[int(i[0])][int(i[1])])
            pxl[arr[int(i[0])][int(i[1])]]=ImageColor.getrgb(color)
            pxl.show()
        print(ImageColor.getrgb(color))
        return render_template('matrix.html', SELECTED=selected, COLOR=color)
    return render_template('matrix.html', COLOR=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True) ## To run across LAN you can acess thought any of the devices by entering your ip followed by port http://192.168.0.###:80
    # app.run(debug=True)