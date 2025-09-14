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

- Gender-stratified analysis:

   - Men: OR = 0.46 (p = 0.016, moderate); OR = 0.35 (p = 0.002, high).

   - Women: Protective trend but not significant (OR = 0.77, p = 0.35, moderate; OR = 0.63, p = 0.089, high).

**Other significant factors:**

- Chronic disease increased odds ~3.7× (OR = 3.72, p < 0.001).

- Underweight BMI increased odds ~2.1× (OR = 2.06, p = 0.014).

- Very low income increased odds ~1.95× (OR = 1.95, p = 0.040).

- Age had a protective effect: each additional year reduced odds by ~3% (OR = 0.97 per year, p < 0.001).

- Overall trend: Higher physical activity and older age were protective; chronic disease, underweight, and very low income were key risk factors.

## Reference Categories Used in the Model

- **Activity level**: Low activity (baseline for comparison with moderate and high)

- **Sex**: Female (baseline for comparison with male)

- **Income group**: High income (baseline for comparison with very low, low, middle, very high)

- **BMI category**: Normal weight (baseline for comparison with underweight, overweight, obese)

- **Chronic disease**: No chronic disease (baseline for comparison with presence of chronic disease)

- **Smoking**: Non-smoker (baseline for comparison with smoker)

- **Drinking alcohol**: Non-drinker (baseline for comparison with drinker)


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
