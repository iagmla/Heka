''' Word Scroll '''
''' by Karl Zander '''
''' For use with all caps A-Z letters only '''

def word_scroll(word, depth):
    word_len = len(word)
    scroll = []
    scroll.append(word)
    for x in range(depth):
        new_word = ""
        for y in range(word_len):
            num = ord(scroll[x][y]) - 65
            letter = chr(((num + num) % 26) + 65)
            new_word += letter
        if new_word not in scroll:
            scroll.append(new_word)
        else:
            break
    return scroll
