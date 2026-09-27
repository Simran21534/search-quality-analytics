# Search Quality & User Behavior Analytics

## Project Overview

This project analyzes search interaction behavior to identify suspicious or potentially abusive interaction patterns using data analytics, statistical testing, machine learning, SQL, and Power BI.

The project uses a synthetic dataset of 50,000 search interactions to demonstrate an end-to-end analytics workflow.

## Objectives

- Analyze user search behavior and interaction patterns
- Identify behavioral signals associated with suspicious activity
- Perform statistical hypothesis testing
- Build a machine learning classifier for suspicious behavior
- Create automated ML-based risk alerts
- Develop an interactive Power BI dashboard

## Technology Stack

- Python
- Pandas
- NumPy
- SQL
- SQLite
- Jupyter Notebook
- Power BI
- Git/GitHub

## Project Pipeline

Raw Data
→ Data Cleaning
→ Behavioral Analysis
→ SQL Analysis
→ Feature Engineering
→ Statistical Testing
→ Machine Learning
→ Automated Monitoring
→ Power BI Dashboard

## Dataset

The project uses 50,000 synthetic search interaction records.

Important fields include:

- Event ID
- Query Text
- Dwell Time
- Number of Results Viewed
- Query Reformulation
- Session Duration
- Clicked
- Suspicious Label

## Data Cleaning

The raw dataset was cleaned and validated using Python and Pandas.

The processed dataset contains:

- 50,000 records
- 14 original analytical columns
- engineered behavioral features for further analysis

## Behavioral Analysis

Suspicious and normal interactions were compared using:

- Click rate
- Average dwell time
- Results viewed
- Query reformulation rate

Suspicious interactions showed substantially shorter average dwell time and higher query reformulation in the synthetic dataset.

## SQL Analysis

SQLite was used to perform analytical queries including:

- Event counts by behavior type
- Click rate
- Average dwell time
- Average results viewed
- Query reformulation rate

## Feature Engineering

Behavioral risk signals were created:

- Short Dwell Flag
- High Reformulation Flag
- Low Results Viewed Flag
- Rapid Interaction Flag
- Behavioral Risk Score

## Statistical Testing

Statistical analysis included:

- Mann–Whitney U test
- Chi-square test

The chi-square test examined the relationship between query reformulation and suspicious behavior.

For the synthetic dataset:

- Chi-square statistic: 4412.66
- p-value: < 0.001

This indicates a statistically significant association in the synthetic data.

## Machine Learning

A logistic regression classifier was implemented using NumPy.

The model was evaluated on a held-out test set containing 10,000 interactions.

### Model Results

- Accuracy: 99.21%
- Precision: 90.75%
- Recall: 99.87%
- F1 Score: 95.09%
- ROC-AUC: 0.999

## Automated Risk Monitoring

An automated ML risk threshold of 0.80 was used to generate alerts.

On the 10,000-interaction test set:

- Automated alerts: 534
- Alert rate: 5.34%

## Power BI Dashboard

The Power BI dashboard contains two pages.

### Page 1 — Search Quality Overview

Includes:

- Total interactions
- Suspicious cases
- Suspicious rate
- Average dwell time by actual label
- Actual vs Predicted Suspicious Behavior

### Page 2 — ML Risk & Automated Monitoring

Includes:

- Automated alert count
- Query reformulation analysis
- Actual vs predicted behavior
- Average ML risk probability
- ML risk probability distribution

## Key Insights

The analysis demonstrates how behavioral signals such as dwell time, query reformulation, results viewed, and session duration can be combined to identify suspicious interaction patterns.

The project also demonstrates an end-to-end workflow from raw data processing to statistical analysis, machine learning, automated monitoring, and business-facing visualization.

## Limitations

This project uses synthetic data created for portfolio and learning purposes.

The reported model metrics should not be interpreted as real-world or production performance. The synthetic target and engineered features are closely related, which can result in unusually strong model performance.

The project does not use Google's internal data, systems, or proprietary information.

## Future Improvements

- Test the pipeline on a real-world open dataset
- Add cross-validation
- Compare multiple classification models
- Add model calibration
- Add threshold tuning
- Add automated data-quality monitoring
- Deploy the pipeline using cloud services
- Add scheduled dashboard refresh