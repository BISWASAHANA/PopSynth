import numpy as np
import pandas as pd

# Define population characteristics from Table 2
population_characteristics = {
    'Sex': {'Male': 25324, 'Female': 24676},
    'Age_category': {'Below 22 years': 17955, '22-60 years': 29642, 'Above 60 years': 2403},
    'Highest_education_level': {'No_formal_education': 7490, 'Primary_education': 5655,
                                 'Secondary_education': 24400, 'Graduation_and_above': 12455}
}

# Load the provided sample dataset
sample_data = pd.read_csv('Data.csv')

# Function to generate synthetic population
def generate_population(sample_data, population_characteristics, total_agents):
    # Initialize an empty DataFrame to store synthesized population
    population_df = pd.DataFrame(columns=population_characteristics.keys())

    # Generate agents for each attribute based on population characteristics
    for attribute, categories in population_characteristics.items():
        # Count the occurrences of each category in the sample data
        if attribute == 'Age_category':
            attribute_counts = sample_data['Age_category'].value_counts().to_dict()
        else:
            attribute_counts = sample_data[attribute].value_counts().to_dict()

        # Update population characteristics to include missing categories
        for category in attribute_counts.keys():
            if category not in categories:
                categories[category] = 0

        # Generate random counts for each category
        counts = np.random.multinomial(total_agents, [value / sum(categories.values()) for value in categories.values()])
        
        # Adjust counts based on the sample data distribution
        for category, count in attribute_counts.items():
            index = list(categories.keys()).index(category)
            counts[index] += count
        
        # Create DataFrame for the attribute
        attribute_df = pd.DataFrame({attribute: list(categories.keys()), 'Frequency': counts})
        
        # Append to the population DataFrame
        population_df = pd.merge(population_df, attribute_df, how='outer', on=attribute)

    return population_df

# Generate synthetic population with 50,000 agents
synthetic_population = generate_population(sample_data, population_characteristics, 50000)

# Save synthetic population to CSV
synthetic_population.to_csv('synthetic_population.csv', index=False)

# Compute frequencies for specified variables
def compute_frequencies(synthetic_population, variable):
    frequencies = synthetic_population[variable].value_counts().reset_index()
    frequencies.columns = [variable, 'Frequency']
    return frequencies

# Compute frequencies for specified variables
frequencies_text = ""
for variable in population_characteristics.keys():
    frequencies = compute_frequencies(synthetic_population, variable)
    frequencies_text += f"Frequencies for {variable}:\n{frequencies.to_string(index=False)}\n\n"

# Save frequencies to .txt file
with open('frequencies_output.txt', 'w') as file:
    file.write(frequencies_text)

print("Output frequencies saved in 'frequencies_output.txt'")