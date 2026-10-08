
# HR Analytics: Employee Attrition Analysis

## Project Overview

This project analyzes employee attrition using Python and the IBM HR Analytics Employee Attrition dataset. The goal is to identify patterns associated with employees leaving the organization through data cleaning, exploratory data analysis, and visualization.

## Tools and Technologies

* Python
* Pandas
* Matplotlib
* Seaborn
* VS Code

## Dataset

The dataset contains 1,470 employee records and 35 columns, including age, department, job role, job satisfaction, overtime, and attrition status.

## Analysis Performed

* Inspected dataset structure and data types
* Checked for missing values and duplicate rows
* Calculated the overall employee attrition rate
* Analyzed attrition by department and job role
* Compared attrition rates for employees working overtime
* Examined attrition by job satisfaction level
* Analyzed attrition across age groups
* Created charts to communicate key findings

## Key Findings

* The dataset contains 1,470 employees, of whom 237 left the organization.
* The overall attrition rate is approximately 16.12%.
* Employees working overtime had a higher attrition rate (30.53%) than those not working overtime (10.44%).
* The highest attrition rate by job satisfaction was among employees with a score of 1 (22.84%).
* Employees aged 18–25 had the highest attrition rate among the analyzed age groups (35.77%).
* Research & Development had the largest number of employee departures (133).

## Visualizations

The project generates these charts:

* `attrition_by_overtime.png`
* `attrition_by_job_satisfaction.png`
* `attrition_by_age_group.png`

## How to Run

1. Install Python.
2. Install the required libraries:
   `pip install pandas matplotlib seaborn`
3. Place the dataset CSV file in the project folder.
4. Run the analysis:
   `python hr_analysis.py`

## Conclusion

The analysis identifies differences in employee attrition across overtime status, job satisfaction, age groups, departments, and job roles. These findings can help guide further investigation into employee retention.

*Note: The findings describe patterns in this dataset and do not establish that any single factor causes employee attrition.*

# HR-Analytics-Python
Employee attrition analysis using Python, Pandas, and Matplotlib

