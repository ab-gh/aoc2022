from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=5)

def main():
    rows, moves = puzzle.input_data.split("\n\n")

    instructions = [[m[0]] + m[1].split(" to ") for m in [m.split(" from ") for m in [m.split("move ")[1] for m in moves.splitlines()]]]

    stacks = []
    for n, i in enumerate(range(0, len(rows.splitlines()[0])+1, 4)):
        stacks.append([])
        for row in rows.splitlines():
            if (l := row[i+1:i+2]) != ' ':
                stacks[n].append(l)
        stacks[n].pop(-1)

    def move(stacks, qty, frm, to):
        for n in range(0, qty):
            # find letter to move
            frm_lttr = stacks[frm-1][0]
            # remove that letter from the from stack
            stacks[frm-1].pop(0)
            # add it to the front of the to stack
            stacks[to-1].insert(0, frm_lttr)
        return stacks

    for line in instructions:
        stacks = move(stacks, int(line[0]), int(line[1]), int(line[2]))
    return "".join([stack[0] for stack in stacks])

if __name__ == "__main__": print(main())