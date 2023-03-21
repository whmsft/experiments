import re
file = "data.txt"
word = "computer"
with open(file, 'r') as f:
	text = f.read()
words = re.findall(r'\b\w+\b', text)
associated_words = []
for i in range(len(words)):
	if words[i] == word:
		if i > 0:
			associated_words.append(words[i-1])
		if i < len(words)-1:
			associated_words.append(words[i+1])
print(associated_words)