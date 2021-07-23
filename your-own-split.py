def mysplit(strng):
    if strng.isspace(): return []# return [] if string is empty or contains whitespaces only
    out_list = []                # prepare a list to return
    current_word = ""            # prepare a word to build subsequent words
    strng += " "                 # funny decision. Final word was missed without it
    for ch in strng:             # iterate through all the characters in string
        if ch.isspace():         # if we found space (unprintable character)
            if len(current_word)!=0:            # if there is a word in our buffer
                out_list.append(current_word)   # add this word to output
                current_word = ""               # and clear our buffer
        else:                                   # if we found valuable character (printable)
            current_word += ch                  # add it to the buffer
    return out_list                             # job complete. Return list of words


####   here are some test cases   ####
##print(mysplit("To be or not to be, that is the question"))
##print(mysplit("To be or not to be,that is the question"))
##print(mysplit("   "))
##print(mysplit(" abc "))
##print(mysplit(""))
