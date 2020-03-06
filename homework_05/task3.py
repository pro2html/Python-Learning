import sys

words_list   = []
counter_list = []

filename = sys.argv[1]
f = open(filename, 'r')
f.close

for line in f:
    for word in line.split(' '):
        words_list.append(word)

for num, name in enumerate(words_list):
    counter_list.append(words_list.count(words_list[num]))

def words_counter(word, iterable):
    return (word, iterable)

people_list = dict(map(words_counter, words_list, counter_list))

print(str(people_list))

