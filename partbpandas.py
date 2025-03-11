import pandas as pd
import numpy as np

# Load dataset
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)

# 1. Filter 'Manufacturer', 'Model', and 'Type' for every 20th row starting from row 0
filtered_df = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print("Filtered Rows:\n", filtered_df)

# 2. Replace missing values in Min.Price and Max.Price with their respective mean
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)
print("\nMissing values replaced in Min.Price and Max.Price columns.")

# 3. Get rows of a dataframe with row sum > 100
df_random = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_with_sum_gt_100 = df_random[df_random.sum(axis=1) > 100]
print("\nRows with sum > 100:\n", rows_with_sum_gt_100)