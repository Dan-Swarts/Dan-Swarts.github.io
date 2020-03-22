#this program does something very strange. I'm not sure what the point is

word_list = []
x = 0
y = 0

while y == 0:
    user_word = input("put ur word in mate: ").lower()
    if len(user_word) < 1:
        y = 1
    else:
        for n in range(0,len(user_word)):
            if user_word[0] == user_word[n]:
                x += 1
        if x >= 2:
            word_list.append(user_word)
        x=0

for j in range(0,len(word_list)):
    print(word_list[j], end =' ')
