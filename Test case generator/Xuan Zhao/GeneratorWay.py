import random

from datetime import datetime
from datetime import timedelta
from dateutil import parser

#UID327-328
def add_two_special(word):
    return str('@' + word + '%')

#UID330-331
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

#UID332-333
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

#UID337-338
def additional_noise_around(word):
    if 'bank' in word:
        word = word.replace('bank', 'bank of money')
    elif ',' in word:
        word = word.replace(',', 'BLAH,')
    return word

#UID339
def additional_noise_in_between(word):
    if 'bank' in word:
        word = word.replace('bank', 'credit bank')
    return word

#UID-341-342
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
    while(len(tmpWord) < 3):
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
    target = 1
    if len(tmp[index]) > target :
        target = random.choice(range(len(tmp[index]) - 1))
    tmplist.insert(target, '$')
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
    index = 1
    if len(tmp) > 1:
        index = random.choice(range(1, len(tmp)))

    strTmp = []
    strTmp.append(tmp.pop(index - 1))
    # strTmp.append(tmp.pop(index - 1))
    tmpWord = ''.join(strTmp)
    tmp.insert(index - 1, tmpWord)
    return ' '.join(tmp)

#UID-355-356
def all_parts_compressed(words):
    tmp = words.split(' ')
    return ''.join(tmp)

#UID-357
def compress_common_name_parts(name):
    return name.replace('COMMERCIAL BANK', 'COMMERCIALBANK')

#UID-358
def compress_common_and_non_common_parts(name):
    tmp = name.replace('COMMERCIAL BANK', '').split(' ')
    return ''.join(tmp) + ' COMMERCIALBANK'

#UID-359
def compress_non_common_name_parts(name):
    tmp = name.replace('COMMERCIAL BANK', '').split(' ')
    return ''.join(tmp) + ' COMMERCIAL BANK'

#UID-360
def more_than_two_name_parts(name):
    return name.replace(' ', '-')

#UID-361-362
def more_than_two_special_replaced(name):
    tmp = name.replace(', ', '. ')
    tmp = tmp.replace(', S.A.', '. S,A.')
    tmp = tmp.replace('-', '_')
    return tmp

#UID-363-364
def one_special_replaced(name):
    tmp = name.replace(',', '.')
    return tmp

#UID-365-366
def two_special_replaced(name):
    tmp = name.replace(', ', '. ')
    tmp = tmp.replace(', S.A.', '. S,A.')
    tmp = tmp.replace('-', '_')
    return tmp

#UID-367-368
def all_special_replaced(name):
    tmp = name.replace('.', ',')
    tmp = tmp.replace(', ', '. ')
    tmp = tmp.replace('-', '_')
    return tmp

#UID-369-370
def more_than_two_special_removed(name):
    tmp = name.replace(', ', ' ')
    tmp = tmp.replace(', S.A.', ' SA')
    tmp = tmp.replace('-', '')
    return tmp

#UID-371-372
def one_special_replaced(name):
    tmp = name.replace(',', '')
    return tmp

#UID-373-374
def two_special_replaced(name):
    tmp = name.replace(', ', ' ')
    tmp = tmp.replace(', S.A.', ' SA')
    tmp = tmp.replace('-', '')
    return tmp

#UID-375-376
def all_special_removed(name):
    tmp = name.replace('.', '')
    tmp = tmp.replace(', ', ' ')
    tmp = tmp.replace('-', '')
    return tmp

#UID-378
def letter_replaced_by_spacial(name):
    first = name[0]
    name = name.replace(first, '@')
    return name

#UID379
def special_character_replaced_by_full(name):
    return name.replace('&', 'and')

#UID-381-382
def more_than_two_name_parts_split(name):
    tmp = name.split(' ')
    for i in range(len(tmp)):
        tmp_word = list(tmp[i])
        tmp_word.insert(1, ' ')
        tmp[i] = ''.join(tmp_word)
    return ' '.join(tmp)

#UID-384-385
def one_name_parts_split(name):
    tmp = name.split(' ')
    for i in range(1):
        tmp_word = list(tmp[i])
        tmp_word.insert(1, ' ')
        tmp[i] = ''.join(tmp_word)
    return ' '.join(tmp)

#UID-387-388
def two_name_parts_split(name):
    tmp = name.split(' ')
    if len(tmp) < 2:
        tmp = list(name)
    else:
        for i in range(2):
            tmp_word = list(tmp[i])
            tmp_word.insert(1, ' ')
            tmp[i] = ''.join(tmp_word)
    return ' '.join(tmp)

#UID-390-391
def all_letters_split(name):
    tmp = name.split(' ')
    for i in range(len(tmp)):
        tmp_word = list(tmp[i])
        tmp[i] = ' '.join(tmp_word)
    return ' '.join(tmp)

#UID-392-393
def all_name_parts_split(name):
    tmp = name.split(' ')
    for i in range(len(tmp)):
        tmp_word = list(tmp[i])
        tmp_word.insert(1, ' ')
        tmp[i] = ''.join(tmp_word)
    return ' '.join(tmp)

#UID-395-396
def new_line_split(name):
    index = random.choice(range(1, len(name) - 1))
    tmp = list(name)
    tmp.insert(index, '\n')
    return ''.join(tmp)

#UID-397
def split_common_and_common(name):
    return name.replace('COMMERCIAL', 'COMMER CIAL')

#UID-398
def split_common_and_non_common(name):
    name = name.replace('COMMERCIAL', 'COMMER CIAL')
    first = name[0]
    rep = str(first + ' ')
    name = name.replace(first, rep)
    return name

#UID-399
def split_noise_name(name):
    return name.replace('COMMERCIAL', 'COMMER CIAL')

#UID-400
def split_non_common_and_non_common(name):
    first = name[0]
    rep = str(first + ' ')
    name = name.replace(first, rep)
    return name

#UID-402-403
def very_short(name):
    first = name[0]
    rep = str(first + ' ')
    name = name.replace(first, rep)
    return name

#UID-418
def exact_dob_dd_mm_yy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%d-%m-%y')

#UID-419
def exact_dob_dd_mm_yyyy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%d-%m-%Y')

#UID-420
def exact_dob_mm_dd(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%m-%d')

#UID-421
def exact_dob_mm_dd_yy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%m-%d-%y')

#UID-422
def exact_dob_mm_dd_yyyy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%m-%d-%Y')

#UID-423
def exact_dob_mm_yy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%m-%y')

#UID-424
def exact_dob_mm_yyyy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%m-%Y')

#UID-425
def exact_dob_yy_dd_mm(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%y-%d-%m')

#UID-426
def exact_dob_yyyy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%Y')

#UID-427
def exact_dob_out_of_dd_mm_yy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=delta)
    return name + ' ' + date.strftime('%d-%m-%y')

#UID-428
def exact_dob_out_of_dd_mm_yyyy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=delta)
    return name + ' ' + date.strftime('%d-%m-%Y')

#UID-429
def exact_dob_out_of_mm_dd(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=delta)
    return name + ' ' + date.strftime('%m-%d')

#UID-430
def exact_dob_out_of_mm_dd_yy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=delta)
    return name + ' ' + date.strftime('%m-%d-%y')

#UID-431
def exact_dob_out_of_mm_dd_yyyy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=delta)
    return name + ' ' + date.strftime('%m-%d-%Y')

#UID-432
def exact_dob_out_of_mm_yy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=delta)
    return name + ' ' + date.strftime('%m-%y')

#UID-433
def exact_dob_out_of_mm_yyyy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=delta)
    return name + ' ' + date.strftime('%m-%Y')

#UID-434
def exact_dob_out_of_yy_dd_mm(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=delta)
    return name + ' ' + date.strftime('%y-%d-%m')

#UID-435
def exact_dob_out_of_yyyy(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    # delta = random.randint(32, 365)
    date = parser.parse(dob) + timedelta(days=366)
    return name + ' ' + date.strftime('%Y')

#UID-436
def exact_dob_dd_mm_yy_with_slash(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob) + timedelta(days=366)
    return name + ' ' + date.strftime('%d/%m/%y')

#UID-437
def exact_dob_dd_mm_yyyy_with_slash(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%d/%m/%Y')

#UID-438
def exact_dob_mm_dd_with_slash(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%m/%d')

#UID-439
def exact_dob_mm_dd_yy_with_slash(name, dob):
    dob = dob.replace('DOB ', '')
    # print(dob)
    date = parser.parse(dob)
    return name + ' ' + date.strftime('%m/%d/%y')
