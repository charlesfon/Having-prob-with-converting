# Convert column to numeric, forcing invalid strings to NaN
d1['counter_code'] = pd.to_numeric(d1['counter_code'], errors='coerce')

# Fill NaN values with a default (e.g., 0) and convert to integer
d1['counter_code'] = d1['counter_code'].fillna(0).astype(int)

# Verify
print(d1['counter_code'].dtypes)          # Check dtype: should be int64
print(d1['counter_code'].unique())        # Check unique integer values