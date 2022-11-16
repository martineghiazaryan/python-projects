#how to do string concatination
#let's say I want to have a string like 'subscribe to ________'

# youtuber = 'Martiros' 

# print('subscribe to ' + youtuber)
# print('subscribe to {}'.format(youtuber))
# print(f'subscribe to {youtuber}')

adj1 = input('Adjective: ')
noun1 = input('Noun: ')
verb1 = input('Verb (Past tense): ')
adverb1 = input('Adverb: ')
adj2 = input('Adjective: ')
noun2 = input('Noun: ')
noun3 = input('Noun: ')
adj3 = input('Adjective: ')
verb2 = input('Verb: ')
adverb2 = input('Adverb: ')
verb3 = input('Verb (Past tense): ')
adj4 = input('Adjective: ')


madlib = f'Today I went to the zoo. I saw a(n) {adj1} {noun1} jumping up and down in its tree. He {verb1} {adverb1} through the large tunnel that led to its {adj2} {noun2}. I got some peanuts and passed them through the cage to a gigantic gray {noun3} towering above my head. Feeding that animal made me hungry. I went to get a {adj3} scoop of ice cream. It filled my stomach. Afterwards I had to {verb2} {adverb2} to catch our bus. When I got home I {verb3} my mom for a {adj4} day at the zoo.'


print(madlib)