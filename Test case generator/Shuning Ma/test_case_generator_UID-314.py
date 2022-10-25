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


uid = 'UID-314' 
theme = 'Names where name parts are Modified'
category = 'Typos'
sub_category = 'Typo noise name parts'
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


# In[6]:


ofac_list_filtered = ofac_list_filtered.reset_index(drop = True)
ofac_list_filtered_noise = pd.DataFrame(columns=['uid', 'name', 'entity_type'])

noise = ['BANK', 'TRADING', 'STOCK', 'MANUFACTURING', 'SHIPPING', 'TECHNOLOGY', 'PUBLIC', 'MONEY', 'CASH', 'LTD', 'LLC']

for ind, name in enumerate(ofac_list_filtered['name']):
    split_name = name.upper().split(' ')
        
    for i in split_name:
        if i in noise:
            ofac_list_filtered_noise.loc[len(ofac_list_filtered_noise)] = list(ofac_list_filtered.loc[ind])
            break

ofac_list_filtered_noise


# ## randomly choose 10 rows

# In[7]:


ofac_list_sampled = ofac_list_filtered_noise.sample(n = 10)
ofac_list_sampled


# # CREATE THE TEST CASES

# ## create blank final test cases table

# In[8]:


final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
final_test_cases


# ## run loop to generate the test cases

# In[9]:


for index, row in ofac_list_sampled.iterrows():
    original_name = row['name'].upper()
    split_original_name = original_name.split(' ') # split name into word
    
    final_test_name = split_original_name.copy()
    
    for word in split_original_name:
        if word in noise:
            modify_original_name = word # choose word to be replaced

    replace_name = list(modify_original_name) # split word into letter

    j = np.random.choice(list(range(len(replace_name))))
    while modify_original_name[j] not in alphabet(): # rerandom if not letter 
        j = np.random.choice(list(range(len(replace_name))))
    while replace_name[j] == modify_original_name[j]: # rerandom if no letter has been replaced
        replace_name[j] = rand_letter() # replace letter

    final_test_name[final_test_name.index(modify_original_name)] = ''.join(replace_name)

    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe

final_test_cases

