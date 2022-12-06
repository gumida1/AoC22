def start_of_message(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, i):
    Alist = []
    Alist.append(_1)
    Alist.append(_2)
    Alist.append(_3)
    Alist.append(_4)
    Alist.append(_5)
    Alist.append(_6)
    Alist.append(_7)
    Alist.append(_8)
    Alist.append(_9)
    Alist.append(_10)
    Alist.append(_11)
    Alist.append(_12)
    Alist.append(_13)
    Alist.append(_14)
    if(len(set(Alist)) == len(Alist)):
        print("PART 2:", i+14)
        exit(0)
        
with open('input_1.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines[0])):
        start_of_message(lines[0][i], lines[0][i+1], lines[0][i+2], lines[0][i+3], lines[0][i+4], lines[0][i+5], lines[0][i+6], lines[0][i+7], \
                                    lines[0][i+8], lines[0][i+9], lines[0][i+10], lines[0][i+11], lines[0][i+12], lines[0][i+13], i)
        print(lines[0][i], lines[0][i+1], lines[0][i+2], lines[0][i+3])
        if ((lines[0][i] != lines[0][i+1]) and (lines[0][i] != lines[0][i+2]) and (lines[0][i] != lines[0][i+3])):
            if (lines[0][i+1] != lines[0][i+2]) and (lines[0][i+1] != lines[0][i+3]):
                if lines[0][i+2] != lines[0][i+3]:
                    #print("PART 1:", i+4)
                    #break
                    pass