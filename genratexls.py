import pandas as pd
from itertools import product

# Define all possible parameter values
parameters = {
    'site address': ['US pre 2411', 'Non US pre 2411', 'US 2411',
                     'Non US 2411', 'US 2502', 'Non US 2502'],
    'Core service deployment': ['N/A (before 2025)', 'Edge (2025)', 'Edgeless (2025)'],
    'edge cluster': ['SAS', 'NON SAS'],
    'Spectrum band': ['48', '77', '78', '79'],
    'Band tier': ['GAA', 'PAL', 'GAA+PAL', 'N/A'],
    'radio technology': ['4g', '5g', '4g+5g'],
    'Channel Width': ['4g', '5g', '4g+5g'],
    'Frequency Configuration': ['auto', 'manual']
}

# Generate all possible combinations
all_combinations = list(product(*parameters.values()))

# Create DataFrame
df = pd.DataFrame(all_combinations, columns = parameters.keys())

# Apply conditional logic to filter invalid combinations
valid_df = df[
    # Before 2025 can only have Core=None
    (~df['Core service deployment'].str.contains('2025')) |
    (df['Core service deployment'].str.contains('2025'))

    # Add all other conditional rules here...
    # Example: SAS can only have band 48
    & ((df['edge cluster'] != 'SAS') | (df['Spectrum band'] == '48'))

    # Add remaining conditions...
    ]

# Add Test Case ID
valid_df.insert(0, 'Test Case ID', range(1, len(valid_df) + 1))

# Save to Excel
valid_df.to_excel("siteArchit_testcases.xlsx", index = False)

print(f"Successfully generated {len(valid_df)} test cases in siteArchit_testcases.xlsx")