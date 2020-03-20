'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    letter = 0
    count = 0
    if len(word) <= 1:
        return count
    elif len(word) == 0:
        return count
    else:
        if word[letter] + word[letter+1] == 'th':
            count += 1
            letter += 1
            word = word[letter:]
            count += count_th(word)
        else: 
            letter += 1
            word = word[letter:]
            count += count_th(word)
    return count
