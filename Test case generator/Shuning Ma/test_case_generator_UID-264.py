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


uid = 'UID-264' 
theme = 'Names where name parts are Modified'
category = 'Truncation'
sub_category = '> 2 Letter Truncation in a middle name part'
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
            elif len(i) <= 3:
                split_name.remove(i) # remove word with <= 3 letter
                
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
    
    split_edit_name = []
    for i in split_original_name:
        if (not all(j not in alphabet() for j in i)) & (num_of_alphabet(i) > 3):
            split_edit_name.append(i) # remove word with all numbers # remove word with <= 3 letter
    
    truncate_word = split_edit_name[len(split_edit_name) // 2] # choose word to be truncated
    truncate_number = np.random.randint(3, len(truncate_word))
        
    final_test_name[final_test_name.index(truncate_word)] = truncate_word[:len(truncate_word) - truncate_number]

    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

