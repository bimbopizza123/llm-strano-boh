import json
import random

try:
    with open('words.json', 'r', encoding='utf-8') as file:
        words = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    words = {}

def r():
    text1 = input("| ")
    text = text1.split()
    
    if len(text) < 2:
        print("| ")
        return


    for i in range(len(text) - 1):
        pword = text[i]    
        word = text[i + 1]  
        
        if pword not in words:
            words[pword] = {}
            
   
        if word in words[pword]:
            words[pword][word] += 1
        else:
            words[pword][word] = 1

    print("Dizionario aggiornato:", words)

    with open('words.json', 'w', encoding='utf-8') as file:
        json.dump(words, file, ensure_ascii=False, indent=4)


import random

def w():
    if not words:
        print("nooooo! dfhsdgcdbj")
        return


    current_word = random.choice(list(words.keys()))
    sentence_length = 20
    result = [current_word]

    for _ in range(sentence_length - 1):
        
        if current_word in words and words[current_word]:
           
            successors = list(words[current_word].keys())
            weights = list(words[current_word].values())
            
          
            next_word = random.choices(successors, weights=weights, k=1)[0]
            
            result.append(next_word)
            current_word = next_word
        else:
            break

    for word in result:
        print(word, end=" ")


def thing():
    x = input("")
    if x == "r":
        r()
    else:
        w()    

thing()