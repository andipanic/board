#!/usr/bin/python3

###
#Created a ascii board with updateable spots
###

class Board:
    """Create an ascii board with updatable spots"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spots = []
        for y in range(self.height):
            self.spots.append([Spot(x,y) for x in range(self.width)])

    def display(self):
        line = "|"
        print(" " + "".join("_ ") * self.width)
        for y in self.spots:
            for x in y:
                line += "".join(x.char) + "|"
            print(line)
            line="|"

class BoardWithHeader(Board):
    """Creats a board, but with a header! """
    def __init__(self,width, height, header=None):
        super().__init__(width, height)
        self.header = header

    def display(self):
        if self.header:
            print(self.header)
        super().display()

class Location(BoardWithHeader):
    """Creates a board with headers and x:y location attached """
    def __init__(self, width, height, x, y, header="Location: "):
        super().__init__(width, height, header)
        self.x = x
        self.y = y

    def display(self):
        self.header += str(self.x) + ":" + str(self.y)
        super().display()


class Spot:
    """Single character spots on a board"""
    def __init__(self, x, y, char="_"):
        self.x = x
        self.y = y
        self.char = char
        self.occupant = None

    def is_occupied(self):
        if self.occupant is not None:
            return True
        return False

    def occupy(self, occupant):
        if self.occupant is None:
            self.occupant = occupant
            self.char = occupant.char

    def reset(self, char="_"):
        self.char = char
        self.occupant = None

if __name__ == '__main__':
    board = Board(5,5)
    board.display()
    board1 = BoardWithHeader(5,5,"Test!")
    board1.display()
    board2 = Location(5,5,0,0)
    board2.display()
