import math

keyboard = [list("qwertyuiop"), list("asdfghjkl;"), list("zxcvbnm,./")]

def dist(key1, key2):
   
    if key1 == key2:
        return 0
    else:
   
        coor = []
        for i in range(3):
            for j in range(10):
                if keyboard[i][j] == key1 or keyboard[i][j] == key2:
                    coor.append([i, j])
   
        if coor[0][0] == coor[1][0]:
            offset = 0
        elif coor[0][0] == 0 and coor[1][0] == 1:
            offset = 0.5
        elif coor[0][0] == 0 and coor[1][0] == 2:
            offset = 1.5
        else:
            offset = 1
   
        h_dist = offset + abs(coor[0][1] - coor[1][1])*1.9
        v_dist = abs(coor[1][0] - coor[0][0])*1.9
   
        return math.sqrt(h_dist**2 + v_dist**2)

def total_dist(word):
    total = 0
    for i in range(len(word)-1):
        total += dist(word[i], word[i+1])
    return total

file = open("words_alpha.txt", "r")
content = file.readlines()

best = content[0][:len(content[0])-1] # first word is not single-lettered

for i in content:
    j = i[:len(i)-1]
    if len(j) == 1:
        continue
    else:
        if total_dist(j)/len(j) > total_dist(best)/len(best):
            best = j
        
print(best)
