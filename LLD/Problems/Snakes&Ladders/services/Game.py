from collections import deque
from typing import List, Deque

from models.Board import Board
from models.Dice import Dice
from models.Player import Player
from models.GameStatus import GameStatus

class Game:
    def __init__(self, board: Board, dice: Dice) -> None:
        self._board = board
        self._dice = dice
        self._players: Deque[Player] = deque()
        self._status = GameStatus.NOT_STARTED

    def add_players(self, players: List[Player]) -> None:
        if self._status == GameStatus.NOT_STARTED:
            for player in players:
                self._players.append(player)
        else:
            raise "Unable to add players while game is running."
    
    def move_player(self, player: Player):
        currPos = player.position
        diceVal = self._dice.roll()
        targetPos = currPos + diceVal
        if targetPos <= self._board.total_dimension:
            if self._board.has_special_entity(targetPos):
                targetPos = self._board.get_special_entity(targetPos).end
            player.position = targetPos

    def start_game(self):
        self._status = GameStatus.RUNNING

        while len(self._players) > 1:
            currPlayer = self._players.popleft()
            self.move_player(currPlayer)
            if currPlayer.position == self._board.total_dimension:
                print(f"Player {currPlayer._name} has finished the game!")
            else:
                self._players.append(currPlayer)
        
        self._status = GameStatus.FINISHED
    
