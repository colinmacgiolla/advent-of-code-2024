#!/bin/python





def search_word_all_directions(matrix, word):
    rows, cols = len(matrix), len(matrix[0])
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Up-Left
        (-1, 1),  # Up-Right
        (1, -1),  # Down-Left
        (1, 1)    # Down-Right
    ]
    count = 0

    def dfs(i, j, index, di, dj):
        if index == len(word):
            return 1
        if (i < 0 or i >= rows or j < 0 or j >= cols or 
            matrix[i][j] != word[index]):
            return 0
        return dfs(i + di, j + dj, index + 1, di, dj)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == word[0]:
                for di, dj in directions:
                    count += dfs(i, j, 0, di, dj)

    return count

  


def main():
    '''

    '''
    with open('.//day-04//input//data.txt') as f:
        raw_input = f.read()
        
    data = []
    for line in raw_input.split('\n'):
        data.append(line)

    result = search_word_all_directions(data,'XMAS')
    
    print(f"Part 1: Sum of all values is: {result}")
    
    # brute force
    result2 = sum((data[i][j] == 'A') and ({data[i-1][j-1], data[i+1][j+1]} == {data[i-1][j+1], data[i+1][j-1]} == {'M', 'S'}) 
        for i in range(1, len(data) - 1)
        for j in range(1, len(data[i]) - 1)
    )
    print(f"Part 2: Brute force sum: {result2}")
    
    

    
    print("End of Line")
    
    return 0


if __name__ == "__main__":
    main()
