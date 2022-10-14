#!/usr/bin/env python
# coding: utf-8

# # IMPORT DATA, PACKAGES, AND FUNCTIONS

# ## import the relevant functions and packages

# In[1]:


import pandas as pd
import numpy as np
from test_case_generator_functions import alphabet, num_of_alphabet


# # TEST CASE TYPE REFERENCE INFORMATION

# In[2]:


uid = 'UID-246' 
theme = 'Names where name parts are Modified'
category = 'Transpositions'
sub_category = '> 2 transpositions (same name part)'
entity_type = 'Individual'


# ## download the OFAC list from the web

# In[3]:


ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)


# In[4]:


ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']


# # FILTER FOR THE REQUIREMENTS OF THE TEST CASE TYPE

# ## filter for the requirements of the specific test case type

# In[5]:


ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate individuals


# ## randomly choose 10 rows

# In[6]:


while True:
    ofac_list_sampled = ofac_list_filtered.sample(n = 10)
    cnt = [0] * 10
    for ind, name in enumerate(ofac_list_sampled['name']):
        split_name = name.upper().split(' ')
        
        for i in split_name:
            if all(j not in alphabet() for j in i):
                split_name.remove(i) # remove word with all numbers
            elif len(i) == 1:
                split_name.remove(i) # remove word with only 1 letter
            elif num_of_alphabet(i) > 2:
                cnt[ind] += 1
                break

    if all(i == 1 for i in cnt):
        break

ofac_list_sampled


# # CREATE THE TEST CASES

# ## create blank final test cases table

# In[7]:


final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
final_test_cases


# ## run loop to generate the test cases

# In[8]:


for index, row in ofac_list_sampled.iterrows():
    original_name = row['name'].upper()
    split_original_name = original_name.split(' ') # split name into word
    final_test_name = split_original_name.copy()
    
    for i in split_original_name:
        if all(j not in alphabet() for j in i):
            split_original_name.remove(i) # remove word with all numbers
        elif len(i) < 3:
            split_original_name.remove(i) # remove word with less than 3 letter
        
    while True:
        replace_word = np.random.choice(split_original_name) # randomly choose word to be transposed
        if num_of_alphabet(replace_word) > 2:
            break
    
    if len(replace_word) == 3:
        loop_time = 3
    else:
        loop_time = np.random.randint(3, len(replace_word))
    
    while True:
        for i in range(loop_time):
            random_list = list(range(len(replace_word))) # randomly choose letter to be transposed
            while True:
                random_letter_index = np.random.choice(random_list)
                random_letter = replace_word[random_letter_index]
                if random_letter in alphabet():
                    break
            random_list.remove(random_letter_index) # remove chosen letter index

            random_place = np.random.choice(random_list) # randomly choose place to transpose to

            replace_word_list = list(replace_word)
            del replace_word_list[random_letter_index] # remove chosen letter
            replace_word_list.insert(random_place, random_letter) # add transposed letter

            final_test_name[final_test_name.index(replace_word)] = ''.join(replace_word_list)
            replace_word = ''.join(replace_word_list)

        final_test_name = ' '.join(final_test_name)
        
        if final_test_name != original_name:
            break
        else:
            final_test_name = final_test_name.split(' ')
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

