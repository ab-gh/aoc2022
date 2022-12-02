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
        case "X": #r
            return 1
        case "Y": #p
            return 2
        case "Z": #s
            return 3
        
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
        opp, you = line.split(" ")
        round_won = win(to_num(opp), to_num(you))
        scores.append(to_score(round_won) + to_num(you))
    print(sum(scores))


if __name__ == "__main__":
    main()