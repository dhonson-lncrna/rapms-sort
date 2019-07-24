#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def rapms_sort(filename, neg_cap2, exp_cap2):
    '''Sorts out contaminants, all proteins that appear
    in negative control capture2, and proteins that do not
    appear in experimental capture 2. Not useful for quantitative
    analysis, but convenient for gauging the data'''
    # filename is the name of the MS dataset in the local directory
    # neg_cap2 is the name of the column of MS/MS count capture2 of the negative control
    # exp_cap2 is the name of the column of LFQ intensity capture2 of the experimental RAP
    
    # Import pandas and the dataset as a DataFrame
    import pandas as pd
               
    rapms = pd.read_csv('19.07.22_U1-RAP-MS.csv')
    
    #Filter out known contaminants (keratin, etc.)
    for i in rapms['Protein IDs']:
        if 'CON' in i:
            rapms = rapms[rapms['Protein IDs'] != i]
               
    # Filter out all proteins that show up in the second negative control capture
    for i in rapms[neg_cap2]:
        if i != 0:
            rapms = rapms[rapms[neg_cap2] != i]
    
    # Filter out all proteins that don't appear in the second experimental capture
    for i in rapms[exp_cap2]:
        if i == 0:
            rapms = rapms[rapms[exp_cap2] != i]
               
    final_name = filename[:-4] + 'filtered.csv'
    
    rapms.to_csv(final_name)
               
    return rapms

