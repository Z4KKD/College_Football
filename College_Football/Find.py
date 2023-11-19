import pandas as pd

# Assuming your CSV data is in a file named 'college_football.csv'
csv_file = 'college_football.csv'

# Load the CSV data
df = pd.read_csv(csv_file)

# Filter data for Week 1
week_1_data = df[df['Week'] == 1]

# Calculate a performance metric based on the difference between home and away postgame Elo ratings
week_1_data['Performance Difference'] = week_1_data['Home Postgame Elo'] - week_1_data['Away Postgame Elo']

# Find the team with the maximum performance difference
best_team = week_1_data.loc[week_1_data['Performance Difference'].idxmax()]

# Display information about the best team for Week 1
print("Best Team for Week 1:")
print(f"Home Team: {best_team['Home Team']}")
print(f"Away Team: {best_team['Away Team']}")
print(f"Performance Difference: {best_team['Performance Difference']}")
print(f"Excitement Index: {best_team['Excitement Index']}")
print(f"Notes: {best_team['Notes']}")