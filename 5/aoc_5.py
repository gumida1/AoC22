stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9 = [], [], [], [], [], [], [], [], []
new_stack_1, new_stack_2, new_stack_3, new_stack_4, new_stack_5, new_stack_6, new_stack_7, new_stack_8, new_stack_9 = [], [], [], [], [], [], [], [], []
tmp_cnt = 0
stack_num = 1
rule_list = 0
rev_flag = 0

def move_crate(list1, list2, how_many, part_1_2):
    tmp_list = []
    if part_1_2 == 1:
        for i in range(0, how_many):
            tmp = list1.pop()
            list2.append(tmp)
        return list1, list2
    else:
        for i in range(0, how_many):
            tmp = list1.pop()
            tmp_list.append(tmp) 
        for i in range(0, how_many):
            tmp = tmp_list.pop()
            list2.append(tmp)
        
        return list1, list2

with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line == '\n':
            rule_list = 1
        if rule_list == 0:
            for char in line:
                if not(char.isspace()):
                    if not (char == '[' or char == ']' or char.isnumeric()):
                        if stack_num == 1:
                            stack_1.append(char)
                        elif stack_num == 2:
                            stack_2.append(char)
                        elif stack_num == 3:
                            stack_3.append(char)
                        elif stack_num == 4:
                            stack_4.append(char)
                        elif stack_num == 5:
                            stack_5.append(char)
                        elif stack_num == 6:
                            stack_6.append(char)
                        elif stack_num == 7:
                            stack_7.append(char)
                        elif stack_num == 8:
                            stack_8.append(char)
                        elif stack_num == 9:
                            stack_9.append(char)
                tmp_cnt += 1
                if tmp_cnt == 4:
                    stack_num += 1
                    tmp_cnt = 0    
                if char == '\n':
                    stack_num = 1
        else:
            if not (line == '\n'):
                arr = line.strip().split(" ")
                if rev_flag == 0:
                    new_stack_1, new_stack_2, new_stack_3, new_stack_4, new_stack_5, new_stack_6, new_stack_7, new_stack_8, new_stack_9 = \
                        stack_1[::-1], stack_2[::-1], stack_3[::-1], stack_4[::-1], stack_5[::-1], stack_6[::-1], stack_7[::-1], stack_8[::-1], stack_9[::-1]
                    stack_dict = {1:new_stack_1, 2:new_stack_2, 3:new_stack_3, 4:new_stack_4, 5:new_stack_5, 6:new_stack_6, 7:new_stack_7, 8:new_stack_8, 9:new_stack_9}
                    rev_flag = 1
                stack_dict[int(arr[3])], stack_dict[int(arr[5])] = move_crate(stack_dict[int(arr[3])], stack_dict[int(arr[5])], int(arr[1]), 2)

print("BOTH PARTS:", new_stack_1.pop() + new_stack_2.pop() + new_stack_3.pop() + new_stack_4.pop() + new_stack_5.pop() + new_stack_6.pop() + new_stack_7.pop() + new_stack_8.pop() + new_stack_9.pop(),)