"""
This is the main driver file. It will be responsible for handling user input and displaying the current GameState object
"""

import pygame as p
import ChessEngine

p.init()
WIDTH = HEIGHT = 512  # 400 is another option
DIMENSION = 8  # dimension of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animation later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''


def loadImages():
    pieces = ['bR', 'bN', 'bB', 'bQ', 'bK', 'wQ', 'wK',
              'wB', 'wN', 'wR', 'bp', 'wp']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: we can access an image by saying 'IMAGES['wp']'


'''
The main driver for our code. This will handle user input and updating the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()  #Only do this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            drawGameState(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()


'''
Responsible for all the graphic within a current game state
'''


def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares on the board
    # add 
    drawPieces(screen, gs.board)  # draw pieces on top of those

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the piece on the board using the current GameState.board
'''


def drawPieces(screen, board):
    pass


if __name__ == "__main__":
    main()
