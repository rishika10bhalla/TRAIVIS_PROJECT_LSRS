# TRAIVIS_PROJECT_LSRS
## Problem Statement
This project aims to develop a Learning Style Recommender System (LSRS) that can analyze and identify the learning styles of students based on their preferences, aptitudes, and cognitive characteristics. The LSRS should leverage machine learning algorithms and techniques to process and analyze various data sources, such as student profiles, academic performance data, self-assessment questionnaires, and teacher feedback. The project model is in light of the Felder and Silverman Learning Style Model (FSLSM) as it is a widely used model that has proven to be suitable for use in traditional educational systems.
## Dataset Columns
The dataset includes the following 12 columns:
ABC: area before content
D: definitions
C: detailed content
AAC: activity questions
A: area after content( summaries, revision exercises)
V: content pages with visual illustrations 
ABC_T: time on area before content
D_T: time spent on definitions
C_T: time spent on detailed content
AAC_T: time spent on activity questions
A_T: time spent on area after content(summaries, revision exercises)
LS: learning style to be predicted
## Target Variable
In the given code, the target variable is represented by the type variable. It is extracted from the LS property of each row in the CSV file. The goal of the code is to train a K-nearest neighbors (KNN) classifier to predict this target variable (type) based on the input data.

In the flow of the code, the type value is stored in the Y array, which represents the target variable values for the corresponding feature vectors in the X array. The KNN classifier is trained using the X and Y arrays, and later used to predict the type for a given input data point.

Essentially, the type variable is the target variable that the code aims to predict using the KNN algorithm.
