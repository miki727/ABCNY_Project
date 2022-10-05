import random
#330-331
def letter_char(name):
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
    res = []
    tmp = name.split(' ')
    for word in tmp:
        tmp_res = []
        for i in range(len(word)):
            if word[i] == ',':
                tmp_res.pop()
            tmp_res.append(word[i])
            if i != (len(word) - 1):
                tmp_res.append(random.choice(special_char))
        res.append(''.join(tmp_res))
    return ' '.join(res)

#332-333
def name_separated_by_char(name):
    if ',' in name:
        tmp = list(name.split(', '))
        tmp.reverse()
        name = ' '.join(tmp)
    tmp = name.split(' ')
    return '/ '.join(tmp)

#335
def name_separated_by_special_char(name):
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
    tmp = name.split(' ')
    re = []
    for i in tmp:
        re.append(i)
        re.append(random.choice((special_char)))
    re.pop()
    return ''.join(re)

#337-338
def additional_noise_around(word):
    return word

#339
def additional_noise_in_between(word):
    return word

#UID-341
def large_number_of_space_between(name):
    tmp = name.split(' ')
    random.seed(random.random())
    str = ''
    for i in range(random.randint(2, 20)):
        str = str + ' '
    return str.join(tmp)

#UID-344
def large_number_of_space_in(name):
    tmp = name.split(' ')
    index = random.choice(range(len(tmp)))
    tmpWord = tmp[index]
    while(len(tmpWord) < 2):
        index = random.choice(range(len(tmp)))
        tmpWord = tmp[index]
    indexSpaces = random.choice(range(1, len(tmpWord) - 1))
    tmpStr = []
    tmpStr.append(tmpWord[:indexSpaces])
    tmpStr.append(tmpWord[indexSpaces:])
    str = ''
    for i in range(random.randint(2, 20)):
        str = str + ' '
    tmp[index] = str.join(tmpStr)
    return ' '.join(tmp)

#UID-346
def additional_space_between_first_last_name(name):
    if ', ' in name:
        tmp = name.split(', ')
        str = ''
        for i in range(random.randint(2, 20)):
            str = str + ' '
        tmp.reverse()
        return str.join(tmp)
    else:
        return name

#UID-347-348
def short_names_special_char_in_the_middle(name):
    tmp = name.split(' ')
    index = random.choice(range(len(tmp)))
    tmplist = list(tmp[index])
    tmplist.insert(random.choice(range(len(tmp[index]) - 1)), '$')
    tmp[index] = ''.join(tmplist)
    return ' '.join(tmp)

#UID-350-351
def more_than_two_parts_compressed(words):
    tmp = words.split(' ')
    if len(tmp) < 3:
        return ''.join(tmp)
    else:
        return words

#UID-353-354
def two_parts_compressed(words):
    tmp = words.split(' ')
    index = random.choice(range(1, len(tmp)))
    strTmp = []
    strTmp.append(tmp.pop(index - 1))
    strTmp.append(tmp.pop(index - 1))
    tmpWord = ''.join(strTmp)
    tmp.insert(index - 1, tmpWord)
    return ' '.join(tmp)

#UID-355-356
def all_parts_compressed(words):
    tmp = words.split(' ')
    return ''.join(tmp)

if __name__ == '__main__':
    print(two_parts_compressed("xuan zhao"))