
cnt = 0
cnt2 = 0
line_arr = []
def char_to_num(char):
    if char.isupper():
        one_based = ord(char) - 64 + 26
        return one_based
    else:
        one_based = ord(char) - 96
        return one_based

with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        line_arr.append(line)   
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        for char in range(0, len(firstpart)):
            if firstpart[char] in secondpart:
                cnt += char_to_num(firstpart[char])
                break
            
    i = 0
    while(1):
        lenght = len(line_arr)
        for char in line_arr[i]:
            if (char in line_arr[i+1]) and (char in line_arr[i+2]):
                cnt2 += char_to_num(char)
                i += 3
                break
        if i == lenght:
            break
            
print("PART 1: ", cnt)
print("PART 2: ", cnt2)