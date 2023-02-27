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
        try:
            with open(os.path.join("result", f"{self.tournament}.txt"), "w") as file:
                json.dump(allocation, file, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            os.mkdir("result")
            self.dump_allocation(allocation)
