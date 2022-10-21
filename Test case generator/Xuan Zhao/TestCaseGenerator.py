import random
import pandas as pd
import numpy as np
import GeneratorWay as gen_util
from dateutil.parser import parse

def is_date(string, fuzzy):
    try:
        parse(string, fuzzy = fuzzy)
        return True
    except ValueError:
        return False


refer = pd.read_excel('GWU Test Case Type Tracker_XuanZhao.xlsx')
UIDList = list(refer['UID'])
ThemeList = list(refer['Theme'])
categoryList = list(refer['Category'])
sub_categoryList = list(refer['Subcategory'])
entity_typeList = list(refer['Entity Type'])

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)


ofac_list = ofac_list_download[[0, 1, 2, 11]]
print(ofac_list_download)
ofac_list.columns = ['uid', 'name', 'entity_type', 'details']

print(ofac_list['entity_type'].value_counts())

# only evaluate individuals
ofac_list_individuals = ofac_list[(ofac_list.entity_type == 'individual')]
print(len(ofac_list_individuals))
ofac_list_individuals['DOB'] = ofac_list_individuals.details.str.split(';', expand=True)[0]
ofac_list_individuals_tmp = ofac_list_individuals[(ofac_list_individuals.DOB.str.contains('DOB ', na = False))]
ofac_list_individuals_DOB = ofac_list_individuals_tmp[(ofac_list_individuals_tmp.DOB.str.len() == 15)]
ofac_list_individuals_special = ofac_list_individuals[(ofac_list_individuals.name.str.contains('-', na = False))]
print(ofac_list_individuals_DOB)
print(len(ofac_list_individuals_DOB))


# only evaluate entity
ofac_list_tmp = ofac_list[(ofac_list.entity_type != 'vessel')]
ofac_list_tmp2 = ofac_list_tmp[(ofac_list_tmp.entity_type != 'individual')]
ofac_list_entities = ofac_list_tmp2[(ofac_list_tmp2.entity_type != 'aircraft')]
ofac_list_entities_bank = ofac_list_entities[(ofac_list_entities.name.str.contains('COMMERCIAL BANK', na = False))]
ofac_list_entities_company = ofac_list_entities[(ofac_list_entities.name.str.contains(', S.A.', na = False))]
ofac_list_entities_and = ofac_list_entities[(ofac_list_entities.name.str.contains('&.', na = False))]

# ofac_list_sampled = ofac_list_individuals.sample(n = 10)
final_test_cases = pd.DataFrame(columns=['UID', 'Theme', 'Category', 'Sub-category', 'Entity-Type', 'Test Case ID',
                                         'OFAC List UID', 'Original Name', 'Test Case Name'])

for index in range(len(UIDList)):
    uid = UIDList[index]
    theme = ThemeList[index]
    category = categoryList[index]
    sub_category = sub_categoryList[index]
    entity_type = entity_typeList[index]

    ofac_list_sampled = []

    if sub_category in ['Compress common and  common name parts', 'Compress non common and non common name parts',
                          'Compress common and non common name parts', 'Split common and  common name parts',
                        'Split common and non common name parts', 'Split noise name parts',
                        'Split non common and non common name parts']:
        ofac_list_sampled = ofac_list_entities_bank.sample(n=10)
    elif index >= 64:
        ofac_list_sampled = ofac_list_individuals_DOB.sample(n=10)
    elif sub_category in ['>2 special characters replaced by equivalent', '1 special character replaced by equivalent',
                          '2 special characters replaced by equivalent', 'All special characters replaced by equivalent',
                          '>2 special characters removed', '1 special character removed', '2 special characters removed',
                          'All special characters removed']:
        if entity_type == 'Individual':
            ofac_list_sampled = ofac_list_individuals_special.sample(n=10)
        elif entity_type == 'Entity':
            ofac_list_sampled = ofac_list_entities_company.sample(n=10)
    elif sub_category in ['Additional noise around', 'Additional Noise in between']:
        if entity_type == 'Individual':
            ofac_list_sampled = ofac_list_individuals.sample(n=10)
        elif entity_type == 'Entity':
            ofac_list_sampled = ofac_list_entities_bank.sample(n=10)
    elif sub_category in ['Special character replaced by full name part']:
        ofac_list_sampled = ofac_list_entities_and.sample(n=10)
    elif entity_type == 'Individual':
        ofac_list_sampled = ofac_list_individuals.sample(n=10)
    elif entity_type == 'Entity':
        ofac_list_sampled = ofac_list_entities.sample(n=10)



    for i, row in ofac_list_sampled.iterrows():
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
        elif sub_category == 'Compress common and  common name parts':
            final_test_name = gen_util.compress_common_name_parts(original_name)
            test_case_flag = True
        elif sub_category == 'Compress common and non common name parts':
            final_test_name = gen_util.compress_common_and_non_common_parts(original_name)
            test_case_flag = True
        elif sub_category == 'Compress non common and non common name parts':
            final_test_name = gen_util.compress_non_common_name_parts(original_name)
            test_case_flag = True
        elif sub_category == '> 2 name parts compressed':
            final_test_name = gen_util.more_than_two_name_parts(original_name)
            test_case_flag = True
        elif sub_category == '>2 name parts split':
            final_test_name = gen_util.more_than_two_name_parts_split(original_name)
            test_case_flag = True
        elif sub_category == '1 name part split':
            final_test_name = gen_util.one_name_parts_split(original_name)
            test_case_flag = True
        elif sub_category == '2 name parts split':
            final_test_name = gen_util.two_name_parts_split(original_name)
            test_case_flag = True
        elif sub_category == 'All letters split':
            final_test_name = gen_util.all_letters_split(original_name)
            test_case_flag = True
        elif sub_category == 'All name parts split':
            final_test_name = gen_util.all_name_parts_split(original_name)
            test_case_flag = True
        elif sub_category == 'New Line split':
            final_test_name = gen_util.new_line_split(original_name)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in DD-MM-YY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_dd_mm_yy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in DD-MM-YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_dd_mm_yyyy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in MM-DD':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_mm_dd(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in MM-DD-YY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_mm_dd_yy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in MM-DD-YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_dd_mm_yyyy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in MM-YY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_mm_yy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in MM-YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_mm_yyyy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in YY-DD-MM':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_yy_dd_mm(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_yyyy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in DD-MM-YY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_dd_mm_yy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in DD-MM-YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_dd_mm_yyyy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in MM-DD':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_mm_dd(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in MM-DD-YY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_mm_dd_yy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in MM-DD-YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_mm_dd_yyyy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in MM-YY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_mm_yy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in MM-YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_mm_yyyy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in YY-DD-MM':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_yy_dd_mm(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Out of range DOB in YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_out_of_yyyy(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in DD/MM/YY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_dd_mm_yy_with_slash(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in DD/MM/YYYY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_dd_mm_yyyy_with_slash(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in MM/DD':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_mm_dd_with_slash(original_name, dob)
            test_case_flag = True
        elif sub_category == 'Exact Name and Exact DOB in MM/DD/YY':
            dob = row['DOB']
            final_test_name = gen_util.exact_dob_mm_dd_yy_with_slash(original_name, dob)
            test_case_flag = True
        elif sub_category == '>2 special characters replaced by equivalent':
            final_test_name = gen_util.more_than_two_special_replaced(original_name)
            test_case_flag = True
        elif sub_category == '1 special character replaced by equivalent':
            final_test_name = gen_util.one_special_replaced(original_name)
            test_case_flag = True
        elif sub_category == '2 special characters replaced by equivalent':
            final_test_name = gen_util.two_special_replaced(original_name)
            test_case_flag = True
        elif sub_category == 'All special characters replaced by equivalent':
            final_test_name = gen_util.all_special_replaced(original_name)
            test_case_flag = True
        elif sub_category == '>2 special characters removed':
            final_test_name = gen_util.more_than_two_special_removed(original_name)
            test_case_flag = True
        elif sub_category == '1 special character removed':
            final_test_name = gen_util.one_special_replaced(original_name)
            test_case_flag = True
        elif sub_category == '2 special characters removed':
            final_test_name = gen_util.two_special_replaced(original_name)
            test_case_flag = True
        elif sub_category == 'All special characters removed':
            final_test_name = gen_util.all_special_removed(original_name)
            test_case_flag = True
        elif sub_category == '2 special characters added':
            final_test_name = gen_util.add_two_special(original_name)
            test_case_flag = True
        elif sub_category == 'Letter replaced by Special Character':
            final_test_name = gen_util.letter_replaced_by_spacial(original_name)
            test_case_flag = True
        elif sub_category == 'Split common and  common name parts':
            final_test_name = gen_util.split_common_and_common(original_name)
            test_case_flag = True
        elif sub_category == 'Split common and non common name parts':
            final_test_name = gen_util.split_common_and_non_common(original_name)
            test_case_flag = True
        elif sub_category == 'Split noise name parts':
            final_test_name = gen_util.split_noise_name(original_name)
            test_case_flag = True
        elif sub_category == 'Split non common and non common name parts':
            final_test_name = gen_util.split_non_common_and_non_common(original_name)
            test_case_flag = True
        elif sub_category == 'Very Short Name':
            final_test_name = gen_util.very_short(original_name)
            test_case_flag = True
        elif sub_category == 'Special character replaced by full name part':
            final_test_name = gen_util.special_character_replaced_by_full(original_name)
            test_case_flag = True



        if not test_case_flag:
            print(sub_category)
            print(entity_type)

        if test_case_flag:
            final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - '
                                                           + str(i), row['uid'], row['name'], final_test_name]  # append to the dataframe
            test_case_flag = False


print(final_test_cases)
final_test_cases.to_csv('UID_330_439.csv')
