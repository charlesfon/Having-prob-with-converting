# Find columns with the string 'train_Client_0'
problem_columns = []
for col in d1.columns:
    if d1[col].astype(str).str.contains('train_Client_0').any():
        problem_columns.append(col)
print("Problem columns:", problem_columns)

# Clean all problematic columns
for col in problem_columns:
    d1[col] = pd.to_numeric(d1[col], errors='coerce')
    d1[col] = d1[col].fillna(0).astype(int)

# Verify
print(d1.dtypes)