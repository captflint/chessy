import asciiboard as ab
import lawsofchess as lc

board = lc.Board('initial')
print(len(board.pieces))
ab.printboard(board.piecepositions())
for move in board.legalmoves:
    print(move)
print(len(board.legalmoves))
