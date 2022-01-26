from word import word1, word2

word_list = word1 + word2

print(
    'O : Correct charactor & position'
    'A : Correct charactor & wrong position'
    'X : Non-exist charactor'
)


for i in range(5):
    w = ''
    correct = ''
    while len(w) != 5:
        w = input('input word\n> ')
        w = w.lower()
    while len(correct) != 5:
        correct = input('input OAX\n> ')
        correct = correct.lower()

    for index, ch in enumerate(correct):
        c = w[index]
        if ch == 'o':
            word_list = list(filter(lambda x:(x[index]==c), word_list))
        elif ch == 'x':
           word_list = list(filter(lambda x:(c not in x), word_list))
        elif ch == 'a':
           word_list = list(filter(lambda x:(c in x and x[index] != c), word_list))
        #print(word_list)

    if len(word_list) >= 100:
        print(word_list[:100])
    elif len(word_list) == 1:
        print(f'Answer:\t{word_list[0]}')
        exit(0)
    else:
        print(word_list)