import random
class map:
    def __init__(self):
        self.life = True
        self.mapsize = 4
        self.map=[[0 for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        self.map_check=[[False for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        self.direction=None
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
        self.direction = "UP"
        self.map_check=[[False for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        for i in range(self.mapsize):
            for j in range(self.mapsize):
                self.move(i,j)

    def down_move(self):
        self.direction = "DOWN"
        self.map_check=[[False for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        for i in range(self.mapsize-1,-1,-1):
            for j in range(self.mapsize):
                self.move(i,j)

    def right_move(self):
        self.direction = "RIGHT"
        self.map_check=[[False for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        for j in range(self.mapsize-1,-1,-1):
            for i in range(self.mapsize):
                self.move(i,j)

    def left_move(self):
        self.direction = "LEFT"
        self.map_check=[[False for _ in range(self.mapsize)] for _ in range(self.mapsize)]
        for j in range(self.mapsize):
            for i in range(self.mapsize):
                self.move(i,j)




# This part need Refactoring
# If some good idea get up, change part for CLEAN CODE
################## Test Case ##################

    def move(self,i,j):
        
        if self.direction == "DOWN":
            tmp_y = i+1
            tmp_x = j
            if i>=self.mapsize-1:
                return 0

        elif self.direction == "UP":
            tmp_y = i-1
            tmp_x = j
            if i<1:
                return 0

        elif self.direction == "RIGHT":
            tmp_y = i
            tmp_x = j+1
            if j>=self.mapsize-1:
                return 0

        elif self.direction == "LEFT":
            tmp_y = i
            tmp_x = j-1            
            if j<1:
                return 0


        if self.map[i][j] == 0:
            pass
        else:
            if self.map[tmp_y][tmp_x]==0:
                self.map[tmp_y][tmp_x]=self.map[i][j]
                self.map_check[tmp_y][tmp_x]=self.map_check[i][j]
                self.map[i][j]=0
                self.map_check[i][j] =False
                self.move(tmp_y,tmp_x)
            elif self.map[tmp_y][tmp_x]==self.map[i][j]:
                if self.map_check[i][j] ==True:
                    self.move(tmp_y,tmp_x)
                else:
                    self.map_check[i][j]= True
                    self.map[tmp_y][tmp_x] +=self.map[i][j]
                    self.map_check[tmp_y][tmp_x]=self.map_check[i][j]
                    self.map[i][j]=0
                    self.map_check[i][j] =False
                    self.move(tmp_y,tmp_x)
    