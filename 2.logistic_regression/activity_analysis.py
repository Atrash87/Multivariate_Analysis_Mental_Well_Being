# activity_analysis.py
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats

def run_activity_analysis(df):
    """
    Perform logistic regression analysis on depression outcome by activity level.
    Includes overall, gender-stratified, interaction analysis and descriptive stats.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing the following columns:
        - 'depression_binary', 'activity_level', 'sex', 'age',
          'income_group_label', 'BMI_category_label', 'chronic_disease',
          'smoking', 'drinking_alcohol', 'weekly_total_MET', 'MET5_group'
          
    Returns:
    None
    """
    # Make a copy
    df_analysis = df.copy()
    
    # Convert categorical variables
    df_analysis['sex'] = df_analysis['sex'].astype('category')  # 0=female, 1=male
    df_analysis['MET5_group'] = df_analysis['MET5_group'].astype('category')
    df_analysis['activity_level'] = df_analysis['activity_level'].astype('category')
    
    # Set reference categories
    df_analysis['activity_level'] = df_analysis['activity_level'].cat.reorder_categories(
        ['low activity', 'moderate activity', 'high activity'])
    df_analysis['sex'] = df_analysis['sex'].cat.rename_categories({0: 'female', 1: 'male'})
    
    # 1. Overall analysis
    print("=== OVERALL ANALYSIS ===")
    model_overall = smf.logit(
        'depression_binary ~ C(activity_level, Treatment(reference="low activity")) + age + C(sex) + '
        'C(income_group_label) + C(BMI_category_label) + C(chronic_disease) + C(smoking) + C(drinking_alcohol)', 
        data=df_analysis
    ).fit()
    print(model_overall.summary())
    
    # Extract ORs and confidence intervals for activity levels
    overall_params = model_overall.params
    overall_conf_int = model_overall.conf_int()
    overall_conf_int.columns = ['2.5%', '97.5%']
    activity_vars = [var for var in overall_params.index if 'activity_level' in var]
    
    print("\nOdds Ratios for Overall Analysis:")
    for var in activity_vars:
        or_value = np.exp(overall_params[var])
        ci_lower = np.exp(overall_conf_int.loc[var, '2.5%'])
        ci_upper = np.exp(overall_conf_int.loc[var, '97.5%'])
        print(f"{var}: OR = {or_value:.3f} (95% CI: {ci_lower:.3f}-{ci_upper:.3f})")
    
    # 2. Gender-stratified analysis
    print("\n" + "="*50)
    print("=== GENDER-STRATIFIED ANALYSIS ===")
    
    for gender in ['male', 'female']:
        print(f"\n--- {gender.upper()} ---")
        df_gender = df_analysis[df_analysis['sex'] == gender]
        model_gender = smf.logit(
            'depression_binary ~ C(activity_level, Treatment(reference="low activity")) + age + '
            'C(income_group_label) + C(BMI_category_label) + C(chronic_disease) + C(smoking) + C(drinking_alcohol)',
            data=df_gender
        ).fit()
        print(model_gender.summary())
        
        gender_params = model_gender.params
        gender_conf_int = model_gender.conf_int()
        gender_conf_int.columns = ['2.5%', '97.5%']
        
        print(f"\nOdds Ratios for {gender.capitalize()}:")
        for var in activity_vars:
            or_value = np.exp(gender_params[var])
            ci_lower = np.exp(gender_conf_int.loc[var, '2.5%'])
            ci_upper = np.exp(gender_conf_int.loc[var, '97.5%'])
            print(f"{var}: OR = {or_value:.3f} (95% CI: {ci_lower:.3f}-{ci_upper:.3f})")
    
    # 3. Interaction analysis
    print("\n" + "="*50)
    print("=== INTERACTION ANALYSIS ===")
    model_interaction = smf.logit(
        'depression_binary ~ C(activity_level, Treatment(reference="low activity")) * C(sex) + age + '
        'C(income_group_label) + C(BMI_category_label) + C(chronic_disease) + C(smoking) + C(drinking_alcohol)',
        data=df_analysis
    ).fit()
    print(model_interaction.summary())
    
    interaction_terms = [var for var in model_interaction.params.index if ':' in var or 'T.' in var]
    print(f"\nInteraction terms: {interaction_terms}")
    
    for term in interaction_terms:
        print(f"P-value for {term}: {model_interaction.pvalues[term]:.4f}")
    
    # 4. Descriptive stats for MET-min/week
    print("\n" + "="*50)
    print("=== DESCRIPTIVE STATISTICS (MET-min/week) ===")
    
    depressed_met = df_analysis[df_analysis['depression_binary'] == 1]['weekly_total_MET']
    non_depressed_met = df_analysis[df_analysis['depression_binary'] == 0]['weekly_total_MET']
    
    print(f"Depressed group: Median = {np.median(depressed_met):.0f}, "
          f"IQR = {np.percentile(depressed_met, 25):.0f}-{np.percentile(depressed_met, 75):.0f}")
    print(f"Non-depressed group: Median = {np.median(non_depressed_met):.0f}, "
          f"IQR = {np.percentile(non_depressed_met, 25):.0f}-{np.percentile(non_depressed_met, 75):.0f}")
    
    u_stat, p_value = stats.mannwhitneyu(depressed_met, non_depressed_met)
    print(f"Mann-Whitney U test p-value: {p_value:.4f}")
