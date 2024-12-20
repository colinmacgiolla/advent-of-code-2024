#!/bin/python






def main():
    '''

    '''
    with open('.//day-05//input//data.txt') as f:
        raw_input = f.read()
        
    data = []
    rules = set()
    tag = False
    for line in raw_input.split('\n'):

        if line == '':
            tag = True
        if not tag:
            if line != '':
                k,v = line.split('|')
                rules.add( (k,v) )
        if tag:
            if line != "":
                data.append( line.split(','))

    total = 0
    invalid_pages = []
    
    for page in data:
        valid = True
        for rule in rules:
            #if data.index(page) == 3:
            #    print(rule)
            if rule[0] in page and rule[1] in page and \
                page.index(rule[1]) < page.index(rule[0]):
                    valid = False
                    break
        if valid:
            total += int(page[ len(page) // 2])
        else:
            invalid_pages.append(page)

    
    print(f"Part 1: Sum of valid pages is: {total}")
    
    total = 0
    for page in invalid_pages:
        for i in range(len(page)):
            for j in range(i+1, len(page)):
                if (page[i], page[j]) in rules:
                    page[j],page[i] = page[i],page[j]

        total += int(page[ len(page) // 2])        
    
    print(f"Part 2: Sum of fixed pages is: {total}")

    
    

    
    print("End of Line")
    
    return 0


if __name__ == "__main__":
    main()
