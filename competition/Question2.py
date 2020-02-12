
def findJumpsForVal(grid: list, val: int) -> list:
    # Find all xy combinations that multiply to val
    for r in range(len(grid)):
        for c in range(len(grid[0])):

            # Check if it is a factor
            if (r+1)*(c+1) == val:
                yield (r, c)


# Read the number of lines
line_count = int(input(""))

# We don't need the second input
input("")

# Read all rows of the grid
grid: list = []
while len(grid) < line_count:
    # Add row to the grid
    grid.append([int(i) for i in input("").strip().split(" ")])

# Define a tasks queue for jumps and tracker for visited points
tasks: list = []
seen = set()

# Push the first position to the tasks list
tasks.append((0, 0, grid[0][0]))


# Handle tasks running
while len(tasks) > 0:

    # Pop the first task off the stack
    task: dict
    try:
        task = tasks.pop(0)
    except IndexError as e:
        break

    # Check all jumps
    for jump in findJumpsForVal(grid, task[2]):

        # Jump not valid if we have been there before
        if (jump in seen or seen.add(jump)):
            continue

        # If the jump is the end, we have finished
        if jump == (len(grid)-1, len(grid[0])-1):
            print("yes")
            exit(0)

        # Otherwise, add the jump to the list of points
        tasks.append((jump[0], jump[1], grid[jump[0]][jump[1]]))


# If tasks runs out, we can not finish the room
print("no")
