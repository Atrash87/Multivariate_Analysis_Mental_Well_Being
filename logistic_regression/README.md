# Depression and Physical Activity Analysis

This project analyzes the relationship between **physical activity levels** and **depression** using **multivariate logistic regression models**.

## What the Code Does
- **Preprocessing**: Cleans the dataset, converts categorical variables, and sets reference groups.  
- **Overall multivariate Logistic Regression**: Models depression status as a function of activity level, age, sex, income group, BMI category, chronic disease, smoking, and alcohol consumption.  
- **Gender-Stratified Analysis**: Runs separate multivariable models for males and females.  
- **Interaction Analysis**: Tests whether the association between activity level and depression differs by gender.  
- **Descriptive Statistics**: Compares weekly MET-minutes between depressed and non-depressed groups using medians, IQRs, and a Mann-Whitney U test.
## Key Findings:
- Moderate activity reduced depression odds by 38% (OR = 0.62, p = 0.023).

- High activity reduced depression odds by 50% (OR = 0.50, p = 0.001).

- For men: OR = 0.46 (p = 0.016, moderate); OR = 0.35 (p = 0.002, high).

- For women: Protective trend but not significant (OR = 0.77, p = 0.35; OR = 0.63, p = 0.089).

## Reference Categories Used in the Model

- Activity level: Low activity (baseline for comparison with moderate and high)

- Sex: Female (baseline for comparison with male)

- Income group: High income (baseline for comparison with very low, low, middle, very high)

- BMI category: Normal weight (baseline for comparison with underweight, overweight, obese)

- Chronic disease: No chronic disease (baseline for comparison with presence of chronic disease)

- Smoking: Non-smoker (baseline for comparison with smoker)

- Drinking alcohol: Non-drinker (baseline for comparison with drinker)


## How to Run
1. Clone this repository.  
2. Install requirements:
   ```bash
   pip install "requirements"
3. Place your dataset (e.g., your_data.csv) in the project folder.

4. Run the script:
   ```bash
   python analysis_functions.py
## Requirements

- pandas

- numpy

- statsmodels

- scipy
