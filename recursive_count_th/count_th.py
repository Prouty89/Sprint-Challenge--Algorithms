'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    if len(word) == 0 or len(word) < len('th'):
        return 0

    # add count
    if word[0:2] == 'th':
        return count_th(word[1:]) + 1

    # must splice, cant just return count
    return count_th(word[1:])
