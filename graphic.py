import pygame
import asyncio

class graphic:
    def __init__(self):
        self.height=400
        self.width=600
        self.font_size=60
        pygame.init()
        pygame.display.set_caption("2048")
        self.screen=pygame.display.set_mode((self.width,self.height),0,32)
        self.clock=pygame.time.Clock()
        self.font = pygame.font.SysFont('굴림',self.font_size)


        # font and screen initalize

   # Initaialize var and font ,open window 
    def key_lock(self):
        self.key_push= False
        self.Key=None
        # keyboard is pressed=> key_push is True 
        # key is return value for what key is pressd
        while self.Key == None and self.key_push==False:
            for event in pygame.event.get():

                if event.type ==pygame.QUIT:
                    pygame.quit()

                    # quit event 
                key_list = pygame.key.get_pressed()
                if key_list[pygame.K_LEFT]:    
                    self.key= 1
                elif key_list[pygame.K_RIGHT]:
                    self.key= 2
                elif key_list[pygame.K_UP]:
                    self.key= 3
                elif key_list[pygame.K_DOWN]:
                    self.key= 4

                if event.type == pygame.KEYDOWN:
                    self.key_push =True
                    # key press => key_push is True
                elif event.type == pygame.KEYUP:
                    self.key_push =False
                    # key nonpress => key_push is False
        return self.key
    
    # left 1 right 2 up 3 down 4
    def draw(self,map):
        h_size=self.height/len(map)
        w_size=self.width/len(map)
        map_size=len(map)
        for i in range(map_size):
            for j in range(map_size):
                
                rect_obj=pygame.draw.rect(self.screen,(255,255,255),[j*w_size,i*h_size,w_size,h_size],2)
                text_obj=self.font.render(str(map[i][j]),True,(255,255,255))
                self.screen.blit(text_obj,(j*w_size+w_size/2-self.font_size/4,i*h_size+h_size/2-self.font_size/4))




