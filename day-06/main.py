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
    

def part_2(grid, start_position, locations):
    # General idea is to insert an obsticle into the next position, then run forward until we find
    # a position we've visited before - that is a win
    blocker_sites = locations.copy()
    blocker_sites.remove(start_position)
    
    loops_detected = 0
    visited = set()
    
    for block in blocker_sites:
        updated_grid = grid.copy()
        updated_grid[block] = '#'
        
        location = start_position
        result = True
        visited.clear()

        
        while result is not False:
            result = move_guard(updated_grid, location)
            if result is False:
                # we've moved off grid
                pass
            else:
                location, direction = result, updated_grid[result]
                if ( location, direction) in visited:
                    # We've been here before
                    loops_detected += 1
                    result = False
                else:
                    visited.add( (location, direction) )
                    
    return loops_detected
 

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
    grid_copy = grid.copy()
      
    positions = set()
    positions.add(start)
    result = True
    loc = start
    while result is not False:
        result = move_guard( grid, loc)
        if result is False:
            pass
        else:
            positions.add(result)
            loc = result
            
    print(f"Part 1: Number of moves by the guard: {len(positions)}")
    
    result = part_2(grid_copy, start, positions)
    print(f"Part 2: Number of positions to create a loop: {result}")
    
    print("End of Line")
    
    return 0


if __name__ == "__main__":
    main()
