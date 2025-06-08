
# preprocess.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("dataset.csv")

# Drop ID or text-based non-informative columns (you can adjust this)
drop_cols = ['StudentAbsenceDays', 'PlaceofBirth', 'SectionID', 'GradeID']
df.drop(columns=drop_cols, inplace=True, errors='ignore')

# Label encode all categorical columns
le = LabelEncoder()
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = le.fit_transform(df[col])

# Map target: L → 1 (Dropout), M/H → 0 (Not Dropout)
df['Class'] = df['Class'].apply(lambda x: 1 if x == 0 else 0)

# Final check
print("Transformed dataset:\n", df.head())

# Save preprocessed dataset
df.to_csv("cleaned_dataset.csv", index=False)
