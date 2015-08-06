#!/usr/bin/python3

import random
import string
import os
import time
from board import Board
from colorama import init, Fore, Back, Style
init(autoreset=True)

def color(text, color):
    c = color.upper()
    result = getattr(Fore, c) + text + Fore.RESET
    return result

class Entity:
    def __init__(self,character,board=None): 
        self.character = character
        self.board = board
        self.x,self.y = self.get_random_spot()

    def place(self, x, y):
        spot = self.board.spots[y][x]
        spot.character = self.character

    def get_valid_moves(self, x, y):
        moves = set()
        for move_x in range(-1,2):
            for move_y in range(-1,2):
                new_x = move_x + x
                new_y = move_y + y
                if new_x < self.board.width and \
                new_y < self.board.height and \
                new_x >= 0 and new_y >= 0:
                    moves.add((move_x+x,move_y+y))
        return moves

    def move_random(self, reset=","):
        current_spot = self.get_spot() 
        current_spot.reset(reset)
        possible_moves = self.get_valid_moves(self.x,self.y)
        move = random.sample(possible_moves,1)[0]
        self.x,self.y = move
        self.place(self.x, self.y)

    def get_spot(self):
        spot = self.board.spots[self.y][self.x]
        return spot

    def get_random_spot(self):
        spots = set((x,y) for x in range(0,self.board.width -1)
                            for y in range(0,self.board.height -1))
        spot = random.sample(spots,1)[0]
        return spot

    def __call__(self):
        self.place(self.x,self.y)

if __name__ == '__main__':
    picture = 0
    while picture <= 1000000000:
        board = Board(104,55)
        a = b = c = d = e = f = g = Entity("_",board)
        a()
        b()
        c()
        d()
        e()
        f()
        g()
        count = 0
        colors = {"BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE", "RESET"}
        junk = string.punctuation + string.ascii_letters + " "
        a.color = random.sample(colors,1)[0]
        a.character = random.choice(junk)
        b.color = random.sample(colors,1)[0]
        b.character = random.choice(junk)
        c.color = random.sample(colors,1)[0]
        c.character = random.choice(junk)
        d.color = random.sample(colors,1)[0]
        d.character = random.choice(junk)
        e.color = random.sample(colors,1)[0]
        e.character = random.choice(junk)
        f.color = random.sample(colors,1)[0]
        f.character = random.choice(junk)
        g.color = random.sample(colors,1)[0]
        g.character = random.choice(junk)
        while count <= 1500:
            a.move_random(color(a.character,a.color))
            b.move_random(color(b.character,b.color))
            c.move_random(color(c.character,c.color))
            d.move_random(color(d.character,d.color))
            e.move_random(color(e.character,e.color))
            f.move_random(color(f.character,f.color))
            g.move_random(color(g.character,g.color))
            count_d = "Count: " + str(count)
            vma = "Valid Moves A: " + str(a.get_valid_moves(a.x,a.y))
            vmb = "Valid Moves B: " + str(b.get_valid_moves(b.x,b.y))
            vmc = "Valid Moves C: " + str(c.get_valid_moves(c.x,c.y))
            vmd = "Valid Moves D: " + str(d.get_valid_moves(d.x,d.y))
            #os.system('clear')
            #board.display()
            #print(count_d + "\n" + vma + "\n" + vmb +"\n" + vmc + "\n" + vmd)
            #print(junk)
            count+=1
            #time.sleep(.1)
        count = 0
        picture += 1
        os.system('clear')
        board.display()
        time.sleep(1)
    #print(count_d + "\n" + vma + "\n" + vmb +"\n" + vmc + "\n" + vmd)

