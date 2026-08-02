import streamlit as st
import joblib
import pandas as pd

model=joblib.load("Employee_Attrition_model.joblib")
st.title("Employee Attrition Prediction System")

age=st.number_input("Age",min_value=18,max_value=60,value=30)
daily_rate = st.number_input("Daily Rate", min_value=102, max_value=1499, value=800)
gender=st.selectbox("Gender",["Male","Female"])
distance_from_home=st.number_input("Distance From Home",min_value=1,max_value=29,value=5)
education = st.number_input("Education", min_value=1, max_value=5, value=3)

employee_number = st.number_input("Employee Number", min_value=1, max_value=2068, value=100)

environment_satisfaction = st.number_input("Environment Satisfaction", min_value=1, max_value=4, value=3)

hourly_rate = st.number_input("Hourly Rate", min_value=30, max_value=100, value=65)

job_involvement = st.number_input("Job Involvement", min_value=1, max_value=4, value=3)

job_level = st.number_input("Job Level", min_value=1, max_value=5, value=2)

job_satisfaction = st.number_input("Job Satisfaction", min_value=1, max_value=4, value=3)

monthly_income = st.number_input("Monthly Income", min_value=1009, max_value=19999, value=5000)

monthly_rate = st.number_input("Monthly Rate", min_value=2094, max_value=26999, value=12000)

num_companies_worked = st.number_input("Number of Companies Worked", min_value=0, max_value=9, value=2)

percent_salary_hike = st.number_input("Percent Salary Hike", min_value=11, max_value=25, value=15)

performance_rating = st.number_input("Performance Rating", min_value=3, max_value=4, value=3)

relationship_satisfaction = st.number_input("Relationship Satisfaction", min_value=1, max_value=4, value=3)

stock_option_level = st.number_input("Stock Option Level", min_value=0, max_value=3, value=1)

total_working_years = st.number_input("Total Working Years", min_value=0, max_value=40, value=10)

training_times_last_year = st.number_input("Training Times Last Year", min_value=0, max_value=6, value=3)

work_life_balance = st.number_input("Work Life Balance", min_value=1, max_value=4, value=3)

years_at_company = st.number_input("Years At Company", min_value=0, max_value=40, value=5)

years_in_current_role = st.number_input("Years In Current Role", min_value=0, max_value=18, value=3)

years_since_last_promotion = st.number_input("Years Since Last Promotion", min_value=0, max_value=15, value=1)

years_with_curr_manager = st.number_input("Years With Current Manager", min_value=0, max_value=17, value=3)


# =========================
# Categorical Inputs
# =========================

business_travel = st.selectbox(
    "Business Travel",
    ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
)

department = st.selectbox(
    "Department",
    ["Sales", "Research & Development", "Human Resources"]
)

education_field = st.selectbox(
    "Education Field",
    [
        "Life Sciences",
        "Medical",
        "Marketing",
        "Technical Degree",
        "Human Resources",
        "Other"
    ]
)



job_role = st.selectbox(
    "Job Role",
    [
        "Sales Executive",
        "Research Scientist",
        "Laboratory Technician",
        "Manufacturing Director",
        "Healthcare Representative",
        "Manager",
        "Sales Representative",
        "Research Director",
        "Human Resources"
    ]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

over_time = st.selectbox(
    "OverTime",
    ["Yes", "No"]
)

over18="Y"

#Creates a button named "Predict Attrition".
#The code below it runs only when the user clicks the button.
if st.button("Predict Attrition"):
#This dictionary represents one employee.
    input_data = {
        "Age": age,
        "BusinessTravel": business_travel,
        "DailyRate": daily_rate,
        "Department": department,
        "DistanceFromHome": distance_from_home,
        "Education": education,
        "EducationField": education_field,
        "EmployeeNumber": employee_number,
        "EnvironmentSatisfaction": environment_satisfaction,
        "Gender": gender,
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobRole": job_role,
        "JobSatisfaction": job_satisfaction,
        "MaritalStatus": marital_status,
        "MonthlyIncome": monthly_income,
        "MonthlyRate": monthly_rate,
        "NumCompaniesWorked": num_companies_worked,
        "Over18": "Y",
        "OverTime": over_time,
        "PercentSalaryHike": percent_salary_hike,
        "PerformanceRating": performance_rating,
        "RelationshipSatisfaction": relationship_satisfaction,
        "StockOptionLevel": stock_option_level,
        "TotalWorkingYears": total_working_years,
        "TrainingTimesLastYear": training_times_last_year,
        "WorkLifeBalance": work_life_balance,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": years_in_current_role,
        "YearsSinceLastPromotion": years_since_last_promotion,
        "YearsWithCurrManager": years_with_curr_manager
    }




#Converts the input_data dictionary into a one-row DataFrame.
#Exactly like one row of your X_train.
    input_df = pd.DataFrame([input_data])

#Sends that one employee's data to your trained SVM model.
#The model predicts:
#0 → Employee will stay
#1 → Employee will leave
    prediction = model.predict(input_df)  #prediction[0] → model.predict() returns an array, even for one employee.

    if prediction[0] == 1:                                          #prediction = [1]
        st.error("Employee Will Leave")                              #prediction[0]   # gives 1
                                                               
    else:
        st.success("Employee Will Stay")