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
## Working: 
This code is a JavaScript module that exports a function called getType.

Here's a step-by-step explanation of what the code does:

It imports two modules: ml-knn and fs. ml-knn is a machine learning library for k-nearest neighbors algorithm, and fs is a module for working with the file system.

It defines a helper function called csvJSON which converts a CSV string into a JSON object. This function takes a CSV string as input, splits it into lines, extracts the headers from the first line, and then creates an array of objects where each object represents a row in the CSV file. The keys of the objects are the headers, and the values are the corresponding values in each row.

The getType function is exported, which takes an input parameter.

The function reads a CSV file located at a specific path using the fs module.

The CSV data is converted to a JSON object using the csvJSON helper function defined earlier.

The function creates an empty set called types.

It iterates over each row in the JSON data, checks if the LS property (assuming it represents a type) is defined, and adds it to the types set. This set is used to determine the unique types in the dataset.

The types set is converted to an array using the spread operator [...types] and stored in the typesArray variable.

The function iterates over each row in the JSON data again. It converts the values of each row (excluding the LS property) to an array of floating-point numbers, which represents the features of the data point. The LS property value is stored in the type variable.

The converted row array is added to the X array, which holds the feature vectors, and the type value is added to the Y array, which holds the corresponding types.

An instance of the KNN classifier is created using the ml-knn library. The X and Y arrays along with the options { k: 1 } (which specifies the number of nearest neighbors to consider) are passed to the constructor.

The knn.predict(input) method is called, where input is the input data point for which we want to predict the type. The predicted type is stored in the type variable.

The predicted type is returned as the output of the getType function.

In summary, this code reads a CSV file, converts it into a JSON object, trains a k-nearest neighbors classifier using the data, and then uses the classifier to predict the type of a given input.
## Flowchart: 
START
      |
     V
[Import Modules]
      |
     V
[Define csvJSON Function]
      |
     V
[Define getType Function]
      |
     V
[Read CSV File]
      |
     V
[Convert CSV to JSON]
      |
     V
[Create Set for Types]
      |
     V
[Iterate Over JSON Data]
      |
     V
[Add Types to Set]
      |
     V
[Convert Types Set to Array]
      |
     V
[Iterate Over JSON Data (Again)]
      |
     V
[Convert Row Values to Array]
      |
     V
[Store Type and Features]
      |
     V
[Train KNN Classifier]
      |
     V
[Predict Type]
      |
     V
[Return Type]
      |
END
# Installation :
## Requirements :
To run this code on a system, you would need the following requirements:

Node.js: Ensure that you have Node.js installed on your system. You can download and install Node.js from the official Node.js website (https://nodejs.org). Choose the appropriate version for your operating system.

Package Dependencies: The code relies on external packages, so you need to install them. Open a terminal or command prompt, navigate to the directory where the code is located, and run the following command to install the required packages:
```
 npm install ml-knn
```
CSV Dataset: The code expects a CSV dataset file named dataset.csv to be present in the specified path (__dirname + "/../TRAVIS/dataset.csv"). Make sure you have the dataset file available at the correct location or modify the csvFilePath variable in the code to match the correct path of your dataset file.
## Installation :
To install and run a project from GitHub, you can follow these general steps:

Clone the Repository: Start by cloning the GitHub repository to your local machine. Open a terminal or command prompt, navigate to the directory where you want to clone the project, and run the following command:

```
git clone <https://github.com/raghavbohra28/TRAIVIS_PROJECT_LSRS>
```
Install Dependencies: Navigate into the project directory that was created after cloning the repository. Typically, it will be the same name as the repository. Once inside the project directory, run the following command to install the required dependencies:
```
npm install
```
This command will read the package.json file in the project and install all the necessary dependencies specified in it.

Configure the Project: If the project requires any additional configuration, such as setting up environment variables or modifying certain files, follow the instructions provided in the project's documentation or README file.
## Running the project :
Once the dependencies are installed and the project is configured, you should be able to run it. Refer to the project's documentation or README file for instructions on how to run the project. Typically, you can run a Node.js project using the following command:
```
streamlit run frontEnd.py
```
By following these steps, you should be able to install and run the project from GitHub on your local machine. 
