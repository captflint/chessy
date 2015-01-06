def validsquare(filerank):
    if filerank[0] >= 1 and filerank[0] <= 8:
        if filerank[1] >= 1 and filerank[1] <= 8:
            return(True)
        else:
            return(False)
    else:
        return(False)

def square2filerank(square):
    if square[0] == 'a':
        File = 1
    elif square[0] == 'b':
        File = 2
    elif square[0] == 'c':
        File = 3
    elif square[0] == 'd':
        File = 4
    elif square[0] == 'e':
        File = 5
    elif square[0] == 'f':
        File = 6
    elif square[0] == 'g':
        File = 7
    elif square[0] == 'h':
        File = 8
    return((File, int(square[1])))

def filerank2square(filerank):
    return('abcdefgh'[filerank[0] - 1] + str(filerank[1]))

class Piece:
    def __init__(self, File, Rank, color):
        self.File = File
        self.Rank = Rank
        self.color = color
        self.symbol = '?'
        self.kind = 'undefined'
        self.captured = False

    def location(self):
        square = ""
        square += "abcdefgh"[(self.File - 1)]
        square += str(self.Rank)
        return([square, self.symbol])

    def move(self, filerank):
        self.File = filerank[0]
        self.Rank = filerank[1]

    def filerank(self):
        return((self.File, self.Rank))

    def colorchooser(self, whiteblackfilerank):
        if self.color == 'white':
            return(whiteblackfilerank)
        elif self.color == 'black':
            return([whiteblackfilerank[1], whiteblackfilerank[0]])

    def qrb(self, whiteblackfilerank, filedelta, rankdelta):
        fileranks = self.colorchooser(whiteblackfilerank)
        returnmoves = []
        KeepGoing = True
        fileoffset = filedelta
        rankoffset = rankdelta
        while KeepGoing:
            candimove = (self.File + fileoffset, self.Rank + rankoffset)
            if validsquare(candimove):
                if candimove not in fileranks[0]:
                    returnmoves.append(candimove)
                else:
                    KeepGoing = False
                if candimove in fileranks[1]:
                    KeepGoing = False
                fileoffset += filedelta
                rankoffset += rankdelta
            else:
                KeepGoing = False
        return(returnmoves)

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

    def move(self, filerank):
        self.HasMoved = True
        Piece.move(self, filerank)

    def calcmoves(self, whiteblackfilerank):
        fileranks = self.colorchooser(whiteblackfilerank)
        possiblemoves = []
        northmove = (self.File, self.Rank + 1)
        if validsquare(northmove):
            if northmove not in fileranks[0]:
                possiblemoves.append(northmove)
        northeastmove = (self.File + 1, self.Rank + 1)
        if validsquare(northeastmove):
            if northeastmove not in fileranks[0]:
                possiblemoves.append(northeastmove)
        eastmove = (self.File + 1, self.Rank)
        if validsquare(eastmove):
            if eastmove not in fileranks[0]:
                possiblemoves.append(eastmove)
        southeastmove = (self.File + 1, self.Rank - 1)
        if validsquare(southeastmove):
            if southeastmove not in fileranks[0]:
                possiblemoves.append(southeastmove)
        southmove = (self.File, self.Rank - 1)
        if validsquare(southmove):
            if southmove not in fileranks[0]:
                possiblemoves.append(southmove)
        southwestmove = (self.File - 1, self.Rank - 1)
        if validsquare(southwestmove):
            if southwestmove not in fileranks[0]:
                possiblemoves.append(southwestmove)
        westmove = (self.File - 1, self.Rank)
        if validsquare(westmove):
            if westmove not in fileranks[0]:
                possiblemoves.append(westmove)
        northwestmove = (self.File - 1, self.Rank + 1)
        if validsquare(northwestmove):
            if northwestmove not in fileranks[0]:
                possiblemoves.append(northwestmove)
        return(possiblemoves)

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

    def calcmoves(self, whiteblackfilerank):
        possiblemoves = []
        # calculate north moves
        possiblemoves += self.qrb(whiteblackfilerank, 0, 1)
        # calculate northeast moves
        possiblemoves += self.qrb(whiteblackfilerank, 1, 1)
        # calculate east moves
        possiblemoves += self.qrb(whiteblackfilerank, 1, 0)
        # calculate southeast moves
        possiblemoves += self.qrb(whiteblackfilerank, 1, -1)
        # calculate south moves
        possiblemoves += self.qrb(whiteblackfilerank, 0, -1)
        # calculate southwest moves
        possiblemoves += self.qrb(whiteblackfilerank, -1, -1)
        # calculate west moves
        possiblemoves += self.qrb(whiteblackfilerank, -1, 0)
        # calculate northwest moves
        possiblemoves += self.qrb(whiteblackfilerank, -1, 1)
        return(possiblemoves)

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

    def move(self, filerank):
        self.HasMoved = True
        Piece.move(self, filerank)

    def calcmoves(self, whiteblackfilerank):
        possiblemoves = []
        # calculate north moves
        possiblemoves += self.qrb(whiteblackfilerank, 0, 1)
        # calculate east moves
        possiblemoves += self.qrb(whiteblackfilerank, 1, 0)
        # calculate south moves
        possiblemoves += self.qrb(whiteblackfilerank, 0, -1)
        # calculate west moves
        possiblemoves += self.qrb(whiteblackfilerank, -1, 0)
        return(possiblemoves)

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

    def calcmoves(self, whiteblackfilerank):
        possiblemoves = []
        # calculate northeast moves
        possiblemoves += self.qrb(whiteblackfilerank, 1, 1)
        # calculate southeast moves
        possiblemoves += self.qrb(whiteblackfilerank, 1, -1)
        # calculate southwest moves
        possiblemoves += self.qrb(whiteblackfilerank, -1, -1)
        # calculate northwest moves
        possiblemoves += self.qrb(whiteblackfilerank, -1, 1)
        return(possiblemoves)

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

    def calcmoves(self, whiteblackfilerank):
        fileranks = self.colorchooser(whiteblackfilerank)
        possiblemoves = []
        nnemove = (self.File + 1, self.Rank + 2)
        if validsquare(nnemove):
            if nnemove not in fileranks[0]:
                possiblemoves.append(nnemove)
        enemove = (self.File + 2, self.Rank + 1)
        if validsquare(enemove):
            if enemove not in fileranks[0]:
                possiblemoves.append(enemove)
        esemove = (self.File + 2, self.Rank - 1)
        if validsquare(esemove):
            if esemove not in fileranks[0]:
                possiblemoves.append(esemove)
        ssemove = (self.File + 1, self.Rank - 2)
        if validsquare(ssemove):
            if ssemove not in fileranks[0]:
                possiblemoves.append(ssemove)
        sswmove = (self.File - 1, self.Rank - 2)
        if validsquare(sswmove):
            if sswmove not in fileranks[0]:
                possiblemoves.append(sswmove)
        wswmove = (self.File - 2, self.Rank - 1)
        if validsquare(wswmove):
            if wswmove not in fileranks[0]:
                possiblemoves.append(wswmove)
        wnwmove = (self.File - 2, self.Rank + 1)
        if validsquare(wnwmove):
            if wnwmove not in fileranks[0]:
                possiblemoves.append(wnwmove)
        nnwmove = (self.File - 1, self.Rank + 2)
        if validsquare(nnwmove):
            if nnwmove not in fileranks[0]:
                possiblemoves.append(nnwmove)
        return(possiblemoves)

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

    def calcmoves(self, whiteblackfilerank, ep):
        fileranks = self.colorchooser(whiteblackfilerank)
        fileranks[1].append(ep)
        possiblemoves = []
        if self.color == 'white':
            direction = 1
            startrank = 2
        else:
            direction = -1
            startrank = 7
        oneforward = (self.File, self.Rank + direction)
        if oneforward not in fileranks[0]:
            if oneforward not in fileranks[1]:
                possiblemoves.append(oneforward)
        if len(possiblemoves) == 1 and self.Rank == startrank:
            twoforward = (self.File, self.Rank + 2 * direction)
            if twoforward not in fileranks[0]:
                if twoforward not in fileranks[1]:
                    possiblemoves.append(twoforward)
        westcapture = (self.File - 1, self.Rank + direction)
        if westcapture in fileranks[1]:
            possiblemoves.append(westcapture)
        eastcapture = (self.File + 1, self.Rank + direction)
        if eastcapture in fileranks[1]:
            possiblemoves.append(eastcapture)
        return(possiblemoves)

class Board:
    def __init__(self, starting_position):
        if starting_position == "initial":
            self.WhiteToMove = True
            self.plycount = 0
            self.movenumber = 1
            self.BlackCCastle = True
            self.BlackGCastle = True
            self.WhiteCCastle = True
            self.WhiteGCastle = True
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
            self.repititionlist = []

    def piecepositions(self):
        returnlist = []
        for piece in self.pieces:
            returnlist.append(piece.location())
        return(returnlist)
    
    def whiteblackfilerank(self):
        whitefileranks = []
        blackfileranks = []
        for piece in self.pieces:
            if piece.color == 'white':
                whitefileranks.append(piece.filerank())
            elif piece.color == 'black':
                blackfileranks.append(piece.filerank())
        return([whitefileranks, blackfileranks])
