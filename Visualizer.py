from heapq import merge
from tkinter import W
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
numofvals = WIDTH//2


def issorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]):  # i is the index of the previous element
            return False
    return True


def nextlov(screen, lov, name):
    if name == "bubble":
        bubblesort(screen, lov)
    elif name == "insertion":
        insertionSort(screen, lov)
    elif name == "shell":
        shellSort(screen, lov)
    elif name == "radix":
        radixSort(screen, lov)
    elif name == "bogo":
        bogosort(screen, lov)
    return lov


def bubblesort(screen, lov):
    for i in range(len(lov)):
        for j in range(0, len(lov) - i - 1):
            if lov[j] > lov[j + 1]:
                temp = lov[j]
                lov[j] = lov[j+1]
                lov[j+1] = temp

            render(screen, lov, [lov[numofvals-i-1], lov[j+1]])

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return None
            eventHandler(screen, events, lov)


def insertionSort(screen, lov):
    for i in range(1, len(lov)):
        key = lov[i]
        j = i-1
        while j >= 0 and key < lov[j]:
            lov[j + 1] = lov[j]
            j -= 1

            render(screen, lov, [lov[i], lov[j]])

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return None
            eventHandler(screen, events, lov)
        lov[j + 1] = key


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

                render(screen, lov, [lov[j], lov[i]])

                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            return None
                eventHandler(screen, events, lov)

            lov[j] = temp
        interval //= 2


def countingSort(screen, array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[int(index % 10)] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[int(index % 10)] - 1] = array[i]
        count[int(index % 10)] -= 1
        i -= 1
        render(screen, output, [array[i]])
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main[array]
        eventHandler(screen, events, array)

    for i in range(0, size):
        array[i] = output[i]
        render(screen, array, [array[i]])
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main[array]
        eventHandler(screen, events, array)


# Main function to implement radix sort
def radixSort(screen, array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(screen, array, place)
        place *= 10
        render(screen, array, [-1])

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return None
        eventHandler(screen, events, array)


def bogosort(screen, lov):
    n = 0
    while not issorted(lov):
        n += 1
        print(n)
        random.shuffle(lov)

        render(screen, lov, [random.randint(0, numofvals-1)*HEIGHT/numofvals])
        time.sleep(0.1)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return None
        eventHandler(screen, events, lov)

    print("DONE WITH ONLY", n, "ITERATIONS")
    print("-------------------------------")


def render(screen, lov, h):
    i = 0
    screen.fill(BLACK)
    for v in lov:
        if v in h:
            pygame.draw.rect(screen, RED, pygame.Rect(
                i * WIDTH/numofvals, HEIGHT - v - HEIGHT/numofvals+3, WIDTH/numofvals+1, v + HEIGHT/numofvals))
        else:
            pygame.draw.rect(screen, WHITE, pygame.Rect(
                i * WIDTH/numofvals, HEIGHT - v - HEIGHT/numofvals+3, WIDTH/numofvals+1, v + HEIGHT/numofvals))
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
            if event.key == pygame.K_4:
                nextlov(screen, lov, "radix")
            if event.key == pygame.K_5:
                pass
            if event.key == pygame.K_6:
                pass
            if event.key == pygame.K_7:
                pass
            if event.key == pygame.K_8:
                pass
            if event.key == pygame.K_9:
                pass
            if event.key == pygame.K_0:
                nextlov(screen, lov, "bogo")
            if event.key == pygame.K_r:
                random.shuffle(lov)
                main(lov)
            if event.key == pygame.K_SPACE:
                render(screen, lov, [-1])
                main(lov)

            global numofvals
            if event.key == pygame.K_EQUALS:
                numofvals += 1
                lov = populate(numofvals)
                main(lov)
            if event.key == pygame.K_MINUS:
                numofvals -= 1
                lov = populate(numofvals)
                main(lov)
            if event.key == pygame.K_ESCAPE:
                sys.exit()


def populate(n):
    lov = []
    for i in range(n):
        lov.append(i*HEIGHT/n)
    random.shuffle(lov)
    return lov


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
        lov = populate(numofvals)

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
        render(screen, lov, [-1])

        # This just
        pygame.display.flip()
        pygame.display.update()


# If the module is imported for whatever reason, the main loop won't run
if __name__ == "__main__":
    main([])
