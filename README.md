# Employee Attrition Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether an employee is likely to **leave the company** or **stay** using Machine Learning.

The project follows a complete end-to-end Machine Learning workflow, including:

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Building
- Hyperparameter Tuning
- Model Evaluation
- Model Deployment using Streamlit

---

## 🎯 Problem Statement

Employee attrition is one of the major challenges faced by organizations.

The objective of this project is to build a Machine Learning model that predicts whether an employee is likely to leave the company so that organizations can take preventive actions to improve employee retention.

---

## 📂 Dataset

**IBM HR Employee Attrition Dataset**

**Target Variable**

- Attrition
  - Yes → Employee will Leave
  - No → Employee will Stay

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit

---

## 🔍 Data Preprocessing

The following preprocessing techniques were applied:

- Handling Missing Values using **SimpleImputer**
- One-Hot Encoding for categorical features
- Pipeline implementation
- ColumnTransformer implementation
- Train-Test Split

The preprocessing pipeline is automatically applied during prediction.

---

## 🤖 Machine Learning Models Used

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- XGBoost Classifier

---

## ⚙️ Hyperparameter Tuning

Hyperparameter tuning was performed using:

- GridSearchCV
- RandomizedSearchCV

5-Fold Cross Validation was used for model selection.

---

## 📈 Model Evaluation

Evaluation Metrics Used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## 🏆 Final Model

**Support Vector Machine (SVM)**

### Why SVM?

Among all the trained models, SVM achieved the best overall performance after hyperparameter tuning.

The model was selected based on:

- Highest Test Accuracy
- Better Precision
- Better Recall
- Better F1 Score

---

## 🚀 Streamlit Application

A Streamlit web application was developed for real-time prediction.

### Features

- User-friendly Interface
- Takes Employee Details as Input
- Predicts whether the Employee will Leave or Stay
- Uses the trained Joblib model for prediction

---

## 📁 Project Structure

```text
Employee-Attrition-Prediction/
│
├── app.py
├── Employee_Attrition.ipynb
├── Employee_Attrition_model.joblib
├── requirements.txt
├── README.md
├── dataset.csv
└── images/
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone <repository-link>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

---

## 📊 Future Improvements

- Handle class imbalance using techniques such as SMOTE.
- Improve Recall for the minority class.
- Deploy the application online using Streamlit Community Cloud.

---

## 📚 What I Learned

Through this project, I learned:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Scikit-Learn Pipelines
- ColumnTransformer
- Hyperparameter Tuning
- Model Evaluation
- Joblib Model Saving & Loading
- Streamlit Deployment
- End-to-End Machine Learning Workflow

---

## ⚠️ Limitations

The dataset is imbalanced, containing significantly more employees who stayed than employees who left.

Although techniques such as `class_weight='balanced'` were used, the model still performs better on the majority class than the minority class.

---

## ⭐ Conclusion

This project demonstrates a complete end-to-end Machine Learning pipeline, starting from data preprocessing to deployment using Streamlit.

It showcases practical implementation of Scikit-Learn Pipelines, Hyperparameter Tuning, Model Evaluation, Joblib, and Streamlit in a real-world HR Analytics problem.
