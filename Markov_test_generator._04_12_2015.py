# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 15:57:45 2015

@author: Alexander
"""
from collections import Counter
import random
import pickle
    
def random_choice_of_one_word(counter, ignorable_signs):
    max_time = Counter(counter).most_common(1)[0][1]
    dimension = random.choice(range(max_time))
    candidates = [key for key, value in counter.iteritems() if value >= dimension and key not in ignorable_signs]
    if len(candidates) > 0:
        return random.choice(candidates)    


def choose_next_by_previous_one_words(current_word, two_words_statistic):
    counter = {}    
    for word, value in two_words_statistic.iteritems(): 
        if word[0] == current_word:
            counter[word] = value    
    max_time = Counter(counter).most_common(1)[0][1]
    dimension = random.choice(range(max_time ))
    candidates = [key[1] for key, value in counter.iteritems() if value > dimension ]
    if len(candidates) > 0:
        return random.choice(candidates)
    else:
        return ""    


def choose_next_by_previous_two_words(tuple_of_words, three_words_statistic):
    counter = {}    
    for word, value in three_words_statistic.iteritems(): 
        if (word[0], word[1]) == tuple_of_words:
            counter[word] = value    
    max_time = Counter(counter).most_common(1)[0][1]
    dimension = random.choice(range(max_time))
    candidates = [key[2] for key, value in counter.iteritems() if value > dimension]
    if len(candidates) > 0:
        return random.choice(candidates)
    else:
        return choose_next_by_previous_one_words(tuple_of_words[1],two_words_statistic)    
        
    
def create_sentence(one_word_statistic, two_words_statistic, three_words_statistic):
    output = []    
    ignorable_signs = [ ".", "!", "?", " ", "'", "`","\n", "\t"]
    possible_end_signs = [".", "!", "?"]
    first = random_choice_of_one_word(one_word_statistic, ignorable_signs)
    second = choose_next_by_previous_one_words(first, two_words_statistic)
    if second in possible_end_signs:
        output.append(first)
        output.append(second)
    else:
        third = choose_next_by_previous_two_words((first, second), three_words_statistic)
        if third in possible_end_signs:
            output.append(first)
            output.append(second)
            output.append(third)
        else:
            while third not in possible_end_signs:
                first, second = second, third
                third = choose_next_by_previous_two_words((first, second), three_words_statistic)
                output.append(third)        
    print  str(output[0].title()) + " " + " ".join(output[1:-1]) + str(output[-1])        
    
def create_text(number_of_sentence, one_word_statistic, two_words_statistic, three_words_statistic):
    while(number_of_sentence):
        create_sentence(one_word_statistic, two_words_statistic, three_words_statistic)
        number_of_sentence -= 1    


if __name__ == "__main__":
    with open('C:\\dickens\\stat\\all_words_2.pickle', 'r') as result:
          one_word_statistic = pickle.load(result)      
    with open('C:\\dickens\\stat\\stat_two_words_2.pickle', 'r') as result:
          two_words_statistic = pickle.load(result)      
    with open('C:\\dickens\\stat\\stat_three_words_2.pickle', 'r') as result:
          three_words_statistic = pickle.load(result)
    #create_text(3, one_word_statistic, two_words_statistic, three_words_statistic)  
    create_text(35, one_word_statistic, two_words_statistic, three_words_statistic)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        