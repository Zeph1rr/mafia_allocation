import json
import os
import random
from typing import List


class Allocator:
    def __init__(self, players: List[str], tournament: str):
        if len(players) % 10 != 0:
            raise ValueError("len(players) % 10 != 0")
        self.players = players
        self.tournament = tournament

    def ot_get_allocation_once(self) -> List[str]:
        shuffled_players = self.players.copy()
        random.shuffle(shuffled_players)
        return shuffled_players

    def ot_get_allocation_for_all_games(self, games_count: int) -> dict[int, List[str]]:
        result = {}
        for i in range(1, games_count + 1):
            result[i] = self.ot_get_allocation_once()
        return result

    def dump_allocation(self, allocation: dict[int, List[str]]):
        allocation_data = ""
        for game in allocation.keys():
            allocation_data += "=" * 3 + f"Игра #{game} " + "=" * 3 + "\n" * 2
            for index, player in enumerate(allocation[game]):
                allocation_data += f"{index + 1}. {player}" + '\n'
            allocation_data += '\n'
        try:
            with open(os.path.join("result", f"{self.tournament}.txt"), "w", encoding='UTF-8') as file:
                file.write(allocation_data)
        except FileNotFoundError:
            os.mkdir("result")
            self.dump_allocation(allocation)
