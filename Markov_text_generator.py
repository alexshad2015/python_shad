import random
import pickle
    
def choose_next_by_previous_one_word(current_word, two_words_statistic):
    selection = [word for word in two_words_statistic if word[0] == current_word]
    candidates = []
    if len(selection) > 0:
        candidates = [word[1] for word in selection if \
        two_words_statistic[word] == max([two_words_statistic[word] for word in selection])]
        return random.choice(candidates)
    else:    
        return ""
        

def choose_next_by_previous_two_words(tuple_of_words, three_words_statistic):
    selection = [word for word in three_words_statistic if (word[0], word[1]) == tuple_of_words]
    candidates = []
    if len(selection) > 0:
        candidates = [word[2] for word in selection if three_words_statistic[word] > \
        max([three_words_statistic[word] for word in selection]) - 1]
        return random.choice(candidates)
    else:    
        return choose_next_by_previous_one_word(tuple_of_words[1], two_words_statistic)
        
    
def create_sentence(one_word_statistic, two_words_statistic, three_words_statistic):
    output = []    
    list_of_signs = [ ".", "!", "?"]
    random.shuffle(one_word_statistic)
    first = one_word_statistic[0]
    while first in list_of_signs or first == "'" or first == " `" or first == " ":
        random.shuffle(one_word_statistic)
        first = one_word_statistic[0]
    second = choose_next_by_previous_one_word(first, two_words_statistic)
    if second in list_of_signs:
        output.append(first)
        output.append(second)
    else:
        third = choose_next_by_previous_two_words((first, second), three_words_statistic)
        if third in list_of_signs:
            output.append(first)
            output.append(second)
            output.append(third)
        else:
            while third not in list_of_signs:
                first, second = second, third
                third = choose_next_by_previous_two_words((first, second), three_words_statistic)
                output.append(third)        
    print  str(output[0].title()) + " " + " ".join(output[1:-1]) + str(output[-1])        
    
def create_text(number_of_sentence, one_word_statistic, two_words_statistic, three_words_statistic):
    while(number_of_sentence):
        create_sentence(one_word_statistic, two_words_statistic, three_words_statistic)
        number_of_sentence -= 1


if __name__ == "__main__":
    with open('C:\\Users\\Alexander\\Downloads\\test\\dickens\\stat\\all_words.pickle', 'r') as result:
          one_word_statistic = pickle.load(result)      
    with open('C:\\Users\\Alexander\\Downloads\\test\\dickens\\stat\\stat_two_words.pickle', 'r') as result:
          two_words_statistic = pickle.load(result)      
    with open('C:\\Users\\Alexander\\Downloads\\test\\dickens\\stat\\stat_three_words.pickle', 'r') as result:
          three_words_statistic = pickle.load(result)
    create_text(30, one_word_statistic, two_words_statistic, three_words_statistic)
