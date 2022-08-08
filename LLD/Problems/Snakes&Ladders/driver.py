from models.Board import Board
from models.Snake import Snake
from models.Ladder import Ladder
from models.Player import Player
from models.Dice import Dice
from services.Game import Game



snake1 = Snake(99,10)
snake2 = Snake(84,65)
snake3 = Snake(75,35)
snake4 = Snake(66,23)
snake5 = Snake(24,12)
snake6 = Snake(18,3)

ladder1 = Ladder(7,21)
ladder2 = Ladder(19,89)
ladder3 = Ladder(27,83)
ladder4 = Ladder(31,78)
ladder5 = Ladder(47,68)
ladder6 = Ladder(57,87)
ladder7 = Ladder(76,98)

board = Board(10)
board.add_special_entity(snake1)
board.add_special_entity(snake2)
board.add_special_entity(snake3)
board.add_special_entity(snake4)
board.add_special_entity(snake5)
board.add_special_entity(snake6)

board.add_special_entity(ladder1)
board.add_special_entity(ladder2)
board.add_special_entity(ladder3)
board.add_special_entity(ladder4)
board.add_special_entity(ladder5)
board.add_special_entity(ladder6)
board.add_special_entity(ladder7)

dice = Dice(6)

game = Game(board, dice)

players = []
players.append(Player('Pawan'))
players.append(Player('Abhinav'))
players.append(Player('Gyan'))
players.append(Player('Divyank'))

game.add_players(players)

game.start_game()