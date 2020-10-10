'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # base cases

    # blank string
    if len(word) <= 0 :
        return 0

    # String of one character cannot contain "th"
    if len(word) == 1:
        return 0

    # String of 2 characters may contain "th"
    if len(word) == 2:
        if word == "th":
            return 1
        else: return 0

    # If word contains more than 2 letters, break word in half and recurse into them
    l = len(word) //2
    front = word[:l]
    back = word[l:]
    th = 0
    th += count_th(front)
    th += count_th(back)

    # after breaking, new "th" may be found at the border of front and back
    candidate = front[-1] + back[0]
    if candidate == "th":
        return  th + 1
    else:
        return th






