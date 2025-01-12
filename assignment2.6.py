import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('SpeedData.txt', delim_whitespace=True)

def compare_migration_speeds(row):
    return "Yes" if row['Spring'] > row['Autumn'] else "No"

df['Faster_in_Spring'] = df.apply(compare_migration_speeds, axis=1)

print(df)

df.to_csv('migration_comparison.txt', sep=' ', index=False)

plt.figure(figsize=(10, 6))
species = df['Species']
spring_speeds = df['Spring']
autumn_speeds = df['Autumn']

plt.bar(species, spring_speeds, width=0.4, label='Spring', align='center')
plt.bar(species, autumn_speeds, width=0.4, label='Autumn', align='edge')
plt.xlabel('Species')
plt.ylabel('Migration Speed')
plt.title('Bird Migration Speeds in Spring and Autumn')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('migration_speeds.png')
plt.show()


comparison_results = []
yes_data = []

def compare_migration_speeds(row):
    if row['Spring'] > row['Autumn']:
        yes_data.append(row)
        return "Yes"
    else:
        return "No"


df['Faster_in_Spring'] = df.apply(compare_migration_speeds, axis=1)
comparison_results = df['Faster_in_Spring'].tolist()

print(df)

print("Comparison Results Array:", comparison_results)

yes_df = pd.DataFrame(yes_data)

print("Yes Data DataFrame:")
print(yes_df)

df.to_csv('migration_comparison.csv', index=False)

yes_df.to_csv('yes_migration_data.csv', index=False)