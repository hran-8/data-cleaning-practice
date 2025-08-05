# Practice Run 1: Cleaning and Analyzing Multi-Family Permit Data (1980-2022) 

Dataset: Residential Construction Permits by County 
Data found through data.gov: https://catalog.data.gov/dataset/residential-construction-permits-by-county
Download for Dataset: https://hudgis-hud.opendata.arcgis.com/datasets/da836467b4904711b14d74acbc4568be_24/about 

### Documentation 
I ensured that the dataset included multi-family, 5+ unit permits.
The dataset was in csv format, and some data points were imputed, making it easy to use pandas methods to filter and organize relevant data. For now, I filtered just 1980-2022 data (most recent from this dataset) and looked for multi-family 5+ unit permits.
Headers were cut and lowercased for easy use and organization, then the filtered data was organized by number of permits for 5+ units

### Notes 
- Data was in csv format
- Missing values were imputed for some data points 
- Because data was very easy to work with, I just needed to filter relevant data and sort it. I want to webscrape and analyze data that may not be so cleanly formatted for further practice. 

