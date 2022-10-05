import random
import pandas as pd
import numpy as np
import GeneratorWay as gen_util


refer = pd.read_excel('GWU Test Case Type Tracker_XuanZhao.xlsx')
UIDList = list(refer['UID'])
ThemeList = list(refer['Theme'])
categoryList = list(refer['Category'])
sub_categoryList = list(refer['Subcategory'])
entity_typeList = list(refer['Entity Type'])

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)


ofac_list = ofac_list_download[[0, 1, 2]]
ofac_list.columns = ['uid', 'name', 'entity_type']

print(ofac_list['entity_type'].value_counts())

# only evaluate individuals
ofac_list_individuals = ofac_list[(ofac_list.entity_type == 'individual')]

# only evaluate entity
ofac_list_tmp = ofac_list[(ofac_list.entity_type != 'vessel')]
ofac_list_tmp2 = ofac_list_tmp[(ofac_list_tmp.entity_type != 'individual')]
ofac_list_entities = ofac_list_tmp2[(ofac_list_tmp2.entity_type != 'aircraft')]

ofac_list_sampled = ofac_list_individuals.sample(n = 10)
final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID',
                                         'OFAC List UID', 'Original Name', 'Test Case Name'])

for index in range(len(UIDList)):
    uid = UIDList[index]
    theme = ThemeList[index]
    category = categoryList[index]
    sub_category = sub_categoryList[index]
    entity_type = entity_typeList[index]

    ofac_list_sampled = []
    if entity_type == 'Individual':
        ofac_list_sampled = ofac_list_individuals.sample(n=10)
    elif entity_type == 'Entity':
        ofac_list_sampled = ofac_list_entities.sample(n=10)

    for index, row in ofac_list_sampled.iterrows():
        original_name = row['name']
        final_test_name = row['name']
        test_case_flag = False
        if sub_category == 'All letters separated by special character':
            final_test_name = gen_util.letter_char(original_name)
            test_case_flag = True
        elif sub_category == 'All name parts separated by character':
            final_test_name = gen_util.name_separated_by_char(original_name)
            test_case_flag = True
        elif sub_category == 'All name parts separated by special character':
            final_test_name = gen_util.name_separated_by_special_char(original_name)
            test_case_flag = True
        elif sub_category == 'Additional noise around':
            final_test_name = gen_util.additional_noise_around(original_name)
            test_case_flag = True
        elif sub_category == 'Additional Noise in between':
            final_test_name = gen_util.additional_noise_in_between(original_name)
            test_case_flag = True
        elif sub_category == 'Abnormally large number of spaces between Name Parts':
            final_test_name = gen_util.large_number_of_space_between(original_name)
            test_case_flag = True
        elif sub_category == 'Abnormally large number of spaces in the name parts':
            final_test_name = gen_util.large_number_of_space_in(original_name)
            test_case_flag = True
        elif sub_category == 'Additional Space Between First and Last Name':
            final_test_name = gen_util.additional_space_between_first_last_name(original_name)
            test_case_flag = True
        elif sub_category == 'Very Short Names w/ Special Character in the Middle':
            final_test_name = gen_util.short_names_special_char_in_the_middle(original_name)
            test_case_flag = True
        elif sub_category == '>2 name parts compressed':
            final_test_name = gen_util.more_than_two_parts_compressed(original_name)
            test_case_flag = True
        elif sub_category == '2 name parts compressed':
            final_test_name = gen_util.two_parts_compressed(original_name)
            test_case_flag = True
        elif sub_category == 'All name parts compressed':
            final_test_name = gen_util.all_parts_compressed(original_name)
            test_case_flag = True

        if test_case_flag:
            final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid1 + ' - '
                                                           + str(index), row['uid'], row['name'], final_test_name]  # append to the dataframe
            test_case_flag = False

print(final_test_cases)
final_test_cases.to_csv('UID_330_439.csv')