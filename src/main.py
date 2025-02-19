import pandas as pd

# Load dataset (Replace 'example.csv' with your actual file)
df = pd.read_csv('example.csv')

# Display first few rows
print("Original Data:")
print(df.head())

################## Handle Missing Values ##################

# Fill missing numeric values with the mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill missing categorical values with the mode
df.fillna(df.mode().iloc[0], inplace=True)

################## Remove Duplicates ######################

df.drop_duplicates(inplace=True)

############# Convert Data Types if Necessary #############

# Example: Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

################## Basic Data Analysis #####################

print("\nData Summary:")
print(df.describe())  # Statistical summary of numerical columns

print("\nMissing Values Count:")
print(df.isnull().sum())  # Check for any remaining missing values

print("\nUnique Values per Column:")
print(df.nunique())

# Save cleaned dataset
df.to_csv('cleaned_data.csv', index=False)

print("\nData cleaning complete. Cleaned file saved as 'cleaned_data.csv'")
