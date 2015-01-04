def validsquare(filerank):
    if filerank[0] >= 1 and filerank[0] <= 8:
        if filerank[1] >= 1 and filerank[1] <= 8:
            return(True)
        else:
            return(False)
    else:
        return(False)

class Piece:
    def __init__(self, File, Rank, color):
        self.File = File
        self.Rank = Rank
        self.color = color
        self.symbol = '?'
        self.kind = 'undefined'

    def location(self):
        square = ""
        square += "abcdefgh"[(self.File - 1)]
        square += str(self.Rank)
        return([square, self.symbol])

    def move(self, File, Rank):
        self.File = File
        self.Rank = Rank

    def filerank(self):
        return((self.File, self.Rank))

    def __str__(self):
        return(self.color + ' ' + self.kind + ' at ' + self.location()[0])

    def __repr__(self):
        return(self.color + ' ' + self.kind + ' at ' + self.location()[0])

class King(Piece):
    def __init__(self, File, Rank, color, HasMoved):
        Piece.__init__(self, File, Rank, color)
        self.HasMoved = HasMoved
        self.kind = 'king'
        if self.color == 'white':
            self.symbol = 'K'
        elif self.color == 'black':
            self.symbol = 'k'
        else:
            self.symbol = '!'

    def move(self, File, Rank):
        self.HasMoved = True
        Piece.move(self, File, Rank)

class Queen(Piece):
    def __init__(self, File, Rank, color):
        Piece.__init__(self, File, Rank, color)
        self.kind = 'queen'
        if self.color == 'white':
            self.symbol = 'Q'
        elif self.color == 'black':
            self.symbol = 'q'
        else:
            self.symbol = '!'

class Rook(Piece):
    def __init__(self, File, Rank, color, HasMoved):
        Piece.__init__(self, File, Rank, color)
        self.kind = 'rook'
        self.HasMoved = HasMoved
        if self.color == 'white':
            self.symbol = 'R'
        elif self.color == 'black':
            self.symbol = 'r'
        else:
            self.symbol = '!'

    def move(self, File, Rank):
        self.HasMoved = True
        Piece.move(self, File, Rank)

class Bishop(Piece):
    def __init__(self, File, Rank, color):
        Piece.__init__(self, File, Rank, color)
        self.kind = 'bishop'
        if self.color == 'white':
            self.symbol = 'B'
        elif self.color == 'black':
            self.symbol = 'b'
        else:
            self.symbol = '!'

class Knight(Piece):
    def __init__(self, File, Rank, color):
        Piece.__init__(self, File, Rank, color)
        self.kind = 'knight'
        if self.color == 'white':
            self.symbol = 'N'
        elif self.color == 'black':
            self.symbol = 'n'
        else:
            self.symbol = '!'

class Pawn(Piece):
    def __init__(self, File, Rank, color):
        Piece.__init__(self, File, Rank, color)
        self.kind = 'pawn'
        if self.color == 'white':
            self.symbol = 'P'
        elif self.color == 'black':
            self.symbol = 'p'
        else:
            self.symbol = '!'

class Board:
    def __init__(self, starting_position):
        if starting_position == "initial":
            self.pieces = []
            p =  King(5, 1, 'white', False)
            self.pieces.append(p)
            p =  Queen(4, 1, 'white')
            self.pieces.append(p)
            p =  Rook(1, 1, 'white', False)
            self.pieces.append(p)
            p =  Rook(8, 1, 'white', False)
            self.pieces.append(p)
            p =  Bishop(3, 1, 'white')
            self.pieces.append(p)
            p =  Bishop(6, 1, 'white')
            self.pieces.append(p)
            p =  Knight(2, 1, 'white')
            self.pieces.append(p)
            p =  Knight(7, 1, 'white')
            self.pieces.append(p)
            for number in range(1, 9):
                p =  Pawn(number, 2, 'white')
                self.pieces.append(p)
            p =  King(5, 8, 'black', False)
            self.pieces.append(p)
            p =  Queen(4, 8, 'black')
            self.pieces.append(p)
            p =  Rook(1, 8, 'black', False)
            self.pieces.append(p)
            p =  Rook(8, 8, 'black', False)
            self.pieces.append(p)
            p =  Bishop(3, 8, 'black')
            self.pieces.append(p)
            p =  Bishop(6, 8, 'black')
            self.pieces.append(p)
            p =  Knight(2, 8, 'black')
            self.pieces.append(p)
            p =  Knight(7, 8, 'black')
            self.pieces.append(p)
            for number in range(1, 9):
                p =  Pawn(number, 7, 'black')
                self.pieces.append(p)

    def piecepositions(self):
        returnlist = []
        for piece in self.pieces:
            returnlist.append(piece.location())
        return(returnlist)
    
