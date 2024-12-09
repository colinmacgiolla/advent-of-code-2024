#!/bin/python


def get_next_key(dictionary, current_key):
    iterator = iter(dictionary)
    for key in iterator:
        if key == current_key:
            return next(iterator, None)
    return None


def move_guard(grid, current_position):
    directions = {
        "^" : (-1,0),
        ">" : (0,1),
        "v" : (1,0),
        "<" : (0,-1)
    }
    
    # Save the current direction
    direction = grid[current_position]
    # Lookup the transformation the direction requires
    next_move = directions[direction]
    # Calculate the next position
    new_position = tuple(i+j for i,j in zip(current_position, next_move))
    
    # We've moved off grid
    if new_position not in grid:
        return False
          
    if grid[new_position] != '#':
        # move the guard
        grid[current_position] = '.'
        grid[new_position] = direction
        return new_position
    
    else:
        # Handle a change in direction
        new_direction = get_next_key(directions, direction)
        # handle wraparound
        if new_direction is None:
            new_direction = "^"
        grid[current_position] = new_direction
        return current_position
    
    
 

def main():
    '''

    '''
    with open('.//day-06//input//data.txt') as f:
        raw_input = f.read()
        
    grid = {}
    
    x,y = 0,0
    for line in raw_input.split('\n'):
        for point in line:
            grid[ (x,y) ] = point
            y += 1
        y = 0
        x += 1

    for position, object in grid.items():
        if object == '^':
            print(f"start position is: {position[0]} x {position[1]}")
            start = position
            
    positions = set()
    positions.add(start)
    result = True
    while result is not False:
        result = move_guard( grid, start)
        if result is False:
            pass
        else:
            positions.add(result)
            start = result
            
    print(f"Part 1: Number of moves by the guard: {len(positions)}")
        
    
    print("End of Line")
    
    return 0


if __name__ == "__main__":
    main()
