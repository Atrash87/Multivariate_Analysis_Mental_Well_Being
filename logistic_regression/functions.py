import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats

def prepare_data(df):
    # Example: convert categorical variables
    categorical_vars = ['gender', 'Education', 'chronic_disease', 'smoking', 
                        'drinking_alcohol', 'income_group_label', 
                        'BMI_category_label', 'activity_level', 'chronic_pain']
    for var in categorical_vars:
        if var in df.columns:
            df[var] = df[var].astype('category')
    return df

def run_main_logistic(df):
    formula = '''
    depression_binary ~ 
    C(activity_level, Treatment(reference="low activity")) + 
    C(income_group_label, Treatment(reference="Very Low")) + 
    C(BMI_category_label, Treatment(reference="Normal")) + 
    C(chronic_disease) + 
    C(smoking) + 
    C(drinking_alcohol) + 
    C(gender) + 
    age
    '''
    model = smf.logit(formula, data=df).fit()
    return model

def run_stratified_by_gender(df):
    males = smf.logit('''
    depression_binary ~ 
    C(activity_level, Treatment(reference="low activity")) + 
    C(income_group_label, Treatment(reference="Very Low")) + 
    C(BMI_category_label, Treatment(reference="Normal")) + 
    C(chronic_disease) + 
    C(smoking) + 
    C(drinking_alcohol) + 
    age
    ''', data=df[df['gender'] == 'male']).fit()

    females = smf.logit('''
    depression_binary ~ 
    C(activity_level, Treatment(reference="low activity")) + 
    C(income_group_label, Treatment(reference="Very Low")) + 
    C(BMI_category_label, Treatment(reference="Normal")) + 
    C(chronic_disease) + 
    C(smoking) + 
    C(drinking_alcohol) + 
    age
    ''', data=df[df['gender'] == 'female']).fit()

    return males, females

def run_interaction_analysis(df):
    formula = '''
    depression_binary ~ 
    C(activity_level, Treatment(reference="low activity")) * C(gender) + 
    C(income_group_label, Treatment(reference="Very Low")) + 
    C(BMI_category_label, Treatment(reference="Normal")) + 
    C(chronic_disease) + 
    C(smoking) + 
    C(drinking_alcohol) + 
    age
    '''
    model = smf.logit(formula, data=df).fit()
    return model

def extract_results(model):
    params = model.params
    conf_int = model.conf_int()
    conf_int.columns = ['2.5%', '97.5%']

    results = {}
    for var in params.index:
        if var != 'Intercept':
            results[var] = {
                'OR': np.exp(params[var]),
                'CI_lower': np.exp(conf_int.loc[var, '2.5%']),
                'CI_upper': np.exp(conf_int.loc[var, '97.5%']),
                'p_value': model.pvalues[var]
            }
    return results

def depression_group_stats(df):
    depressed = df[df['depression_binary'] == 1]['weekly_total_MET']
    non_depressed = df[df['depression_binary'] == 0]['weekly_total_MET']

    u_stat, p_value = stats.mannwhitneyu(depressed, non_depressed)
    return {
        "Depressed_median": np.median(depressed),
        "Non_depressed_median": np.median(non_depressed),
        "p_value": p_value
    }
