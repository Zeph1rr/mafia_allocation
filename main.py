import argparse
from typing import List

from mafia_allocation import Allocator


def parse_file(filepath: str) -> List[str]:
    with open(filepath, encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) % 10 != 0:
            raise ValueError("Количество игроков должно быть кратно 10")
        result = []
        for line in lines:
            result.append(line.replace("\n", ""))
    return result


def get_players_from_stdin():
    players_count = int(input("Количество игроков: "))
    while players_count % 10 != 0:
        players_count = int(
            input("Количество игроков должно быть кратно 10! Количество игроков: ")
        )
    return [input(f"Player #{i + 1}: ") for i in range(players_count)]


def main():
    parser = argparse.ArgumentParser(
        description="Get allocations for mafia tournaments"
    )
    parser.add_argument(
        "-f", "--file", required=False, help="Path to file with players"
    )
    parser.add_argument(
        "-c",
        "--game-count",
        type=int,
        required=False,
        help="Count of games in tournament",
    )
    parser.add_argument(
        "-n", "--tournament-name", required=False, help="Name of tournament"
    )
    args = parser.parse_args()

    players = parse_file(args.file) if args.file else get_players_from_stdin()
    games_count = args.game_count if args.game_count else int(input("Количество игр: "))
    tournament_name = (
        args.tournament_name if args.tournament_name else input("Название турнира: ")
    )

    allocator = Allocator(players, tournament_name)
    allocation = allocator.get_allocation_for_all_games(games_count)
    print(allocator.dump_allocation(allocation))


if __name__ == "__main__":
    main()
