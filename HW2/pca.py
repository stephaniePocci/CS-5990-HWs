# -------------------------------------------------------------------------
# AUTHOR: Stephanie Pocci
# FILENAME: pca.py
# SPECIFICATION: PCA for HW 2
# FOR: CS 5990 (Advanced Data Mining) - Assignment #2
# TIME SPENT: 35 minutes
# -----------------------------------------------------------*/

#importing some Python libraries
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#Load the data
#--> add your Python code here
df = pd.read_csv('heart_disease_dataset.csv')

#Create a training matrix without the target variable (Heart Disease)
# Assuming all columns are features since there is no target variable
df_features = df.copy()

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_features)

#Get the number of features
num_features = df_features.shape[1]

# Run PCA for 9 features, removing one feature at each iteration
for i in range(num_features):
    # Create a new dataset by dropping the i-th feature
    reduced_data = df_features.drop(df_features.columns[i], axis=1)

    # Run PCA on the reduced dataset
    pca = PCA()
    pca.fit(reduced_data)

    #Store PC1 variance and the feature removed
    #Use pca.explained_variance_ratio_[0] and df_features.columns[i] for that
    print("PC1 variance: ", pca.explained_variance_ratio_[0], "Feature removed: ", df_features.columns[i])

# Find the maximum PC1 variance
# --> add your Python code here
max_variance = max(pca.explained_variance_ratio_)

#Print results
#Use the format: Highest PC1 variance found: ? when removing ?
print("Highest PC1 variance found: ", max_variance, "when removing", df_features.columns[i])





