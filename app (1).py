import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Load the trained model
with open("gradient_boost.pkl", "rb") as pickle_in:
    gradient_boost_model = pickle.load(pickle_in)

def predict_salary_category(features):
    """Function to predict the salary category using the Gradient Boosting model."""
    prediction = gradient_boost_model.predict([features])
    return prediction[0]

def main():
    # HTML for styling
    html_temp = """
    <div style="background-color:darkblue;padding:10px">
    <h2 style="color:white;text-align:center;">Data Scientist Salary Predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input fields for each feature
    work_year = st.number_input("Work Year", min_value=2024, step=1)
    job_category = st.selectbox("Job Category", options=["Data Engineering", "Data Science", "Machine Learning", "Data Architecture", "Management", "Other"])
    experience_level = st.selectbox("Experience Level", options=["Entry", "Mid-Level", "Senior", "Executive"])
    employment_type = st.selectbox("Employment Type", options=["Contract", "Freelance", "Full Time", "Part Time"])
    employee_residence = st.selectbox("Employee Residence", options=["North America", "Europe", "Asia", "Africa", "South America", "Australia & Oceania", "Middle East", "Other"])
    company_location = st.selectbox("Company Location", options=["North America", "Europe", "Asia", "Africa", "South America", "Australia & Oceania", "Middle East", "Other"])
    company_size = st.selectbox("Company Size", options=["Small", "Medium", "Large"])
    ratio_class = st.selectbox("Work Arrangement", options=["Remote", "In-Person", "Hybrid"])

    # Map the categorical variables to numerical values
    job_category_map = {
        "Data Engineering": 1, "Data Science": 2, "Machine Learning": 3,
        "Data Architecture": 4, "Management": 5, "Other": 6}
    experience_map = {"Entry": 1, "Mid-Level": 2, "Senior": 3, "Executive": 4}
    employment_map = {"Contract": 1, "Freelance": 2, "Full Time": 3, "Part Time": 4}
    residence_map = {"North America": 1, "Europe": 2, "Asia": 3, "Africa": 4, "South America": 5, "Australia & Oceania": 6, "Middle East": 7, "Other": 8}
    location_map = {"North America": 1, "Europe": 2, "Asia": 3, "Africa": 4, "South America": 5, "Australia & Oceania": 6, "Middle East": 7, "Other": 8}
    size_map = {"Small": 1, "Medium": 2, "Large": 3}
    ratio_map = {"Remote": 1, "In-Person": 2, "Hybrid": 3}

    # Salary category mapping
    salary_category_map = {
        1: "salary < 100,000 USD",
        2: "100,000 ≤ salary < 200,000 USD",
        3: "salary ≥ 200,000 USD"
    }

    # Apply the mappings
    features = [
        work_year,
        experience_map[experience_level],
        employment_map[employment_type],
        residence_map[employee_residence],
        location_map[company_location],
        size_map[company_size],
        ratio_map[ratio_class],
        job_category_map[job_category]
    ]
    
# When the 'Predict' button is clicked
    if st.button("Predict"):
        result = predict_salary_category(features)
        st.markdown(f"<p style='color:red;'>The predicted salary category is: {salary_category_map[result]}</p>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()
