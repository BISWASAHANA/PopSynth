import numpy as np
import pandas as pd

# Define population characteristics from Table 2
population_characteristics = {
    'Sex': {'Male': 25324, 'Female': 24676},
    'Age_group': {'Below 22 years': 17955, '22-60 years': 29642, 'Above 60 years': 2403},
    'Highest_education_level': {'No_formal_education': 7490, 'Primary_education': 5655,
                                 'Secondary_education': 24400, 'Graduation_and_above': 12455}
}

# Load the provided sample dataset
sample_data = pd.read_csv('Data.csv')
