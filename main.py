import rule
import graphic
import pygame
map_handler = rule.map()
run_handler = rule.run(map_handler)
game_handler = rule.run(map_handler)
graphic_handler=graphic.graphic()
###  Initialize handler 
while map_handler.life:
    graphic_handler.clock.tick(60)
    graphic_handler.screen.fill((0,0,0))
    map_handler.map_draw()
    graphic_handler.draw(map_handler.map)
    pygame.display.flip()
    ### draw map
    key=graphic_handler.key_lock()
    if key == 1:
        run_handler.left_move()
    elif key ==2:
        run_handler.right_move()
    elif key ==3:
        run_handler.up_move()
    elif key ==4:
        run_handler.down_move()
    # if key is press => key_lock unlock and return 1 2 3 4 

    graphic_handler.screen.fill((0,0,0))
    graphic_handler.draw(map_handler.map)
    # draw

    pygame.display.flip()