def count_words(word):
    freq= {}

    for i in word:
        if i in freq:
            freq[i] +=1
        else:
            freq[i]=1
    return freq

print(count_words("aabbccddd"))
