# This program compares stuff

# Importing SpaCy module
import spacy
nlp = spacy.load('en_core_web_md')

# Comparing words
print('\n***Advanced language model***')
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
'''
What's interesting about the similarities between cat, apple, monkey and banana
is that monkey and banana has a very great similarity probability.
Also, monkey and cat have a lower similarity (0.59) than banana and apple (0.66).
I assume that we will have a higher similarity between cat and dog.
Let's try
'''

# Comparing cat and dog
print("\n***Comparing 'cat' and 'dog'***")
tokens = nlp('cat dog ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Indeed, cat and dog have a much higher similarity (0.82)
        
# Running the first example with a simpler language model
slp = spacy.load('en_core_web_sm')
tokens = slp('cat apple monkey banana ')
print('\n***Simpler model***')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

'''
I got a warning:
The model you're using has no word vectors loaded, so the result of the 
Token.similarity method will be based on the tagger, parser and NER, 
which may not give useful similarity judgements.

I got strange similarity probs, such as: apple monkey 0.6756038665771484
'''

        
# Comparing sentences
# Reference sentence
sentence_to_compare = "Why is my cat on the car"

# Sentences to compare
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# Using nlp and similarity method
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ",  similarity)
      

