###CREATING AND LOADING DATASET###

# Import pandas
import pandas as pd

# Create a list of countries (string values)
country = ['India', 'Pakistan', 'USA', 'Nepal', 'Srilanka']

# Convert list into Pandas Series
country_ser = pd.Series(country)

# Print country series
print(country_ser)

# Create a list of runs (integer values)
runs = [13, 24, 56, 78, 100]

# Convert list into Pandas Series
runs_ser = pd.Series(runs)

# Print runs series
print(runs_ser)
