# Knots and Crosses -- Tic-Tac-Toe.
# Author: Paul Delaney
# 6th January 2021

import numpy as np
import pygame
import sys
import math

# Global variables + RGB values

ROW_COUNT = 3
COLUMN_COUNT = 3
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


def gameboard(r, c):
    # This function creates our game board.
    board = np.zeros((r, c))
    return board


def take_turn(board, row, col, piece):
    # This function places an "X" or and "O"
    board[row][col] = piece
    return board


def valid_turn(board, row, column, piece):
    # This function ensures that the position selected is free to use
    if board[row][column] == 0:
        return True


def winning_move(board, piece):
    # Check for vertical winning move

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 2):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece:
                pygame.draw.line(screen, BLACK, (c * SQUARESIZE + 0.5 * SQUARESIZE, 0.5 * SQUARESIZE)
                                 , (c * SQUARESIZE + 0.5 * SQUARESIZE, 2.5 * SQUARESIZE), 3)
                pygame.display.update()
                return True

    # Check for horizontal winning move

    for c in range(COLUMN_COUNT - 2):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece:
                pygame.draw.line(screen, BLACK, (0.5 * SQUARESIZE, r * SQUARESIZE + 0.5 * SQUARESIZE)
                                 , (2.5 * SQUARESIZE, r * SQUARESIZE + 0.5 * SQUARESIZE), 3)
                pygame.display.update()
                return True

    # Check the negative slope diagonal

    for c in range(COLUMN_COUNT - 2):
        if board[c][c] == piece and board[c + 1][c + 1] == piece and board[c + 2][c + 2] == piece:
            pygame.draw.line(screen, BLACK, (0.5 * SQUARESIZE, 0.5 * SQUARESIZE)
                             , (2.5 * SQUARESIZE, 2.5 * SQUARESIZE), 3)
            pygame.display.update()
            return True

    # Check the positive slope diagonal

    for c in range(COLUMN_COUNT - 2):
        if board[c + 2][c] == piece and board[c + 1][c + 1] == piece and board[c][c + 2] == piece:
            pygame.draw.line(screen, BLACK, (0.5 * SQUARESIZE, 2.5 * SQUARESIZE)
                             , (2.5 * SQUARESIZE, 0.5 * SQUARESIZE), 3)
            pygame.display.update()
            return True


def drawboard(board):
    # Draws our inital game board
    for c in range(1, COLUMN_COUNT):
        pygame.draw.line(screen, BLACK, (c * SQUARESIZE, 10), (c * SQUARESIZE, 290), 2)
        pygame.draw.line(screen, BLACK, (10, c * SQUARESIZE), (290, c * SQUARESIZE), 2)

    # Updates game board with "X" and "O" as players make their moves.
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, BLUE, ((c + 0.5) * SQUARESIZE, (r + 0.5) * SQUARESIZE), RADIUS, 2)
            elif board[r][c] == 2:
                pygame.draw.line(screen, RED, (c * SQUARESIZE + 15, r * SQUARESIZE + 15),
                                 (c * SQUARESIZE + 85, r * SQUARESIZE + 85), 2)
                pygame.draw.line(screen, RED, (c * SQUARESIZE + 85, r * SQUARESIZE + 15),
                                 (c * SQUARESIZE + 15, r * SQUARESIZE + 85), 2)

    pygame.display.update()

# Create Game Board
board = gameboard(ROW_COUNT, COLUMN_COUNT)
game_over = False
turn = 0

# Initialise pygame

pygame.init()  # Initialises Pygame

SQUARESIZE = 100
height = ROW_COUNT * SQUARESIZE
width = COLUMN_COUNT * SQUARESIZE
RADIUS = SQUARESIZE * 0.5 - 20


size = (width, height)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)

drawboard(board)
pygame.display.update()  # Creates Pygame board

while not game_over:

    # Ensures Pygame can be exited correctly
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Player 1 turn
    if event.type == pygame.MOUSEBUTTONDOWN:

        if turn == 0:
            xpos = event.pos[0]
            ypos = event.pos[1]
            row = int(math.floor(ypos / SQUARESIZE))
            col = int(math.floor(xpos / SQUARESIZE))

            if valid_turn(board, row, col, 1):
                take_turn(board, row, col, 1)
                drawboard(board)
                turn += 1
                turn = turn % 2

            if winning_move(board, 1):
                game_over = True


        # Player 2 turn

        else:
            xpos = event.pos[0]
            ypos = event.pos[1]
            row = int(math.floor(ypos / SQUARESIZE))
            col = int(math.floor(xpos / SQUARESIZE))

            if valid_turn(board, row, col, 2):
                take_turn(board, row, col, 2)
                drawboard(board)
                turn += 1
                turn = turn % 2

            if winning_move(board, 2):
                game_over = True

        if game_over == True:
            pygame.time.wait(3000)
