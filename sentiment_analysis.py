import re
import pandas as pd
from pathlib import Path

def processing_words(word):
    #change to uppercase
    word = word.upper()
    #remove all special characters
    word = re.sub(r'[^A-Z]', '', word)
    return word

#Loughran-McDonald dictionary
word_dictionary = pd.read_csv('Loughran-McDonald_MasterDictionary_1993-2025.csv')
word_dictionary.set_index('Word', inplace=True)
columns = ["Negative", "Positive", "Uncertainty", "Litigious", 
    "Strong_Modal", "Weak_Modal", "Constraining", "Complexity"]


results_list = []
#looping through each text file in the folder in sorted order
for file in sorted(Path("data/").rglob('*.txt')):
    #file names are "Company X - CEO.txt"
    file_name = file.stem
    #company name is left side of the string "-"
    company_name = file_name.split(" - ")[0]
    print(company_name)
    
    #word counts to zero for each file
    n_negative = 0
    n_positive = 0
    n_uncertainty = 0
    n_litigious = 0
    n_strong = 0
    n_weak = 0
    n_constraining = 0
    word_count = 0
    
    #processsing the text files
    with open(file, "r", encoding="utf-8-sig") as f:
        text = f.read()
        #text to words
        words = text.split()
        #loop each word
        for w in words:
            #process the words to match dictionary
            processed_word = processing_words(w)
            #Loughran-McDonald do not count one-letter words, as they are not critical content words
            if len(processed_word) >= 2:
                word_count += 1
                #find the row in the dictionary if the word exists there
                if processed_word in word_dictionary.index:
                    row = word_dictionary.loc[processed_word]
                
                    if row['Negative'] > 0:
                        n_negative += 1
                    if row['Positive'] > 0:
                        n_positive += 1
                    if row['Uncertainty'] > 0:
                        n_uncertainty += 1
                    if row['Litigious'] > 0:
                        n_litigious += 1
                    if row['Strong_Modal'] > 0:
                        n_strong +=1
                    if row['Weak_Modal'] > 0:
                        n_weak +=1
                    if row['Constraining'] > 0:
                        n_constraining +=1

        #changing the values to proportions
        p_negative = n_negative/word_count
        p_positive = n_positive/word_count
        p_uncertainty = n_uncertainty/word_count
        p_litigious = n_litigious/word_count
        p_strong = n_strong/word_count
        p_weak = n_weak/word_count
        p_constraining = n_constraining/word_count
        
        #results dictionary
        company_data = {
            "Company": company_name,
            "Negative": p_negative,
            "Positive": p_positive,
            "Uncertainty": p_uncertainty,
            "Litigious": p_litigious,
            "Strong_Modal": p_strong,
            "Weak_Modal": p_weak,
            "Constraining": p_constraining,
            "Word_Count": word_count
        }
        
        #add results to the list
        results_list.append(company_data)
        
#list to dataframe
results_df = pd.DataFrame(results_list)
#df to csv
results_df.to_csv('sentiment_analysis.csv', index=False, encoding='utf-8-sig')
        
        
            



    

