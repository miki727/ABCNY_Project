#!/usr/bin/env python
# coding: utf-8

# # IMPORT DATA, PACKAGES, AND FUNCTIONS

# ## import the relevant functions and packages

# In[1]:


import pandas as pd
import numpy as np
from test_case_generator_functions import alphabet, num_of_alphabet, rand_letter


# # TEST CASE TYPE REFERENCE INFORMATION

# In[2]:


uid = 'UID-313' 
theme = 'Names where name parts are Modified'
category = 'Typos'
sub_category = '2 Typos same name part - Non-adjacent'
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
            if num_of_alphabet(i) >= 4:
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
    
    split_edit_name = []
    for i in split_original_name:
        if not all(j not in alphabet() for j in i):
            split_edit_name.append(i) # remove word with all numbers
    
    while True:
        replace_word = np.random.choice(split_edit_name) # randomly choose word to be replaced
        if num_of_alphabet(replace_word) >= 4:
            break
    
    random_list = list(range(len(replace_word))) 
    replace_word_list = list(replace_word)

    if replace_word_list[-1] not in alphabet():
        del random_list[-3:]
    else:
        del random_list[-2:]
        
    rand_letter_index = np.random.choice(random_list) # randomly choose beginning letter to be replaced

    for i in range(0, 3, 2):
        while replace_word_list[rand_letter_index + i] == replace_word[rand_letter_index + i]: # rerandom if no letter has been replaced
            replace_word_list[rand_letter_index + i] = rand_letter() # replace letter

    final_test_name[final_test_name.index(replace_word)] = ''.join(replace_word_list)
    
    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

