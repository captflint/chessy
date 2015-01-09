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
    def __init__(self, starting_position, chess960=False):
        self.chess960 = chess960
        if starting_position == "initial" and not chess960:
            self.WhiteToMove = True
            self.plycount = 0
            self.movenumber = 1
            self.BlackWestCastle = True
            self.BlackEastCastle = True
            self.WhiteWestCastle = True
            self.WhiteEastCastle = True
            self.enpasant = (0, 0)
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
            self.legalmoves = self.getlegalmoves()

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

    def getoneplymoves(self, hypoposition='', colortomove=''):
        position = self.whiteblackfilerank()
        if len(hypoposition) > 0:
            position = hypoposition
        ep = (0, 0)
        oneplymoves = []
        if len(colortomove) == 0:
            ep = self.enpasant
            if self.WhiteToMove:
                colortomove = 'white'
            else:
                colortomove = 'black'
        for piece in self.pieces:
            if piece.color == colortomove:
                origin = (piece.File, piece.Rank)
                if piece.kind == 'pawn':
                    destinations = piece.calcmoves(position, ep)
                else:
                    destinations = piece.calcmoves(position)
                if len(destinations) > 0:
                    oneplymoves.append([origin, destinations])
        return(oneplymoves)

    def getcastlemoves(self):
        castlemoves = []
        if self.WhiteToMove:
            colortomove = 'white'
            attackcolor = 'black'
            castlerank = 1
            eastcastle = self.WhiteEastCastle
            westcastle = self.WhiteWestCastle
        else:
            colortomove = 'black'
            attackcolor = 'white'
            castlerank = 8
            eastcastle = self.BlackEastCastle
            westcastle = self.BlackWestCastle
        if eastcastle or westcastle:
            attackedsquares = []
            for piecemoves in self.getoneplymoves(colortomove=attackcolor):
                attackedsquares += piecemoves[1]
            for piece in self.pieces:
                if piece.kind == 'king' and piece.color == colortomove:
                    king = piece
            if king.HasMoved:
                eastcastle = False
                westcastle = False
                if self.WhiteToMove:
                    self.WhiteEastCastle = False
                    self.WhiteWestCastle = False
                else:
                    self.BlackEastCastle = False
                    self.BlackWestCastle = False
                return("")
            for piece in self.pieces:
                if eastcastle:
                    if piece.kind == 'rook' and piece.color == colortomove:
                        if piece.File < king.File:
                            eastrook = piece
                if westcastle:
                    if piece.kind == 'rook' and piece.color == colortomove:
                        if piece.File > king.File:
                            westrook = piece
            if eastrook.HasMoved:
                eastcastle = False
                if self.WhiteToMove:
                    self.WhiteEastCastle = False
                else:
                    self.BlackEastCastle = False
            if westrook.HasMoved:
                westcastle = False
                if self.WhiteToMove:
                    self.WhiteWestCastle = False
                else:
                    self.BlackWestCastle = False
            if eastcastle:
                allowedpieces = [king.filerank(), eastrook.filerank()]
                kingpath = []
                rookpath = []
                if king.filerank() == (3, castlerank):
                    kingpath.append(king.filerank())
                if len(kingpath) == 0:
                    if king.File > 3:
                        pathrange = range(3, king.File + 1)
                    else:
                        pathrange = range(king.File, 4)
                    for filenumber in pathrange:
                        kingpath.append((filenumber, castlerank))
                if eastrook.filerank() == (4, castlerank):
                    rookpath.append(eastrook.filerank())
                if len(rookpath) == 0:
                    if eastrook.File > 4:
                        pathrange = range(4, eastrook.File + 1)
                    else:
                        pathrange = range(eastrook.File, 5)
                    for filenumber in pathrange:
                        rookpath.append((filenumber, castlerank))
                keepgoing = True
                for path in [kingpath, rookpath]:
                    for piece in self.pieces:
                        if piece.filerank() in path and piece not in allowedpieces:
                            keepgoing = False
                if keepgoing:
                    for square in kingpath:
                        if square in attackedsquares:
                            keepgoing = False
                if keepgoing:
                    if self.chess960:
                        cmove = filerank2square(king.filerank())
                        cmove += filerank2square(eastrook.filerank())
                        castlemoves.append(cmove)
                    else:
                        castlemoves.append('e1c1')
            if westcastle:
                allowedpieces = [king.filerank(), westrook.filerank()]
                kingpath = []
                rookpath = []
                if king.filerank() == (7, castlerank):
                    kingpath.append(king.filerank())
                if len(kingpath) == 0:
                    if king.File > 7:
                        pathrange = range(1, king.File + 1)
                    else:
                        pathrange = range(king.File, 8)
                    for filenumber in pathrange:
                        kingpath.append((filenumber, castlerank))
                if westrook.filerank() == (6, castlerank):
                    rookpath.append(westrook.filerank())
                if len(rookpath) == 0:
                    if westrook.File > 6:
                        pathrange = range(6, westrook.File + 1)
                    else:
                        pathrange = range(westrook.File, 7)
                    for filenumber in pathrange:
                        rookpath.append((filenumber, castlerank))
                keepgoing = True
                for path in [kingpath, rookpath]:
                    for piece in self.pieces:
                        if piece.filerank() in path and piece not in allowedpieces:
                            keepgoing = False
                if keepgoing:
                    for square in kingpath:
                        if square in attackedsquares:
                            keepgoing = False
                if keepgoing:
                    if self.chess960:
                        cmove = filerank2square(king.filerank())
                        cmove += filerank2square(westrook.filerank())
                        castlemoves.append(cmove)
                    else:
                        castlemoves.append('e1g1')
            return(castlemoves)
        else:
            return([])

    def gametermination(state):
        pass

    def getlegalmoves(self):
        if self.WhiteToMove:
            colortomove = 'white'
            attackcolor = 'black'
        else:
            colortomove = 'black'
            attackcolor = 'white'
        legalmoves = []
        candimoves = self.getoneplymoves()
        position = self.piecepositions()
        for piece in self.pieces:
            if piece.kind == 'king' and piece.color == colortomove:
                kingfilerank = piece.filerank()
        if self.WhiteToMove:
            movingpieces = position[0]
            replypieces = position[1]
        else:
            movingpieces = position[1]
            replypieces = position[0]
        for moveset in candimoves:
            origin = filerank2square(moveset[0])
            for move in moveset[1]:
                hypoposition = []
                for p in movingpieces:
                    if p == moveset[0]:
                        hypoposition.append(move)
                    else:
                        hypoposition.append(p)
                if self.WhiteToMove:
                    replymoves = self.getoneplymoves(hypoposition=[hypoposition, replypieces], colortomove=attackcolor)
                else:
                    replymoves = self.getoneplymoves(hypoposition=[replypieces, hypoposition], colortomove=attackcolor)
                if kingfilerank not in replymoves:
                    legalmoves.append(origin + filerank2square(move))
        legalmoves += self.getcastlemoves()
        return(legalmoves)
