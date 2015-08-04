#!/usr/bin/python3

from board import Board
from getch import getch
import os

class Entity:
    def __init__(self, x, y, char=None, board=None):
        self.x = x
        self.y = y
        self.char = char
        self.board = board

    def get_spot(self):
        spot = self.board.spots[self.y][self.x]
        return spot

    def place(self, x, y):
        spot = self.board.spots[y][x]
        spot.occupy(self)

    def can_place(self, x, y):
        spot = self.board.spots[y][x]
        if not spot.is_occupied():
            return True
        return False

    def move_direction(self, direction):
        current_spot = self.get_spot()
        current_spot.reset(".")
        directions = { 'north': (0,-1),
                       'east':  (1,0),
                       'south': (0,1),
                       'west':  (-1,0) }
        move_x, move_y = directions[direction]
        if self.can_place(self.x + move_x, self.y + move_y):
            self.x += move_x
            self.y += move_y
        self.place(self.x, self.y)

    def __call__(self):
        self.place(self.x,self.y)

def main():
    board = Board(30,30)
    a = Entity( 20, 20, "A", board)
    b = Entity( 15, 15, "B", board)
    a()
    b()
    os.system('clear')
    board.display()
    print("[ w:up a:left s:down d:right q:quit ]")
    print("[ A:you .:travelled _:untravelled x:" + str(a.x) + " y:" + str(a.y) + " ]")

    while True:
        key = getch()
        if key == 'w':
            a.move_direction('north')
        if key == 'a':
            a.move_direction('west')
        if key == 's':
            a.move_direction('south')
        if key == 'd':
            a.move_direction('east')
        if key == 'q':
            break
        os.system('clear')
        board.display()
        print("[ w:up a:left s:down d:right q:quit ]")
        print("[ A:you .:travelled _:untravelled x:" + str(a.x) + " y:" + str(a.y) + " ]")

if __name__ == '__main__':
    main()

