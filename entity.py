#!/usr/bin/python3

class Entity:
    """Basic Entity with character representation
    x and y coordinates and a board"""
    def __init__(self, x=0,y=0, char=None, board=None):
        self.x = x
        self.y = y
        self.char = char
        self.board = board

    def get_spot(self, x, y):
        if x is None and y is None:
            x = self.x
            y = self.y
        return self.board.spots[y][x]

    def place(self, x, y):
        spot = self.get_spot(x,y)
        spot.occupy(self)

    def can_place(self, x, y):
        spot = self.get_spot(x,y)
        if not spot.is_occupied():
            return True
        return False

    def __call__(self):
        self.place(self.x,self.y)

def main():
    from board import Board
    board = Board(20,20)
    a = Entity(10,10,"A",board)
    b = Entity(15,15,"B",board)
    a()
    b()
    board.display()
    a.place(15,15)
    board.display()

if __name__ == '__main__':
    main()
