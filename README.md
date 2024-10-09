# Spam Detection Using SVM

Summary of Best Classifiers by Scenario:
|Scenario |	Best Classifiers |
|Binary Classification|	Logistic Regression, SVM, Random Forest|
|Multiclass Classification|	Random Forest, SVM, Neural Networks|
|Imbalanced Datasets|	Random Forest, XGBoost, SVM with class weights|
|High-Dimensional Data|	SVM, Logistic Regression with L1, Naive Bayes|
|Small Dataset, Low Complexity|	k-NN, Decision Trees, Naive Bayes|
|Large Dataset, High Complexity|	XGBoost, Neural Networks, Random Forest|
|Time-Series Data|	LSTM, TCN, ARIMA|
|Text Classification|	Naive Bayes, SVM, Transformers|


#Before Pre-processing Dataset

As necessary as cleaning and preprocessing operations are in preparing data for machine learning models, they must be performed carefully in relation to spam detection. Cleaning can sometimes go to the extent of removing such factors that are helpful in distinguishing samples for classification. Thus, it is advised to follow a balanced strategy where all such features are kept as potential features, but noise is excluded. Methods like feature extraction and the selection of preprocessing methods based on the nature of the dataset can greatly improve spam filter efficiency.

This means that the choice of whether to eliminate or include certain preprocessing steps in spam detection specifically is entirely dependent on the situation and the nature of the given data set. Excessive cleaning of the words may result in discarding some information which can be useful in the proper categorization of the data. It is advisable to maintain potentially useful features while removing noise in a system to have good performance in spam detection.
 
