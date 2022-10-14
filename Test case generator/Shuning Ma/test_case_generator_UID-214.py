#!/usr/bin/env python
# coding: utf-8

# # IMPORT DATA, PACKAGES, AND FUNCTIONS

# ## import the relevant functions and packages

# In[1]:


import pandas as pd
import numpy as np
from test_case_generator_functions import phonetic, alphabet, num_of_phonetic


# # TEST CASE TYPE REFERENCE INFORMATION

# In[2]:


uid = 'UID-214' 
theme = 'Names where name parts are Modified'
category = 'Phonetic'
sub_category = '> 2 phonetic variations - different name part'
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
        split_name = name.upper().split(' ')
        if len(split_name) <= 2:
            break
            
        for word in split_name:
            if num_of_phonetic(word) > 0:
                cnt[ind] += 1
    
    if all(i > 2 for i in cnt):
        break



# # CREATE THE TEST CASES

# ## create blank final test cases table

# In[7]:


final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])


# ## run loop to generate the test cases

# In[8]:


for index, row in ofac_list_sampled.iterrows():
    original_name = row['name'].upper()
    split_original_name = original_name.split(' ') # split name into word
    
    final_test_name = split_original_name.copy()
    
    for i in split_original_name:
        if all(j not in alphabet() for j in i):
            split_original_name.remove(i) # remove word with all numbers
    
    if len(split_original_name) > 3:
        loop_time = np.random.randint(3, len(split_original_name))
    else:
        loop_time = len(split_original_name)
    
    for i in range(loop_time):
        modify_original_name = np.random.choice(split_original_name) # randomly choose word to be replaced
        while num_of_phonetic(modify_original_name) < 1:
            modify_original_name = np.random.choice(split_original_name)
        modify_index = original_name.split(' ').index(modify_original_name) # record index of chosen word
        split_original_name.remove(modify_original_name) # remove chosen word
        
        modify_original_name = list(modify_original_name) # split word into letter
        replace_name = modify_original_name.copy()
        
        j = np.random.choice(list(range(len(replace_name))))
        while replace_name[j] == modify_original_name[j]: # rerandom if no letter has been replaced
            j = np.random.choice(list(range(len(replace_name))))
            replace_name[j] = phonetic(replace_name[j]) # replace 1 letter with similar phonetic
        
        final_test_name[modify_index] = ''.join(replace_name)
    
    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe


