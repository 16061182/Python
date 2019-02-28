# readme

## 运行环境 

* python3  
* pygame  

 ## 寻路策略

```python
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

```



读图和bfs寻路。我们用bfs先将每个格子的最短路径找出来，然后target中存了每个格子的下一个目标点是哪。

你们读读代码，论文润色一下，吹吹比

## 社会力模型

看ppt “2018 - 6 - 2 社会力 神经网络 _6.pdf“  

然后在社会力基础上添加了，每个点当前格子到寻路策略中的下一格的一个引导力。这样每个点就会在迷宫中寻路了。

## 使用方法

map.txt 中是21*21的地图 1为墙 3为出口

运行sfm

