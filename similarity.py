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

# Reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # Skipping the header
            documents.append(row)

# Identify each distinct word in the collection
distinct_words = set()
for doc in documents:
    words = doc[1].split()  # Split the text by spaces
    distinct_words.update(words)

# Sort the distinct words
sorted_distinct_words = sorted(distinct_words)

# Create a dictionary for each row to count the number of instances of each word
docTermMatrix = []
for doc in documents:
    word_count = {word: 0 for word in sorted_distinct_words}
    words = doc[1].split()
    for word in words:
        word_count[word] += 1
    docTermMatrix.append(word_count)

highest_sim = 0
most_sim_docs = (0, 0)

# Convert the dictionaries to lists of values based on sorted distinct words
doc_vectors = [list(word_count.values()) for word_count in docTermMatrix]

for i in range(len(doc_vectors)):
    for j in range(i + 1, len(doc_vectors)):  # Only compare each pair once
        x = doc_vectors[i]
        y = doc_vectors[j]
        sim = cosine_similarity([x], [y])[0][0]
        if sim > highest_sim:
            highest_sim = sim
            most_sim_docs = (i, j)

# Print the highest cosine similarity following the information below
print(f"The most similar documents are document {most_sim_docs[0] + 1} and document {most_sim_docs[1] + 1} with cosine similarity = {highest_sim}")