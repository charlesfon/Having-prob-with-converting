# Convert all object-type columns to integers
for col in d1.select_dtypes(include='object').columns:
    d1[col] = pd.to_numeric(d1[col], errors='coerce')  # Clean strings
    d1[col] = d1[col].fillna(0).astype(int)            # Convert to int

# Verify
print(d1.dtypes)