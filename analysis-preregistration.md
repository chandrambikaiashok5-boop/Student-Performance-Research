# Analysis Preregistration 
## Research question

Is there a statistically significant relationship between the number of hours students study per day and their final academic scores?

## Hypotheses

There is no statistically significant relationship between students' daily study hours and their final academic scores.

Alternative Hypothesis (H1)

There is a statistically significant positive relationship between students' daily study hours and their final academic scores.

## Population, sample, and exclusions

Target population:

Students represented in the selected student performance dataset.

Sample:

All eligible student records available in the selected dataset will be included in the analysis.

Inclusion criteria:

- Students must have valid study hours data.
- Students must have valid final academic scores.
- Each record must represent a valid student observation.

Exclusion criteria:

- Records with missing study hours will be excluded.
- Records with missing final academic scores will be excluded.
- Duplicate records will be identified and handled before analysis.
- Invalid values will be checked and excluded where appropriate.

Observation window:

The observation period will be based on the academic period represented in the selected dataset.

## Variables and measures

Outcome variable:

Final academic score obtained by each student.

Predictor variable:

Number of hours spent studying per day.

Control variables:

Age and gender, if available in the dataset.

Measurement:

Study hours will be measured in hours per day.
Academic performance will be measured using final scores.

Data type:

Study hours: Numerical variable.
Final academic score: Numerical variable.
Age: Numerical variable, if available.
Gender: Categorical variable, if available.


## Transformations

Data cleaning:

- Check the dataset for missing values.
- Identify and handle duplicate records.
- Check for invalid values in study hours and final academic scores.

Missing values:

Records with missing values in the main variables will be excluded from the primary analysis.

Outliers:

Potential outliers will be identified and examined. They will not be removed automatically.

Data format:

Study hours and final academic scores will be kept in numerical format.

Scaling:

No scaling or normalisation will be applied for the primary analysis.
## Analysis plan


Descriptive statistics:

Mean, median, standard deviation, minimum, and maximum will be calculated for study hours and final academic scores.

Data visualization:

A scatter plot will be created to visualize the relationship between study hours and academic performance.

Correlation analysis:

Pearson correlation will be used to measure the strength and direction of the linear relationship between study hours and final academic scores.

Spearman correlation will be used as a sensitivity analysis if the data do not meet the assumptions for Pearson correlation.

Regression analysis:

Simple linear regression will be performed to estimate the relationship between daily study hours and final academic scores.

Statistical significance:

The significance level (alpha) will be set at 0.05.

Effect size:

The Pearson correlation coefficient (r) and regression R-squared value will be reported.

Reporting:

The analysis will report correlation coefficients, regression coefficients, p-values, and 95% confidence intervals.

Robustness checks:

- Check for missing values.
- Examine potential outliers.
- Compare Pearson and Spearman correlation results.
- Check regression assumptions.
- Record any limitations affecting the results.

Interpretation:

Results will describe associations and will not be interpreted as proof of causation.
## Deviations

No deviations from the preregistered analysis plan have been made at the time of registration.

Any future deviations will be recorded here with the date, reason, and description of the change.
