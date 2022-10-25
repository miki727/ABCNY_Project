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


uid = 'UID-247' 
theme = 'Names where name parts are Modified'
category = 'Transpositions'
sub_category = '1 transposition - 2 letters Any where'
entity_type = 'Entity'


# ## download the OFAC list from the web

# In[3]:


ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)


# In[4]:


ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']


# # FILTER FOR THE REQUIREMENTS OF THE TEST CASE TYPE

# ## filter for the requirements of the specific test case type

# In[5]:


ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities


# ## randomly choose 10 rows

# In[6]:


while True:
    ofac_list_sampled = ofac_list_filtered.sample(n = 10)
    cnt = [0] * 10
    for ind, name in enumerate(ofac_list_sampled['name']):
        
        if len(name) > 10:
            cnt[ind] += 1

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
    
    while True:
        replace_word = np.random.choice(split_original_name) # randomly choose word to be transposed
        if num_of_alphabet(replace_word) < 2:
            continue
        
        replace_word_list = list(replace_word)
        replace_word_index = list(range(len(replace_word)))
        replace_index = np.random.choice(replace_word_index) # choose letter to be transposed
        
        if replace_word_list[replace_index] not in alphabet():
            continue
        
        if replace_index == 0:
            if replace_word_list[1] not in alphabet():
                continue
            else:
                replace_word_list.insert(0, replace_word_list.pop(1)) # transpose
        
        elif replace_index == len(replace_word_list) - 1:
            if replace_word_list[-2] not in alphabet():
                continue
            else:
                replace_word_list.insert(-1, replace_word_list.pop(-2)) # transpose
        
        else:
            if (replace_word_list[replace_index + 1] not in alphabet()) & (replace_word_list[replace_index - 1] not in alphabet()):
                continue
            elif replace_word_list[replace_index + 1] not in alphabet():
                replace_word_list.insert(replace_index, replace_word_list.pop(replace_index - 1)) # transpose
            elif replace_word_list[replace_index - 1] not in alphabet():
                replace_word_list.insert(replace_index, replace_word_list.pop(replace_index + 1)) # transpose
            else:
                random_choice = np.random.choice([-1, 1])
                replace_word_list.insert(replace_index, replace_word_list.pop(replace_index + random_choice)) # transpose
        
        if replace_word == ''.join(replace_word_list):
            continue
        else:
            break

    final_test_name[final_test_name.index(replace_word)] = ''.join(replace_word_list)

    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

