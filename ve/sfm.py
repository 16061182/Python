# -*-coding:utf-8-*-
# Author: SS and WP
import torch
import pygame
import pygame.draw
import numpy as np
from sfm_cal import *
from tt import *
import math
#from config import *
#import random


import queue


# ==================================读图bfs=============================================

class Road_map:
    map = []
    target = None
    endx = 0
    endy = 0

    def __init__(self, mapstr):
        mm = []
        for linestr in mapstr:
            line = []
            linestr = linestr[:-1]
            for num in linestr.split(' '):
                if num != '':
                    line.append(int(num))
            mm.append(line)
        self.n = len(mm)
        self.m = len(mm[0])
        self.map = mm

    def bfs(self):
        mm = self.map.copy()
        self.target = [[(-1, -1) for i in range(self.m)] for i in range(self.n)]
        q = queue.Queue()
        q.put((self.endx, self.endy))
        while not q.empty():
            head = q.get()
            # print(head)
            dx = [        (-1, 0),
                  (0, -1),        (0, 1),
                          (1, 0),         ]
            for i, j in dx:
                nx = head[0] + i
                ny = head[1] + j
                if nx in range(self.n) and ny in range(self.m):
                    if mm[nx][ny] == 0:
                        self.target[nx][ny] = head
                        mm[nx][ny] = -1
                        q.put((nx, ny))

# ==================================读图bfs=============================================

# ==================================画墙=============================================

BLOCKSIZE = 30
SCREENSIZE = [1000, 1000]
RESOLUTION = 180
AGENTSNUM = 15
BACKGROUNDCOLOR = [255, 255, 255]
AGENTCOLOR = [0, 0, 255]
LINECOLOR = [255, 0, 0]
ARIVECOLOR = [0, 100, 0]
AGENTSIZE = 13
AGENTSICKNESS = 3


walls = []

fmap = open("map.txt", "r")
m = Road_map(fmap.readlines())


for i in range(m.n):
    for j in range(m.m):
        if m.map[i][j] == 1:
            walls.append([j, i, j + 1, i])
            walls.append([j, i, j, i + 1])
            walls.append([j, i + 1, j + 1, i + 1])
            walls.append([j + 1, i, j + 1, i + 1])
        if m.map[i][j] == 3:
            m.endx = i
            m.endy = j

m.bfs()
print(m.target)
m.target[m.endx][m.endy] = (m.endx,m.endy+2)
tt = m.endx
m.endx = m.endy
m.endy = tt
wallsy = []
wallyy = []

for wall in walls:
    flag = True
    for wi in wallsy:
        if (wi[0] == wall[0]) and (wi[1] == wall[1]) and (wi[2] == wall[2]) and (wi[3] == wall[3]):
            flag = False
            wallsy.remove(wi)
            if wi[0]==wi[2]:
                wallyy.append([wi[0]-0.5,(wi[1]+wi[3])/2,wi[0]+0.5,(wi[1]+wi[3])/2])
            else:
                wallyy.append([(wi[0]+wi[2])/2, wi[3]-0.5, (wi[0]+wi[2])/2, wi[3]+0.5])
            break
    if flag:
        wallsy.append(wall)


walls = wallyy

# ==================================画墙=============================================
# ==================================pygame画图=============================================

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption('Social Force Model - Single-Room Egress')
clock = pygame.time.Clock()

arive = [22.0, 0.00, 22.00, 20.00]

# print(arive)

# initialize agents
agents = []

print(m.endx, m.endy)
for n in range(AGENTSNUM):
    agent = Agent(m.endx, m.endy)
    agents.append(agent)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()

    screen.fill(BACKGROUNDCOLOR)

    # draw walls
    for wall in walls:
        startPos = np.array([wall[0], wall[1]])
        endPos = np.array([wall[2], wall[3]])
        startPx = startPos*BLOCKSIZE
        endPx = endPos*BLOCKSIZE
        pygame.draw.line(screen, LINECOLOR, startPx, endPx)

    startPos = np.array([arive[0], arive[1]])
    endPos = np.array([arive[2], arive[3]])

    startPx = startPos*BLOCKSIZE
    endPx = endPos*BLOCKSIZE
    pygame.draw.line(screen, ARIVECOLOR, startPx, endPx)

    # ==================================pygame画图=============================================

    # ==================================计算社会力和寻路=============================================
    for idai, ai in enumerate(agents):

        nowx = int(ai.pos[0])
        nowy = int(ai.pos[1])
        if nowx>m.endx :
            ai.dest = np.array([m.endx+2,m.endy])
        else:
            newx = m.target[nowy][nowx][1] + 0.5
            newy = m.target[nowy][nowx][0] + 0.5
            ai.dest =  np.array([newx, newy])
        print(ai.pos,"--->",ai.dest)

        ai.direction = normalize(ai.dest - ai.pos)
        ai.desiredV = ai.desiredSpeed*ai.direction
        # 计算受力
        adapt = ai.adaptVel()
        peopleInter = 0.0
        wallInter = 0.0

        for idaj, aj in enumerate(agents):
            if idai == idaj:
                continue
            peopleInter += ai.peopleInteraction(aj)

        for wall in walls:
            wallInter += ai.wallInteraction(wall)

        sumForce = adapt*2  + peopleInter*1.5 + wallInter*0.1
        # 计算加速度
        accl = sumForce/ai.mass
        # 计算速度
        ai.actualV =accl*0.2  + ai.actualV   # consider dt = 0.5
        # 计算位移
        ai.pos = ai.pos + ai.actualV*0.2

        # ==================================计算社会力和寻路=============================================

        if (ai.pos[0] >= 22.0) & (ai.Goal == 0):
            print('test')
            ai.Goal = 1
            ai.timeOut = pygame.time.get_ticks()
            agents.remove(ai)
            print('Time to Reach the Goal:', ai.timeOut)

    # ==================================pygame画图=============================================


    for agent in agents:

        scPos = [0, 0]
        scPos[0] = int(agent.pos[0]*BLOCKSIZE)
        scPos[1] = int(agent.pos[1]*BLOCKSIZE)

        endPos = [0, 0]
        endPos[0] = int(agent.pos[0]*BLOCKSIZE + agent.actualV[0]*BLOCKSIZE)
        endPos[1] = int(agent.pos[1]*BLOCKSIZE + agent.actualV[1]*BLOCKSIZE)

        endPosDV = [0, 0]
        endPosDV[0] = int(agent.pos[0]*BLOCKSIZE + agent.desiredV[0]*BLOCKSIZE)
        endPosDV[1] = int(agent.pos[1]*BLOCKSIZE + agent.desiredV[1]*BLOCKSIZE)

        pygame.draw.circle(screen, AGENTCOLOR, scPos, AGENTSIZE, AGENTSICKNESS)
        pygame.draw.line(screen, AGENTCOLOR, scPos, endPos, 2)
        pygame.draw.line(screen, [255, 60, 0], scPos, endPosDV, 2)

    scPos = [1*BLOCKSIZE, 3*BLOCKSIZE]
    pygame.display.flip()
    clock.tick(50)
    # ==================================pygame画图=============================================
