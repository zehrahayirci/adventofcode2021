def solve_line(line):
    print(line)
    line = list(map(lambda x: ''.join(sorted(x)), line))
    print (line)
    num1 = [word for word in line if len(word) == 2][0]
    num7 = [word for word in line if len(word) == 3][0]
    num4 = [word for word in line if len(word) == 4][0]
    chara = list(set.difference(set(num7), set(num1)))
    charbd = list(set.difference(set(num4), set(num1)))
    num5 = [word for word in line if len(word) == 5 if charbd[0] in word and charbd[1] in word][0]
    num3 = [word for word in line if len(word) == 5 if num1[0] in word and num1[1] in word][0]
    num2 = [word for word in line if len(word) == 5 if not (word == num5 or word == num3)][0]
    num6 = [word for word in line if len(word) == 6 if not (num1[0] in word and num1[1] in word)][0]
    num9 = [word for word in line if len(word) == 6 if num4[0] in word and num4[1] in word and num4[2] in word and num4[3] in word][0]
    num0 = [word for word in line if len(word) == 6 if not (word == num6 or word == num9)][0]
    return {num0: 0, num1: 1, num2: 2, num3: 3, num4: 4, num5: 5, num6: 6, num7: 7, 'abcdefg': 8, num9: 9}

dat = open('input8.txt').read().split('\n')


processed_dat = list(map(lambda x: (x.split('|')[0].split(' '), x.split('|')[1].split(' ')), dat))

counter = 0

summ = 0
for i in range(len(processed_dat)):
    num = 0
    sol = solve_line(processed_dat[i][0])
    print(sol)
    print(processed_dat[i][1])
    for word in processed_dat[i][1]:
        if word == '':
            continue
        num = num*10 + sol["".join(sorted(list(word)))]
    print(num)
    summ += num
