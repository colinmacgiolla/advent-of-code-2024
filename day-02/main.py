#!/bin/python

import re


def part2(input):
    do = r"do\(\)"
    dont = r"don't\(\)"
    mul = r"mul\((\d*),(\d*)\)"
    
    total = 0
    enabled = True
    
    for x in re.finditer( f'{do}|{dont}|{mul}', input ):
        if re.fullmatch(do, x.group() ):
            enabled = True
        elif re.fullmatch(dont, x.group() ):
            enabled = False
        elif enabled:
            total += int(x.group(1)) * int(x.group(2))
    return total
        

def main():
    '''

    '''
    with open('.//day-03//input//data.txt') as f:
        raw_input = f.read()
        

    
    sum = 0
    
    
    for a,b in re.findall( r"mul\((\d*),(\d*)\)", raw_input):
        sum += int(a) * int(b)

    print(f"Part 1: Sum of all values is: {sum}")

       
    print(f"Part 2: Sum of enabled multiplications is: {part2(raw_input)}")

    
    print("End of Line")
    
    return 0


if __name__ == "__main__":
    main()
