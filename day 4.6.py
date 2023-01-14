def removeChar(s, c):
    # find total no. of
    # occurrence of character
    counts = s.count(c)

    # convert into list
    # of characters
    s = list(s)

    # keep looping until
    # counts become 0
    while counts:
        # remove character
        # from the list
        s.remove(c)

        # decremented by one
        counts -= 1

    # join all remaining characters
    # of the list with empty string
    s = ''.join(s)

    print(s)


# Driver code
if __name__ == '__main__':
    s = "hello world"
    removeChar(s, 'l')
