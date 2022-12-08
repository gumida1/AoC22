import re

dir_dict = {}
dir_dict2 = {}
cur_dir = ""
with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if (re.match(r"^\$ cd", line)):
            if not (line.split(" ")[2] == ".."):
                cur_dir += "-" + line.split(" ")[2]
                dir_dict[cur_dir] = 0
            else:                                                       #command $cd ..
                if not(cur_dir == "-/"):
                    splitted = cur_dir.split("-")
                    x = len(splitted.pop()) + 1
                    cur_dir = cur_dir[:-x]
                    dir_dict[cur_dir] = 0                      
cur_dir = ""

for i in range(0, len(lines)):
    lines[i] = lines[i].strip()
    if (re.match(r"^\$ cd", lines[i])):                             #command $cd *
        if not(re.match(r"^\$ cd \.\.", lines[i])):                   #command $cd dir          
            cur_dir += "-" + lines[i].split(" ")[2]
        else:                                                           #command $cd ..
            if not(cur_dir == "-/"):
                splitted = cur_dir.split("-")
                x = len(splitted.pop()) + 1
                cur_dir = cur_dir[:-x]
    elif (re.match(r"^\$ ls", lines[i])):                           #command $ls
        pass
    else:                                                           #soubory a slozky
        if not(lines[i].split(" ")[0] == "dir"):
            dir_dict[cur_dir] += int(lines[i].split(" ")[0])

cur_dir = ""
suma = 0 

for item in dir_dict.keys():
    for item2 in dir_dict.keys():
        if item2.startswith(item):
            suma += dir_dict[item2]
    dir_dict2[item] = suma
    suma = 0
        
ans = 0
ans2 = 10000000    
for k in dir_dict2:
    if dir_dict2[k] <= 100000:
        ans += dir_dict2[k] 
            
for k in dir_dict2:
    if dir_dict2[k] < ans2:
        if dir_dict2[k] > 3636666:
            ans2 = dir_dict2[k] 
            
            
print("PART 1:", ans)
print("PART 2:", ans2)