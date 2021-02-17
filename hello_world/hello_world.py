'''
Author: your name
Date: 2021-02-16 09:20:40
LastEditTime: 2021-02-16 10:26:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /undefined/home/aoooa/PyGame_In_Framebuffer/hello_world/hello_world.py
'''
import os
import time
import random
import pygame, sys, os
from pygame.locals import *

drivers = ['/dev/fb1']
# Uncomment if you have a touch panel and find the X value for your device
#os.environ["SDL_MOUSEDRV"] = "TSLIB"
#os.environ["SDL_MOUSEDEV"] = "/dev/input/eventX"
 
class pyscope :
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print ("I'm running under X display = "+ str(disp_no))
        
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output

        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_FBDEV'):
                os.putenv('SDL_FBDEV', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print ("Driver: " +str(driver)+ "failed.")
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print ("Framebuffer size: %d x %d" % (size[0], size[1]))
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()
 
    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."
 
    def show(self):
        pygame.mouse.set_visible(False)
        white = (255, 255, 255)
        black = (0, 0, 0)
        fontObj = pygame.font.Font('SIMYOU.TTF',32)
        img = pygame.image.load('linux_icon.jpeg')
        imgbox = pygame.draw.rect(self.screen, (255, 255, 255), (0, 32, 240, 103))
        textbox = pygame.draw.rect(self.screen, (255, 255, 255), (0, 0, 176, 32))
        textSurfaceObj = fontObj.render('Hello world!',True,black,white)
        self.screen.fill(white)
        self.screen.blit(img,imgbox)
        self.screen.blit(textSurfaceObj,textbox)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
 
# Create an instance of the PyScope class
scope = pyscope()
scope.show()
