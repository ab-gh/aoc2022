from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=2)

def win(opponent, you):
    return (opponent - you) % 3

def to_num(letter):
    match letter:
        case "A": #r
            return 1
        case "B": #p
            return 2
        case "C": #s
            return 3
        case "X": # lose
            return 1
        case "Y": # draw
            return 0
        case "Z": # win
            return 2
        
def to_score(wld):
    match wld:
        case 2: #win
            return 6
        case 1: #loss
            return 0
        case 0: #draw
            return 3
        
def main():
    scores = []
    for line in puzzle.input_data.splitlines():
        opp, outcome = line.split(" ")
        for choice in ["A", "B", "C"]:
            outcome_of_game = win(to_num(opp), to_num(choice))
            outcome_looking_for = to_num(outcome)
            if outcome_looking_for == outcome_of_game:
                scores.append(to_score(win(to_num(opp), to_num(choice))) + to_num(choice))
    print(sum(scores))


if __name__ == "__main__":
    main()