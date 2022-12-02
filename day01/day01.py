from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=1)
def main(): #split list by \n\n for arrays of elves, split arrays of elves by \n into individual calorie counts, then sum, sort, head, and sum
    return sum(sorted([sum(list(map(int, a.split("\n")))) for a in puzzle.input_data.split("\n\n")], reverse=True)[:int(input("Number of elves to count for calories: "))])  
if __name__ == "__main__": print(main())