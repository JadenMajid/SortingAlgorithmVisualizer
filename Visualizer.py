from heapq import merge
import pygame
import copy
from pygame import gfxdraw
import random
import math
import numpy as np
import time
import sys
import pyaudio
"""
-----TO DO-----
1) ADD MORE SORTING FUNCTIONS!!!!!
2) Add audio 
3) 



-----USEFUL FUNCTIONS-----
0) Datatype: Name of method: purpose
1) List: random.shuffle(list): randomize contents of list
2) 



"""

# Color Constants
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0,   0,   255)
GREEN = (0,   255, 0)
RED = (255, 0,   0)
YELLOW = (255,   255, 0)
ORANGE = (255,  165, 0)

# Size of Screen
HEIGHT = 600
WIDTH = 800

# Amount of Rectangles
N = WIDTH // 2


def issorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]):  # i is the index of the previous element
            return False
    return True


def nextlov(screen, lov, name):
    if name == "bubble":
        bubblesort(screen, lov)
    elif name == "bogo":
        bogosort(screen, lov)
    elif name == "insertion":
        insertionSort(screen, lov)
    elif name == "shell":
        shellSort(screen, lov)
    return lov


def bubblesort(screen, lov):
    for i in range(len(lov)):
        for j in range(0, len(lov) - i - 1):
            if lov[j] > lov[j + 1]:
                temp = lov[j]
                lov[j] = lov[j+1]
                lov[j+1] = temp
            eventHandler(screen, pygame.event.get(), lov)
            render(screen, lov, lov[j+1])


def shellSort(screen, lov):
    n = len(lov)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = lov[i]
            j = i
            while j >= interval and lov[j - interval] > temp:
                lov[j] = lov[j - interval]
                j -= interval
                eventHandler(screen, pygame.event.get(), lov)
                render(screen, lov, lov[j])

            lov[j] = temp
        interval //= 2


def insertionSort(screen, lov):
    for i in range(1, len(lov)):
        key = lov[i]
        j = i-1
        while j >= 0 and key < lov[j]:
            lov[j + 1] = lov[j]
            j -= 1
            eventHandler(screen, pygame.event.get(), lov)
            render(screen, lov, lov[j])
        lov[j + 1] = key


def bogosort(screen, lov):
    while not issorted(lov):
        random.shuffle(lov)
        eventHandler(screen, pygame.event.get(), lov)
        render(screen, lov, -1)


def render(screen, lov, h):
    i = 0
    screen.fill(BLACK)
    for v in lov:
        if v == h:
            pygame.draw.rect(screen, RED, pygame.Rect(
                i * WIDTH/N, HEIGHT - v - HEIGHT/N+3, WIDTH/N+1, v + HEIGHT/N))
        else:
            pygame.draw.rect(screen, WHITE, pygame.Rect(
                i * WIDTH/N, HEIGHT - v - HEIGHT/N+3, WIDTH/N+1, v + HEIGHT/N))
        i += 1
    pygame.display.flip()
    pygame.display.update()


def eventHandler(screen, events, lov):
    for event in events:
        # Only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # Change the value to False, to exit the main loop
            running = False

        # Mouse event handler
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            pass

        # Key event handler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                nextlov(screen, lov, "bubble")
            if event.key == pygame.K_2:
                nextlov(screen, lov, "insertion")
            if event.key == pygame.K_3:
                nextlov(screen, lov, "shell")
            if event.key == pygame.K_0:
                nextlov(screen, lov, "bogo")
            if event.key == pygame.K_r:
                random.shuffle(lov)
                main(lov)
            if event.key == pygame.K_SPACE:
                render(screen, lov, -1)
                main(lov)
            if event.key == pygame.K_ESCAPE:
                sys.exit()


def main(arr):

    pygame.init()
    clock = pygame.time.Clock()
    """
    # Audio Stuff
    p = pyaudio.PyAudio()

    VOLUME = 0.5     # range [0.0, 1.0]
    FS = 44100       # sampling rate, Hz, must be integer
    DURATION = 1.0   # in seconds, may be float
    F = 440.0        # sine frequency, Hz, may be float
    """

    # Initalizes List Object (lov = listofvalues)
    lov = arr

    if arr == []:
        for i in range(N):
            lov.append(i*HEIGHT/N)
        random.shuffle(lov)

    pygame.display.set_caption("Sorting Algorithm Visualizer")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True
    paused = False

    while running:

        screen.fill(BLACK)

        events = pygame.event.get()
        eventHandler(screen, events, lov)

        if not paused:
            # Stuff to do only if not paused
            pass

        # Render function, needs screen to pass stuff to and whatever data we deem necessary
        render(screen, lov, -1)

        # This just
        pygame.display.flip()
        pygame.display.update()


# If the module is imported for whatever reason, the main loop won't run
if __name__ == "__main__":
    main([])
