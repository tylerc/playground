#/usr/bin/env python
import time
import string
import random

# PyGame Constants
import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import box
import manager
import gameobject

def main():
	world = manager.World()
	world.run()

if __name__=="__main__":
	main()