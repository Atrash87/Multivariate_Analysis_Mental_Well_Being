# Depression and Physical Activity Analysis

This project analyzes the relationship between **physical activity levels** and **depression** using **multivariate logistic regression models**.

## What the Code Does
- **Preprocessing**: Cleans the dataset, converts categorical variables, and sets reference groups.  
- **Overall multivariate Logistic Regression**: Models depression status as a function of activity level, age, sex, income group, BMI category, chronic disease, smoking, and alcohol consumption.  
- **Gender-Stratified Analysis**: Runs separate multivariable models for males and females.  
- **Interaction Analysis**: Tests whether the association between activity level and depression differs by gender.  
- **Descriptive Statistics**: Compares weekly MET-minutes between depressed and non-depressed groups using medians, IQRs, and a Mann-Whitney U test.  

## How to Run
1. Clone this repository.  
2. Install requirements:
   ```bash
   pip install -r requirements.txt
3. Place your dataset (e.g., your_data.csv) in the project folder.

4. Run the script:
   ```bash
   python analysis_functions.py
## Requirements

- **pandas

- **numpy

- **statsmodels

- **scipy
