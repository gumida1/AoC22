cnt = 0
cnt2 = 0
with open('input_1.txt') as f:
    lines = f.readlines()
    for line in lines:
        first, second = line.split(",")
        f1, f2 = first.split("-")
        s1, s2 = second.split("-")
        if (int(f1) <= int(s1) and int(f2) >= int(s2)) or (int(s1) <= int(f1) and int(s2) >= int(f2)):
            cnt += 1
        if (int(f2) >= int(s1) and int(s2) >= int(f1)):
            cnt2 +=1

print("PART 1:", cnt)
print("PART 2:", cnt2)
