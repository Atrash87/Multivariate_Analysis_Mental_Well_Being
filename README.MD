# Physical Activity and Depression Risk Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-orange)
![StatsModels](https://img.shields.io/badge/StatsModels-0.13%2B-green)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A comprehensive statistical analysis examining the protective effects of physical activity against depression using logistic regression and data visualization.

## 📊 Overview

This project investigates the relationship between physical activity levels and depression risk in a Chinese population sample. Using multiple logistic regression, we quantify how different intensity levels of physical activity are associated with reduced depression risk while controlling for key covariates including chronic disease status, age, BMI categories, and demographic factors.

## 🎯 Key Findings

### Protective Effects:
- **High Physical Activity**: 52% lower depression risk (OR = 0.48, p < 0.001)
- **Moderate Physical Activity**: 38% lower risk (OR = 0.62, p < 0.001) 
- **Older Age**: 3% lower risk per year (OR = 0.97, p < 0.001)

### Risk Factors:
- **Chronic Disease**: 2.37× higher risk (OR = 2.37, p < 0.001)
- **Underweight BMI**: 42% higher risk vs normal weight (OR = 1.42, p = 0.029)

## 📁 Data Availability

The dataset used in this analysis is publicly available on FigShare:

[![DOI](https://figshare.com/articles/dataset/Data_Sheet_1_The_relationship_between_physical_activity_and_depression_among_community-dwelling_adults_in_Wuhan_China_ZIP/22689049?file=40280554)]

### Original Study Background
This research addresses the limited evidence on physical activity and depression risk in Chinese populations. The original study employed stratified random sampling to recruit participants from five urban districts in Wuhan, China.

**Study Design**: Cross-sectional study  
**Participants**: 5,583 permanent residents aged ≥18 years  
**Measures**: 
- Physical Activity: International Physical Activity Questionnaire Short Form (IPAQ-SF)
- Depression: 9-item Patient Health Questionnaire (PHQ-9)
- Covariates: Demographics, BMI, chronic disease status, lifestyle factors

## 📁 Project Structure
