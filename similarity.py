# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy,
#pandas, or other sklearn modules.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity

documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         documents.append (row)
        #  print(row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection without applying any transformations, using
# the spaces as your character delimiter.
# Identify each distinct word in the collection

# Identify each distinct word in the collection
distinct_words = set()
for doc in documents:
    words = doc[1].split()  # Split the text by spaces
    distinct_words.update(words)

# Create a dictionary for each row to count the number of instances of each word
docTermMatrix = []
for doc in documents:
    word_count = {}
    words = doc[1].split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    docTermMatrix.append(word_count)

x = []
y = []
highest_sim = 0
most_sim_docs = (0,0)

for i in range(len(docTermMatrix)):
  for j in range(len(docTermMatrix)):
    if i != j:
      x = docTermMatrix[i]
      y = docTermMatrix[j]
      all_keys = list(set(x.keys()).union(set(y.keys())))
      for key in all_keys:
        if key not in x:
          x[key] = 0
        if key not in y:
          y[key] = 0
      x_sorted = []
      y_sorted = []
      for key in sorted(all_keys):
        x_sorted.append(x[key])
        y_sorted.append(y[key])
      sim = cosine_similarity([x_sorted], [y_sorted])
      if sim > highest_sim:
        highest_sim = sim
        most_sim_docs = (i,j)
      
print("The most similar documents are document", most_sim_docs[0], "and document", most_sim_docs[1], "with cosine similarity =", highest_sim)


# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here


# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here