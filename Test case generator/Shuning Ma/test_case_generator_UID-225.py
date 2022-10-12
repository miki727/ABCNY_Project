#!/usr/bin/env python
# coding: utf-8

# # IMPORT DATA, PACKAGES, AND FUNCTIONS

# ## import the relevant functions and packages

# In[1]:


import pandas as pd
import numpy as np
from test_case_generator_functions import alphabet


# # TEST CASE TYPE REFERENCE INFORMATION

# In[2]:


uid = 'UID-225' 
theme = 'Names where name parts are Modified'
category = 'Repetitions'
sub_category = '> 2 letters repeated once'
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


ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'individual')] # only evaluate entities


# ## randomly choose 10 rows

# In[6]:


while True:
    ofac_list_sampled = ofac_list_filtered.sample(n = 10)
    cnt = [0] * 10
    for ind, name in enumerate(ofac_list_sampled['name']):
        split_name = name.split(' ')
        
        for i in split_name:
            if all(j not in alphabet() for j in i):
                split_name.remove(i) # remove word with all numbers
                
        cnt[ind] += len(split_name)

    if all(i > 2 for i in cnt):
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
    
    if len(split_original_name) == 3:
        loop_time = 3
    else:
        loop_time = np.random.randint(3, len(split_original_name))
        
    for i in range(loop_time):
        replace_word = np.random.choice(split_original_name) # randomly choose word to be replaced
        split_original_name.remove(replace_word) # remove chosen word
        
        replace_word_list = list(replace_word)
        repeat_list = [] # get index of alphabets in each word
        for i in range(len(replace_word)):
            if replace_word[i] in alphabet():
                repeat_list.append(i)
        
        random_index = np.random.choice(repeat_list) # randomly choose letter to be repeated
        
        replace_word_list[random_index] += replace_word_list[random_index] # add repeated letter
        
        final_test_name[final_test_name.index(replace_word)] = ''.join(replace_word_list)

    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

