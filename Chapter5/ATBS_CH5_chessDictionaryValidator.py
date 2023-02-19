pieces = {}

def isValidChessBoard(pieces):
    if 'bking' or 'wking' not in pieces:
        return False
    if len(pieces) > 16:
        return False
print(isValidChessBoard(pieces))
