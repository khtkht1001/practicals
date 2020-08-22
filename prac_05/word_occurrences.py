word_count = {}
text = input("Text: ")
words = text.split()
for each_word in words:
    count = word_count.get(each_word, 0)
    word_count[each_word] = count + 1
words = list(word_count.keys())
words.sort()
longest_word = max(len(each_word) for each_word in words)
for each_word in words:
    print("{:<{}}:{}".format(each_word, longest_word, word_count[each_word]))
