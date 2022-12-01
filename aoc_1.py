
tmp = 0
maxim_cnt_1 = 0
maxim_cnt_2 = 0
maxim_cnt_3 = 0

with open('input_1.txt') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        if line == '\n':
            if tmp > maxim_cnt_1:
                maxim_cnt_3 = maxim_cnt_2
                maxim_cnt_2 = maxim_cnt_1
                maxim_cnt_1 = tmp
                print ("1:", tmp, maxim_cnt_1, maxim_cnt_2, maxim_cnt_3, )
            elif tmp > maxim_cnt_2:
                maxim_cnt_3 = maxim_cnt_2
                maxim_cnt_2 = tmp
                print ("2:", tmp, maxim_cnt_1, maxim_cnt_2, maxim_cnt_3, )
            elif tmp > maxim_cnt_3:
                maxim_cnt_3 = tmp
                print ("3:", tmp, maxim_cnt_1, maxim_cnt_2, maxim_cnt_3, )
            tmp = 0
        else:
            tmp += int(line)    
        
print(maxim_cnt_1 + maxim_cnt_2 + maxim_cnt_3)