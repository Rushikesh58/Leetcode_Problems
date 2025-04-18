word = "internationalization"
abbr = "i12iz4n"
def validWordAbbreviation(word: str, abbr: str) -> bool:
    wlen = len(word)
    ablen = len(abbr)
    i,j = 0,0
    while i < wlen and j < ablen:
        if word[i] != abbr[j]:
            temp = 0
            while abbr[j].isnumeric() and j < ablen:
                temp =  temp * 10 + int(abbr[j])
                j+=1
            print(temp)
            i += temp
        else:
            i += 1
            j += 1
    return False if i != wlen or j != ablen else True