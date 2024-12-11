#!/bin/python


def is_safe(input):
    # Check if the levels are either increasing or decreasing
    if all( input[i] < input[i+1] for i in range(len(input)-1) ) or \
       all( input[i] > input[i+1] for i in range(len(input)-1) ):
           # now check the diffs
           if all( abs( input[i] - input[i+1] ) >= 1 for i in range(len(input)-1) ) and \
               all( abs( input[i] - input[i+1] ) <= 3 for i in range(len(input)-1) ):
                   return True


def damper(input):
    
    if any(is_safe(input[:i] + input[i+1:]) for i in range(len(input))):
        return True
    return False   
       


def main():
    '''

    '''
    with open('.//day-02//input//data.txt') as f:
        raw_input = f.read()
        
    data = []
    for line in raw_input.split('\n'):
        if not line == '':
            data.append( [ int(num) for num in line.split() ])
    

    safe_reports = 0
    unsafe_report_list = []
    for report in data:
        if is_safe(report):
            safe_reports += 1
        else:
            unsafe_report_list.append(report)
        
    
    print(f"Part 1: Sum of all values is: {safe_reports}")
    dampened_reports = 0
    for entry in unsafe_report_list:
        if damper(entry):
            dampened_reports += 1

    print(f"Part 2: Dampened list is {safe_reports + dampened_reports}")

    
    print("End of Line")
    
    return 0


if __name__ == "__main__":
    main()
