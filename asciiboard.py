files = "abcdefgh"
ranks = "87654321"
whiteorder = []
for number in ranks:
    for letter in files:
        whiteorder.append(letter + number)

blackorder = []
for square in whiteorder:
    blackorder.append(square)
blackorder.reverse()

flipboard = False

lightsquares = []
rowcounter = 0
rowfliper = True

for square in whiteorder:
    if rowfliper:
        if rowcounter % 2 == 0:
            lightsquares.append(square)
    else:
        if rowcounter % 2 != 0:
            lightsquares.append(square)
    rowcounter += 1
    if rowcounter % 8 == 0:
        rowfliper = not rowfliper

def printboard(piecelist):
    if flipboard:
        renderorder = blackorder
    else:
        renderorder = whiteorder
    rankstr = ""
    for square in renderorder:
        emptysquare = True
        for piece in piecelist:
            if square == piece[0]:
                rankstr += piece[1]
                emptysquare = False
                if len(rankstr) == 8:
                    print(rankstr)
                    rankstr = ""
        if emptysquare:
            if square in lightsquares:
                rankstr += '='
            else:
                rankstr += '-'
            if len(rankstr) == 8:
                print(rankstr)
                rankstr = ""

def fancyboard(piecelist):
    fancypieces = [
        ('K', '♔'),
        ('Q', '♕'),
        ('R', '♖'),
        ('B', '♗'),
        ('N', '♘'),
        ('P', '♙'),
        ('k', '♚'),
        ('q', '♛'),
        ('r', '♜'),
        ('b', '♝'),
        ('n', '♞'),
        ('p', '♟')]
    fancylist = []
    for piece in piecelist:
        square = piece[0]
        for pair in fancypieces:
            if pair[0] == piece[1]:
                symbol = pair[1]
        fancylist.append((square, symbol))
    printboard(fancylist)

initialposition = [
    ("a1", "R"),
    ("b1", "N"),
    ("c1", "B"),
    ("d1", "Q"),
    ("e1", "K"),
    ("f1", "B"),
    ("g1", "N"),
    ("h1", "R"),
    ("a8", "r"),
    ("b8", "n"),
    ("c8", "b"),
    ("d8", "q"),
    ("e8", "k"),
    ("f8", "b"),
    ("g8", "n"),
    ("h8", "r"),
    ("a2", "P"),
    ("b2", "P"),
    ("c2", "P"),
    ("d2", "P"),
    ("e2", "P"),
    ("f2", "P"),
    ("g2", "P"),
    ("h2", "P"),
    ("a7", "p"),
    ("b7", "p"),
    ("c7", "p"),
    ("d7", "p"),
    ("e7", "p"),
    ("f7", "p"),
    ("g7", "p"),
    ("h7", "p")]


