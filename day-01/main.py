#!/bin/python


from collections import Counter


def main():
    '''

    '''
    with open('.//input//data.txt') as f:
        raw_input = f.read()
        
    left = []
    right = []
    for line in raw_input.split('\n'):
        if not line == '':
            data = line.split()
            left.append(int(data[0]))
            right.append(int(data[1]))
    
    result = sum ( [ abs(a - b) for a,b in zip( sorted(left),sorted(right) ) ]  )  
    
    print(f"Part 1: Sum of all values is: {result}")
    
    counter = Counter(right)
    
    sumulartity = 0
    
    for entry in left:
        sumulartity += entry * counter[entry]
        
    print(f"Part 2: Sum of the sumularity score is is: {sumulartity}")

    
    print("End of Line")
    
    return 0


if __name__ == "__main__":
    main()
