from funcs import *
  
        
# set difficulty
tries = get_num_tries()

# select random word
word = get_random_word()
#print(word)

gaps = ['*' for letter in word]
wrong = []
remaining = set(ascii_lowercase)
word_solved = False

while(tries > 0 and not word_solved):
    # print game state
    print_state(tries, wrong, gaps)
    
    
    # get next letter guess
    next_l = (input("Choose next letter: ")).lower()
    
    # check letter in word
    if next_l in word:
        # guess correct
        print(f"{next_l} is in the word!")
        for i in range(len(word)):
            if word[i] == next_l:
                gaps[i] = next_l
        
        # word solved?        
        if '*' not in gaps:
            word_solved = True
            
            
    else:
        # guess not correct
        print(f"{next_l} is not in the word!")
        tries -= 1
        wrong.append(next_l)

print(f'The word is {word}')

if word_solved:
    print('you win!')
else:
    print('try again next time')

          
            
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    