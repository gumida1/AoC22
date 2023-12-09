with open('input_2.txt') as f:
    lines = f.readlines()
dict_sou = {}
i, j = 0, 0
for line in lines:
    line = line.strip()
    for char in line:
        dict_sou[i, j] = int(char)
        j += 1
    i += 1
    max_j = j
    j = 0

print(dict_sou)
visibles = 0
highest_rigt, highest_left, highest_top, highest_bottom = 0, 0, 0, 0
right, left, top, bottom = 0, 0, 0, 0
biggest_view, stop_right, stop_left, stop_top, stop_bottom = 0, 0, 0, 0, 0 


for item in dict_sou:
    if not(item[0] == 0 or item[0] == i-1 or item[1] == 0 or item[1] == max_j-1):
        current_height = dict_sou[item]
        for second in dict_sou:
            if second[0] == item[0] and second[1] != item[1]:               #projdou hodnoty ze stejneho radku
                if second[1] > item[1] and dict_sou[second] > highest_rigt:         
                    highest_rigt = dict_sou[second]
                elif second[1] < item[1] and dict_sou[second] > highest_left:
                    highest_left = dict_sou[second]
            elif second[1] == item[1] and second[0] != item[0]:
                if second[0] > item[0] and dict_sou[second] > highest_bottom:         
                    highest_bottom = dict_sou[second] 
                elif second[0] < item[0] and dict_sou[second] > highest_top:
                    highest_top = dict_sou[second]
                    
        for second in dict_sou:
            if second[0] == item[0] and second[1] != item[1]:               #projdou hodnoty ze stejneho radku
                if second[1] > item[1] and current_height > dict_sou[second]:         
                    if stop_right == 0:
                        right += 1
                else:
                    stop_right = 1     
                if second[1] < item[1] and current_height > dict_sou[second]:
                    if stop_left == 1:
                        left += 1
                else:
                    stop_left = 1
                    #left = 0
            elif second[1] == item[1] and second[0] != item[0]:
                if second[0] > item[0] and current_height > dict_sou[second]:         
                    if stop_bottom == 0:
                        bottom += 1
                else:
                    stop_bottom = 1    
                if second[0] < item[0] and current_height > dict_sou[second]:
                    if stop_top == 1:
                        top += 1
                else:
                    stop_top = 1
                    #top = 0

        if stop_right == 1:
            right += 1
        if stop_left == 1:
            left += 1
        if stop_bottom == 1:
            bottom += 1
        if stop_top == 1:
            top += 1
        
        
        
        print(top, left, bottom,  right)
        
        if current_height > highest_left or current_height > highest_rigt or current_height > highest_top or current_height > highest_bottom:
            visibles += 1
        
        highest_rigt, highest_left, highest_bottom, highest_top = 0, 0, 0, 0  
         
        if right * left * top * bottom > biggest_view:
            biggest_view = right * left * top * bottom 
        
        right, left, top, bottom = 0, 0, 0, 0
        stop_right, stop_left, stop_top, stop_bottom = 0, 0, 0, 0
        
okraje = 2*i + 2*(max_j-2)        
print("PART 1:", visibles + okraje)
print("PART 2:", biggest_view)