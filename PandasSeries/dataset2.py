# Import pandas
import pandas as pd

# Custom index and a name
marks = [67, 57, 89, 100]
subjects = ['maths', 'english', 'science', 'hindi']

marks = pd.Series(marks, index=subjects, name='Ramya ke marks')

# Display series
print(marks)

# Access a specific value
print(marks['english'])

# Create Series from dictionary
marks_dict = {
    'maths': 67,
    'english': 57,
    'science': 89,
    'hindi': 100
}

marks_series = pd.Series(marks_dict, name='nitish ke marks')

print(marks_series)

# Series attributes

# Index
print(marks_series.index)

# Values
print(marks_series.values)

# Name
print(marks_series.name)

# Check uniqueness
print(marks_series.is_unique)

# Example with duplicate values
print(pd.Series([1, 1, 2, 3, 4, 5]).is_unique)
