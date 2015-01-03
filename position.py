files = "abcdefgh"
ranks = "87654321"
renderorder = []

for number in ranks:
    for letter in files:
        renderorder.append(letter + number)

lightsquares = []
rowcounter = 0
rowfliper = True

for square in renderorder:
    if rowfliper:
        if rowcounter % 2 == 0:
            lightsquares.append(square)
    else:
        if rowcounter % 2 != 0:
            lightsquares.append(square)
    rowcounter += 1
    if rowcounter % 8 == 0:
        rowfliper = not rowfliper

def printboard():
    print("\n\n\n")
    eightcounter = 0
    rankstr = ""
    for square in renderorder:
        if square in lightsquares:
            rankstr += '='
        else:
            rankstr += '-'
        eightcounter += 1
        if eightcounter % 8 == 0:
            print(rankstr)
            rankstr = ""

printboard()
