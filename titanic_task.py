import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titanic Data Analysis Script
# Author: [Your Name]
# Description: This script performs data cleaning, transformation, and visualization on Titanic dataset.

# ==========================
# Data Preparation
# ==========================
# Sample Titanic dataset
data = {
    'survived': [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    'pclass': [3, 1, 3, 1, 3, 3, 1, 2, 2, 3],
    'sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'male'],
    'age': [22.0, 38.0, 26.0, 35.0, 35.0, None, 54.0, 27.0, 14.0, None],
    'sibsp': [1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    'parch': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'fare': [7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51.8625, 13.0, 30.0708, 7.75],
    'embarked': ['S', 'C', 'S', 'S', 'S', 'Q', 'S', 'S', None, 'Q'],
    'class': ['Third', 'First', 'Third', 'First', 'Third', 'Third', 'First', 'Second', 'Second', 'Third'],
    'deck': [None, 'C', None, 'C', None, None, 'E', None, None, None],
    'embark_town': ['Southampton', 'Cherbourg', 'Southampton', 'Southampton', 'Southampton', 'Queenstown', 'Southampton', 'Southampton', 'Southampton', 'Queenstown'],
    'alive': ['no', 'yes', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'no']
}

# Create DataFrame
df = pd.DataFrame(data)

# ==========================
# Data Cleaning
# ==========================
# Handle missing values
df['age'] = df['age'].fillna(df['age'].median())  # Replace missing 'age' with median
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])  # Replace missing 'embarked' with mode
df = df.drop(columns=['deck'])  # Drop 'deck' column due to too many missing values

# Convert data types
df['sex'] = df['sex'].astype('category')
df['embarked'] = df['embarked'].astype('category')
df['class'] = df['class'].astype('category')
df['survived'] = df['survived'].astype(bool)  # Convert 'survived' to boolean

# Remove duplicates
df = df.drop_duplicates()

# Rename columns for consistency
df.columns = df.columns.str.lower().str.replace(' ', '_')

# ==========================
# Data Visualization
# ==========================
# Plot the count of survivors vs. non-survivors
sns.countplot(data=df, x='survived')
plt.title('Count of Survivors vs. Non-Survivors')
plt.xlabel('Survived (False = Non-Survivor, True = Survivor)')
plt.ylabel('Count')
plt.show()

# Create a barplot of average age by class
sns.barplot(data=df, x='class', y='age', ci=None)
plt.title('Average Age by Class')
plt.xlabel('Class')
plt.ylabel('Average Age')
plt.show()

# ==========================
# End of Script
# ==========================















































































