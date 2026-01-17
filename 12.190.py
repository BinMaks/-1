sentence = input("Введите предложение: ")
words = sentence.split()
result_words = []
for word in words:
    word = word.replace('а', 'о', 1)
    last_char = word[-1]
    word = last_char + ''.join(char for char in word[:-1] if char != last_char)
    seen = set()
    filtered_word = ''
    for char in word:
        if char not in seen:
            filtered_word += char
            seen.add(char)
    word = filtered_word
    result_words.append(word)
longest_word_idx = max(range(len(result_words)), key=lambda i: len(result_words[i]))
longest_word = result_words[longest_word_idx]
mid = len(longest_word) // 2
if len(longest_word) % 2 == 0:
    longest_word = longest_word[:mid-1] + longest_word[mid+1:]
else:
    longest_word = longest_word[:mid] + longest_word[mid+1:]
result_words[longest_word_idx] = longest_word
print("Преобразованное предложение:", ' '.join(result_words))