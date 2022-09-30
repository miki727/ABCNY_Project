#!/usr/bin/env python
# coding: utf-8

# # -----------------------------------
# # TEST CASE TYPE REFERENCE INFORMATION
# # -----------------------------------
# 
# uid = 'UID-550' 
# theme = 'Name Deletions'
# category = 'Name Part in the Middle'
# sub_category = '>2 Name Parts removed'
# entity_type = 'Vessel'
# 
# # ********************

# In[116]:


uid = 'UID-550' 
theme = 'Name Deletions'
category = 'Name Part in the Middle'
sub_category = '>2 Name Parts removed'
entity_type = 'Vessel'


# In[117]:


def separate_words_in_name_(name):
    first_word = name[:name.find(' ')]
    last_word = name[name.find(' ',
                               name.find(' ',
                                         name.find(' ',
                                                   name.find(' ')+2)+2)+2)+1:]

    separated_words = [first_word, last_word]
    
    return separated_words


# In[118]:


import pandas as pd

ofac_list_download = pd.read_csv('https://www.treasury.gov/ofac/downloads/sdn.csv', header=None)
ofac_list = ofac_list_download[[0,1,2]]
ofac_list.columns = ['uid', 'name', 'entity_type']


# In[119]:


ofac_list


# In[139]:



ofac_list_filtered_draft = ofac_list[(ofac_list.entity_type == 'vessel')] # only evaluate individuals


# In[140]:


ofac_list_filtered_draft


# In[141]:


ofac_list_filtered_draft = ofac_list_filtered_draft[(ofac_list_filtered_draft.name.str.count(' ') > 2)] # only evaluate names with more than 2 words
ofac_list_filtered_draft


# In[142]:


ofac_list_filtered = ofac_list[(ofac_list.entity_type == 'vessel')] # only evaluate individuals
ofac_list_filtered = ofac_list_filtered[(ofac_list_filtered.name.str.count(' ') > 3)] # only evaluate names with more than 2 words


# In[143]:


ofac_list_filtered


# In[144]:


# Because we only have two variables that have more than 3 words in name, we use this two as sample


# In[145]:


ofac_list_sampled = ofac_list_filtered.sample(n = 2)
ofac_list_sampled


# In[146]:


# create blank final test cases table

final_test_cases = pd.DataFrame(columns=['UID', 'Theme','Category','Sub-category','Entity-Type','Test Case ID' , 'OFAC List UID', 'Original Name','Test Case Name'])
final_test_cases


# In[147]:



# run loop to generate the test cases

for index, row in ofac_list_sampled.iterrows():
   
    number_of_words = row['name'].count(' ') + 1 # determine for each name the number of words
    
    if number_of_words == 5:
        separated_words = separate_words_in_name(row['name']) # separate the name into distinct words
        final_test_name = separated_words[0] + ' ' + separated_words[1] # create the test case
        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe
        
    if number_of_words == 6:
        separated_words = separate_words_in_name(row['name']) # separate the name into distinct words
        final_test_name = separated_words[0] + ' ' + separated_words[1]  # create the test case
        
        final_test_cases.loc[len(final_test_cases)] = [uid, theme, category, sub_category, entity_type, uid + ' - ' + str(index), row['uid'], row['name'], final_test_name] # append to the dataframe


# In[148]:


final_test_cases


# In[ ]:




