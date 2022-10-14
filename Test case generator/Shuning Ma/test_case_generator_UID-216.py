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


uid = 'UID-216' 
theme = 'Names where name parts are Modified'
category = 'Phonetic'
sub_category = '> 2 phonetic variations - same name part'
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
            
        for word in split_name:
            if len(word) <= 2:
                break
            cnt[ind] = num_of_phonetic(word)
            if cnt[ind] > 2:
                break
    
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
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    split_original_name = original_name.split(' ') # split name into word
    
    final_test_name = split_original_name.copy()
    
    modify_original_name = np.random.choice(split_original_name) # randomly choose word to be replaced
    while (all(i not in alphabet() for i in modify_original_name)) | (num_of_phonetic(modify_original_name) <= 2):
        modify_original_name = np.random.choice(split_original_name)
    
    modify_index = split_original_name.index(modify_original_name) # record index of chosen word

    replace_name = list(modify_original_name) # split word into letter

    random_list = list(range(len(replace_name)))
    random_time = np.random.randint(2, num_of_phonetic(modify_original_name))
    for i in range(random_time):
        j = np.random.choice(random_list)
        while replace_name[j] == modify_original_name[j]: # rerandom if no letter has been replaced
            j = np.random.choice(random_list)
            random_list.remove(j)
            replace_name[j] = phonetic(replace_name[j]) # replace with similar phonetic

    final_test_name[modify_index] = ''.join(replace_name)
    
    final_test_name = ' '.join(final_test_name)
    
    final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe


