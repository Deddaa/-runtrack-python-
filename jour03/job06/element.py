alphabet10= "abcdefghijklmnopqrstuvwxyz"*10
offset = 0
i = 1
while offset < len(alphabet10)-i:
    print(alphabet10[offset : offset +i])
    offset += i
    i +=1