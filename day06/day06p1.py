from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=6)
def main():
    return [i+1 for i in range(3, len(puzzle.input_data)) if len(list(puzzle.input_data[i-3:i+1])) == len(set(puzzle.input_data[i-3:i+1]))][0]
if __name__ == "__main__": print(main())