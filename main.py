import pandas as pd 

# data from https://catalog.data.gov/dataset/residential-construction-permits-by-county
# Download source: https://hudgis-hud.opendata.arcgis.com/datasets/da836467b4904711b14d74acbc4568be_24/about 
df = pd.read_csv('residential_construction_permits_by_county.csv')

# print(df.shape)
# print(df.columns[:15])
# print(df.head())



# clean column names 
df.columns = df.columns.str.strip()
print(df.isna().sum().sum()) # Check if there are any missing values

# Show count of missing values per column
missing_per_column = df.isna().sum()
print(missing_per_column[missing_per_column > 0].sort_values(ascending=False))

# create a new list of just the 2022 column headers (all data from 1980-2022)
columns_2022 = []
for col in df.columns: 
    if "2022" in col: 
        columns_2022.append(col) 


# print(columns_2022)
# filter column headers to just data we're interested in 
cols_2022 = ['STATE_NAME', 'COUNTY', 'NAME', 'ALL_PERMITS_2022', 'SINGLE_FAMILY_PERMITS_2022', 'ALL_MULTIFAMILY_PERMITS_2022', 'MULTIFAMILY_PERMITS_2_UNITS_2022', 'MULTIFAMILY_PERMITS_3_4_UNIT_2022', 'MULTIFAMILY_PERMITS_5_OR_MORE_2022']

# create a new df from these new column headers and rename headers 
df_2022 = df[cols_2022].copy() 

new_cols = [] 
for col in df_2022.columns: 
    new_cols.append(col.replace("_2022", "").lower())
df_2022.columns = new_cols
# print(df_2022.head())


# filter out and create new df for just the permits that have 5+ units (not included if multifamily permits == 0)
df_multi5 = df_2022[df_2022['multifamily_permits_5_or_more'] > 0]
# sorted by 5+ units permits
top_multi = df_multi5.sort_values('multifamily_permits_5_or_more', ascending=False) 
# print(top_multi[['state_name', 'county', 'multifamily_permits_5_or_more']].head(10))

df_2022.to_csv("cleaned_permit_data_2022.csv", index=False)
top_multi.to_csv("top_multi5.csv", index=False)