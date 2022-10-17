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


uid = 'UID-290' 
theme = 'Names where name parts are Modified'
category = 'Typos'
sub_category = '> 2 Typos same name part - Adjacent'
entity_type = 'Entity'


# ## download the OFAC list from the web

# In[3]:


ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list_download


# In[4]:


ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']
ofac_list


# # FILTER FOR THE REQUIREMENTS OF THE TEST CASE TYPE

# ## filter for the requirements of the specific test case type

# In[5]:


ofac_list_filtered = ofac_list[(ofac_list.entity_type == '-0- ')] # only evaluate entities
ofac_list_filtered


# ## randomly choose 10 rows

# In[6]:


while True:
    ofac_list_sampled = ofac_list_filtered.sample(n = 10)
    cnt = [0] * 10
    for ind, name in enumerate(ofac_list_sampled['name']):
        split_name = name.upper().split(' ')
        
        for i in split_name:
            if (len(split_name) == 2) & (len(split_name[0]) <= 4):
                break
            elif (len(split_name) == 2) & (len(split_name[-1]) <= 4):
                break
                
            if all(j not in alphabet() for j in i):
                split_name.remove(i) # remove word with all numbers
            elif num_of_alphabet(i) > 3:
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
        if num_of_alphabet(replace_word) > 3:
            break
    
    random_list = list(range(len(replace_word))) 
    replace_word_list = list(replace_word)
    if final_test_name.index(replace_word) == 0: # avoid the at the beginning situation
        del random_list[0] 
        del random_list[-2:]
        
        rand_letter_index = np.random.choice(random_list) # randomly choose beginning letter to be replaced

        if len(random_list) == 1:
            random_length = 2
        else:
            random_length = np.random.randint(2, len(replace_word_list) - rand_letter_index)
    
        for i in range(random_length + 1):
            while replace_word_list[rand_letter_index] == replace_word[rand_letter_index]: # rerandom if no letter has been replaced
                replace_word_list[rand_letter_index] = rand_letter() # replace letter
            rand_letter_index += 1
    
    elif final_test_name.index(replace_word) == len(final_test_name) - 1: # avoid the at the end situation
        if replace_word_list[-1] not in alphabet():
            del random_list[-2:]
        else:
            del random_list[-1]
        del random_list[:2]
        
        rand_letter_index = np.random.choice(random_list) # randomly choose end letter to be replaced

        if len(random_list) == 1:
            random_length = 2
        else:
            random_length = np.random.randint(2, rand_letter_index + 1)
    
        for i in range(random_length + 1):
            while replace_word_list[rand_letter_index] == replace_word[rand_letter_index]: # rerandom if no letter has been replaced
                replace_word_list[rand_letter_index] = rand_letter() # replace letter
            rand_letter_index -= 1
    
    else:
        del random_list[-2:]
        
        rand_letter_index = np.random.choice(random_list) # randomly choose beginning letter to be replaced

        if len(random_list) == 1:
            random_length = 2
        else:
            random_length = np.random.randint(2, len(replace_word_list) - rand_letter_index)
    
        for i in range(random_length + 1):
            while replace_word_list[rand_letter_index] == replace_word[rand_letter_index]: # rerandom if no letter has been replaced
                replace_word_list[rand_letter_index] = rand_letter() # replace letter
            rand_letter_index += 1

    final_test_name[final_test_name.index(replace_word)] = ''.join(replace_word_list)
    
    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

