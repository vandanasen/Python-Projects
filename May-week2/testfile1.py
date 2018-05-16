def remove_vowels():
    sentence = 'the dog is very friendly with my neighbour'
    vowels = 'aeiou'
    non_list = []
    for l in sentence:
        if not l in vowels:
            non_list.append(l)
    nonvowels = ''.join(non_list)
    print (nonvowels)
remove_vowels()
