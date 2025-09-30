import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats


def preprocess_data(df):
    """Preprocess dataframe: set categories and rename values."""
    df = df.copy()
    df['sex'] = df['sex'].astype('category').cat.rename_categories({0: 'female', 1: 'male'})
    df['MET5_group'] = df['MET5_group'].astype('category')
    df['activity_level'] = df['activity_level'].astype('category')
    df['activity_level'] = df['activity_level'].cat.reorder_categories(
        ['low activity', 'moderate activity', 'high activity']
    )
    return df


def run_logistic_regression(formula, df):
    """Fit logistic regression model and return fitted model."""
    model = smf.logit(formula, data=df).fit()
    return model


def print_odds_ratios(model, label=""):
    """Print odds ratios and confidence intervals for activity level."""
    params = model.params
    conf_int = model.conf_int()
    conf_int.columns = ['2.5%', '97.5%']

    activity_vars = [var for var in params.index if 'activity_level' in var]

    print(f"\nOdds Ratios {label}:")
    for var in activity_vars:
        or_value = np.exp(params[var])
        ci_lower = np.exp(conf_int.loc[var, '2.5%'])
        ci_upper = np.exp(conf_int.loc[var, '97.5%'])
        print(f"{var}: OR = {or_value:.3f} (95% CI: {ci_lower:.3f}-{ci_upper:.3f})")


def gender_stratified_analysis(df, formula):
    """Run separate logistic regressions for males and females."""
    for sex in ['male', 'female']:
        print(f"\n--- {sex.upper()} ---")
        df_sub = df[df['sex'] == sex]
        model = run_logistic_regression(formula, df_sub)
        print(model.summary())
        print_odds_ratios(model, label=f"for {sex}")


def interaction_analysis(df, formula):
    """Run logistic regression with interaction term."""
    print("\n=== INTERACTION ANALYSIS ===")
    model = run_logistic_regression(formula, df)
    print(model.summary())

    interaction_terms = [var for var in model.params.index if ':' in var]
    print(f"\nInteraction terms: {interaction_terms}")
    for term in interaction_terms:
        print(f"P-value for {term}: {model.pvalues[term]:.4f}")


def descriptive_stats(df):
    """Calculate and print descriptive statistics and Mann-Whitney U test."""
    print("\n=== DESCRIPTIVE STATISTICS (MET-min/week) ===")
    depressed = df[df['depression_binary'] == 1]['weekly_total_MET']
    non_depressed = df[df['depression_binary'] == 0]['weekly_total_MET']

    print(f"Depressed: Median = {np.median(depressed):.0f}, "
          f"IQR = {np.percentile(depressed, 25):.0f}-{np.percentile(depressed, 75):.0f}")
    print(f"Non-depressed: Median = {np.median(non_depressed):.0f}, "
          f"IQR = {np.percentile(non_depressed, 25):.0f}-{np.percentile(non_depressed, 75):.0f}")

    u_stat, p_value = stats.mannwhitneyu(depressed, non_depressed)
    print(f"Mann-Whitney U test p-value: {p_value:.4f}")
