hashed_words = {
    'A': 'Apple',    'a': 'apricot',
    'B': 'Banana',   'b': 'blueberry',
    'C': 'Cherry',   'c': 'cranberry',
    'D': 'Date',     'd': 'dragonfruit',
    'E': 'Elderberry', 'e': 'eggfruit',
    'F': 'Fig',      'f': 'feijoa',
    'G': 'Grape',    'g': 'guava',
    'H': 'Honeydew', 'h': 'huckleberry',
    'I': 'IndianFig','i': 'ichangpapeda',
    'J': 'Jackfruit', 'j': 'jambul',
    'K': 'Kiwi',      'k': 'kumquat',
    'L': 'Lemon',     'l': 'lime',
    'M': 'Mango',     'm': 'melon',
    'N': 'Nectarine', 'n': 'nectar',
    'O': 'Orange',    'o': 'olive',
    'P': 'Papaya',    'p': 'passionfruit',
    'Q': 'Quince',    'q': 'quararibea',
    'R': 'Raspberry',  'r': 'rhubarb',
    'S': 'Strawberry', 's': 'starfruit',
    'T': 'Tangerine',  't': 'tomato',
    'U': 'Uglifruit',  'u': 'ugnifruit',
    'V': 'Violetcurrant', 'v': 'voavanga',
    'W': 'Watermelon',  'w': 'waxapple',
    'X': 'Xigua',       'x': 'ximenia',
    'Y': 'Yellow passionfruit', 'y': 'youngberry',
    'Z': 'Zucchini',     'z': 'ziziphus'
}
def hashfunc(word):
    index = 0
    hesh = ""
    index_letter = ""
    for i in range(len(word)):
        index_letter = word[index]
        hesh += hashed_words[index_letter]
        index += 1

    return hesh

def unhashfunc(heshedword):
    unheshedword = ""
    while heshedword:
        for key, value in hashed_words.items():
            if heshedword.startswith(value):
                unheshedword += key
                heshedword = heshedword[len(value):]
                break
    return unheshedword

a = hashfunc("wordforhash")
b = unhashfunc(a)
print("hashed word: ", a)
print("unhashed word: ", b)
