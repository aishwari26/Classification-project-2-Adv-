Employee Attrition Prediction using Machine Learning
📌 Project Overview

This project predicts whether an employee is likely to leave the company (Attrition = Yes) or stay (Attrition = No) using Machine Learning.

The complete project includes:

Data preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Machine Learning model comparison
Hyperparameter tuning
Model evaluation
Model deployment using Streamlit
🎯 Problem Statement

Employee attrition is a major challenge for organizations. Predicting employees who are likely to leave helps companies take proactive measures to improve employee retention.

📊 Dataset

IBM HR Employee Attrition Dataset

Target Variable:

Attrition
Yes → Employee will leave
No → Employee will stay
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
XGBoost
Joblib
Streamlit
🔍 Data Preprocessing
Missing value handling using SimpleImputer
One-Hot Encoding for categorical features
Pipeline and ColumnTransformer implementation
Train-Test Split
Feature preprocessing integrated into the pipeline
🤖 Models Implemented
Logistic Regression
Decision Tree Classifier
Random Forest Classifier
Support Vector Machine (SVM)
XGBoost Classifier
⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed using:

GridSearchCV
RandomizedSearchCV

Cross-validation (5-Fold) was used for model selection.

📈 Model Evaluation

Evaluation Metrics:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Classification Report
Final Model

Support Vector Machine (SVM)

Reasons:

Highest overall test accuracy among the models.
Better Precision, Recall and F1-score for the minority class compared to other models evaluated.
Selected after hyperparameter tuning.
🚀 Streamlit Application

The trained model was deployed using Streamlit.

Features:

User-friendly interface
Accepts employee information
Predicts whether the employee is likely to leave or stay
Uses the saved Joblib model
📁 Project Structure
Employee-Attrition-Prediction/
│
├── app.py
├── Employee_Attrition_model.joblib
├── Employee_Attrition.ipynb
├── requirements.txt
├── README.md
├── dataset.csv (or dataset link)
└── images/
▶️ How to Run

Clone the repository

git clone <repository_link>

Install dependencies

pip install -r requirements.txt

Run Streamlit

streamlit run app.py
📌 Future Improvements
Improve recall for the minority class using advanced imbalance handling techniques such as SMOTE.
Experiment with ensemble learning methods.
Deploy the application on Streamlit Community Cloud.
📚 Learning Outcomes

Through this project, I learned:

End-to-end Machine Learning workflow
Data preprocessing using Pipelines
Feature Engineering
Hyperparameter tuning
Model comparison and evaluation
Saving and loading models using Joblib
Building and deploying ML applications using Streamlit
⭐ Final Note

This project demonstrates a complete end-to-end Machine Learning pipeline—from data preprocessing and model building to deployment—using industry-standard tools such as Scikit-Learn Pipelines, Joblib, and Streamlit.
