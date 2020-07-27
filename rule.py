import random
class map:
    def __init__(self):
        self.life = True
        self.mapsize = 4
        self.map=[[0 for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        
    def print_map(self):
        for i in range(self.mapsize):
            for j in range(self.mapsize):
                print(self.map[i][j],end=" ")
            print()

    def map_draw(self):
        count=0
        empty_map=[]
        for i in range(self.mapsize):
            for j in range(self.mapsize):
                if self.map[i][j]==0:
                    count+=1
                    empty_map.append([i,j])
                else:
                    pass
        if count ==0:
            self.life = False
        else:
            rand_position = empty_map[random.randint(0,len(empty_map)-1)]
            self.map[rand_position[0]][rand_position[1]]=2

class run:
    def __init__(self,map):
        self.map = map.map
        self.mapsize=map.mapsize
        self.plus_check=[[0 for _ in range(self.mapsize)] for _ in range(map.mapsize)]
        # if plus 0=>1 in next array

    def up_move(self):
        self.plus_check=[[0 for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        for i in range(self.mapsize-1,0,-1):
            for j in range(self.mapsize):
                if self.map[i-1][j] ==0:
                    self.map[i-1][j]= self.map[i][j]
                    self.map[i][j]=0
                elif self.plus_check[i][j] != 0:
                    pass
                elif self.map[i][j]==self.map[i-1][j]:
                    self.map[i-1][j]+=self.map[i][j]
                    self.map[i][j]=0
                    self.plus_check[i-1][j]=1
                else:
                    pass

    def down_move(self):
        self.plus_check=[[0 for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        for i in range(self.mapsize-1):
            for j in range(self.mapsize):
                if self.map[i+1][j] ==0:
                    self.map[i+1][j]= self.map[i][j]
                    self.map[i][j]=0
                elif self.plus_check[i][j] != 0:
                    pass
                elif self.map[i][j]==self.map[i+1][j]:
                    self.map[i+1][j]+=self.map[i][j]
                    self.map[i][j]=0
                    self.plus_check[i+1][j]=1
                else:
                    pass

    def right_move(self):
        self.plus_check=[[0 for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        for j in range(self.mapsize-1):
            for i in range(self.mapsize):
                if self.map[i][j+1] ==0:
                    self.map[i][j+1]= self.map[i][j]
                    self.map[i][j]=0
                elif self.plus_check[i][j] != 0:
                    pass
                elif self.map[i][j]==self.map[i][j+1]:
                    self.map[i][j+1]+=self.map[i][j]
                    self.map[i][j]=0
                    self.plus_check[i][j+1]=1
                else:
                    pass

    def left_move(self):
        self.plus_check=[[0 for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        for j in range(self.mapsize-1,0,-1):
            for i in range(self.mapsize):
                if self.map[i][j-1] == 0:
                    self.map[i][j-1] = self.map[i][j]
                    self.map[i][j]=0
                elif self.plus_check[i][j] != 0:
                    pass
                elif self.map[i][j]==self.map[i][j-1]:
                    self.map[i][j-1]+=self.map[i][j]
                    self.map[i][j]=0
                    self.plus_check[i][j-1]=1
                else:
                    pass

# This part need Refactoring
# If some good idea get up, change part for CLEAN CODE
        
a=map()
b=run(a)
################## Test Case ####################
while a.life:
    a.map_draw()
    a.print_map()
    #input()
    b.left_move()