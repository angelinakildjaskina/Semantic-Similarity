# This program reads in movies and their descriptions
# Find the most similar movie to the reference

# Importing spacy and specifying the language model
import spacy 
nlp = spacy.load('en_core_web_md')

# Planet Hulk movie description
reference = '''
Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator
'''

# Reading from the file
with open('movies.txt', 'r') as f:

    descriptions = {}

    # Appending each movie to a dictionary
    for line in f:
        line = line.strip().split(':')
        descriptions[line[0]] = line[1]

# Comparing the descriptions
model_desc = nlp(reference)

similarities = {}

# Appending each movie and its similarity to Planet Hulk to a dictionary
for key in descriptions:
    similarity = nlp(descriptions[key]).similarity(model_desc)
    similarities[key] = similarity

# Finding the key (Movie name) of the most similar discription
max_sim = max(similarities, key=similarities.get)
print(f'The movie that\'s most similar to Planet Hulk is {max_sim}.')
    