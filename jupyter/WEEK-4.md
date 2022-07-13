# DATA PREPROCESSING

[medium reference](https://towardsdatascience.com/data-preprocessing-e2b0bed4c7fb)
- Porcess of transforming the raw data into understandable format(for computer also). The quality of the data should be checked before applying the data for machine learning model
- The preprocessing is doing to check the quality of the data. The quality of a data can be checked by following
1. Accuracy 
2. completeness
3. Consistancy
4. Timeliness
5. Believability
6. Interpretability

<img src = 'https://media.geeksforgeeks.org/wp-content/uploads/20190312184006/Data-Preprocessing.png' />

# Major Tasks in data preprocessing
1. Data cleaning
2. Data integration
3. Data reduction 
4. Data transformation

## 1. Data cleaning

-  ### (a) Missing values handling: isna(), fillna(), notana() dropna()
   -  We can drop the record, or fill the np.nan with mean(normal dist), median(non normal or mode. 
   1. Ignore the tuple
   2. Fill
  
- ### (b)Noisy
   1. Binnig: Partition by frequency,  smoothing by bin mean, smoothing by bin median or smoothing by bin boundaries
   [binnig geeksforgeeks](https://www.geeksforgeeks.org/python-binning-method-for-data-smoothing/)
   
   2. Regression - smoothe the data by fitting it into a regression
   3. clustering
   
## 3. Data Integration

Data from different sources should be integrated to one data set. sources could be no sql, or sql. 
The column name of data set could be different. we need to integrate this into same


## 3. Data transformation(transform the data in appropriate forms)
1. Normalization: scale the data values in a specified range (-1.0 to 1.0 or 0 to 1)
2. Attribute selection
3. Discretization
   -  Replace the raw values of numeric data by interval level
4. Concept heirarchy generation
   - Attributes are converted from lower level to a higher level in herirarchy. for ex. city -> country
   
## 4. Data reduction : Reduct the amount of data

1. Aggregation(data cube aggregation)

2. Attribute subset selection - according the p-values. eg. color of house in not needed in house predicion
3. Numerosity reduction - store the model instead of whole data. eg.regression model
4. Dimensionality reduction - Combining and merging the attributes of the data without losing its original characteristics.or lossy with eg. PCA


# Preprocessing steps in machine learning

[analticsvida\ya](https://www.analyticsvidhya.com/blog/2021/08/data-preprocessing-in-data-mining-a-hands-on-guide/)

1. Import libraries and data set

2. Extracting independent variable

3. Extract dependent variable

4. Filling the dataset wiht mean, median or mode. 

5. Encoding of categorical data column

6. Splitting the data into training and test 

7. Feature scaling: StandardScalar


# EXPLORATORY DATA ANALYSIS (EDA)

Exploratory data analysis (EDA) is used by data scientists to analyze and investigate data sets and summarize their main characteristics, often employing data visualization methods

[ibm.com](https://www.ibm.com/in-en/cloud/learn/exploratory-data-analysis)

# Git and git basics
-  Amigose code, gitconnected.com from medium

- Git reset, revert, rebase [geekflare](https://geekflare.com/git-reset-vs-revert-vs-rebase/)

# ML Basics

## ML workflow

[towards ds. best tutorial](https://towardsdatascience.com/workflow-of-a-machine-learning-project-ec1dba419b94)

 1. Gathering information
 2. Data preprocessing
 3. Building data set and research the best model to fit
   - Training set
   - Validation set
   - Test set
 4. Training and refinement
 5. Machine learning evaluation
 
 
 ## Classification and regression concepts
 
 ## Vectorization cocepts
 
 Making the data set into vector format to perfom the vector and matrix operations using numpy instead of using normal addition and for loop execution 
 
 [mlcompass](https://machinelearningcompass.com/machine_learning_math/vectorization/)
 
 ## Performance concepts
 
 For classification
 - Confusion matrix
 - Accuracy
 - Logarihmic loss
 - Area under curve
 - F1 score(recall and preciion)
 
 
 For regression
 
 - Mean absolute error
 - Mean squared error
 - R squared score
 - Adjusted R squared
 
 ## Linear regression
 - Gradient descent
 - Normal equation
 
 ## Case study
 
 



