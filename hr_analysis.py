
import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print(df.head())
print(df.shape)
print(df.info())

print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Employee Attrition Analysis

total_employees = len(df)

attrition_count = (df["Attrition"] == "Yes").sum()

attrition_rate = (attrition_count / total_employees) * 100

print("Total Employees:", total_employees)
print("Employees Who Left:", attrition_count)
print("Attrition Rate:", round(attrition_rate, 2), "%")


# Attrition by Department

department_attrition = df[df["Attrition"] == "Yes"]["Department"].value_counts()

print("\nEmployees Who Left by Department:")
print(department_attrition)


# Attrition by Overtime

overtime_attrition = df[df["Attrition"] == "Yes"]["OverTime"].value_counts()

print("\nEmployees Who Left by Overtime:")
print(overtime_attrition)


# Compare Attrition Rates by Overtime

overtime_rates = df.groupby("OverTime")["Attrition"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nAttrition Rate by Overtime:")
print(overtime_rates.round(2))

import matplotlib.pyplot as plt

overtime_rates.plot(kind="bar")

plt.title("Employee Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()


plt.savefig("attrition_by_overtime.png")
plt.show()

# Attrition by Job Role

job_role_attrition = df[df["Attrition"] == "Yes"]["JobRole"].value_counts()

print("\nEmployees Who Left by Job Role:")
print(job_role_attrition)

# Attrition by Job Satisfaction

satisfaction_attrition = df.groupby("JobSatisfaction")["Attrition"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nAttrition Rate by Job Satisfaction:")
print(satisfaction_attrition.round(2))

# Chart: Attrition Rate by Job Satisfaction

import matplotlib.pyplot as plt

satisfaction_attrition = df.groupby("JobSatisfaction")["Attrition"].apply(
    lambda x: (x == "Yes").mean() * 100
)

plt.figure(figsize=(8, 5))
satisfaction_attrition.plot(kind="bar")

plt.title("Attrition Rate by Job Satisfaction")
plt.xlabel("Job Satisfaction Score")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("attrition_by_job_satisfaction.png")
plt.show()


# Attrition by Age Group

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"]
)

age_attrition = df.groupby("AgeGroup", observed=False)["Attrition"].apply(
    lambda x: (x == "Yes").mean() * 100
)

print("\nAttrition Rate by Age Group:")
print(age_attrition.round(2))


# Chart: Attrition Rate by Age Group

plt.figure(figsize=(8, 5))
age_attrition.plot(kind="bar")

plt.title("Attrition Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("attrition_by_age_group.png")
plt.show()