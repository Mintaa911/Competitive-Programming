def sort_sentence(s):
    shuffled = s.split(' ')
    arranged = ["" for i in range(len(shuffled))]
    
    for word in shuffled:
        place = int(word[len(word)-1])
        arranged[place-1] = word[:len(word)-1]
    
    return " ".join(arranged)