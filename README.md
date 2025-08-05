# Practice Run 1: Cleaning and Analyzing Multi-Family Permit Data (1980-2022) 

- Dataset: Residential Construction Permits by County 
- Data found through data.gov: https://catalog.data.gov/dataset/residential-construction-permits-by-county
- Download for Dataset: https://hudgis-hud.opendata.arcgis.com/datasets/da836467b4904711b14d74acbc4568be_24/about 

### Documentation 
I ensured that the dataset included multi-family, 5+ unit permits.
The dataset was in csv format, and some data points were imputed, making it easy to use pandas methods to filter and organize relevant data. For now, I filtered just 1980-2022 data (most recent from this dataset) and looked for multi-family 5+ unit permits.
Headers were cut and lowercased for easy use and organization, then the filtered data was organized by number of permits for 5+ residential units. 

### Notes 
- Data was in csv format
- Missing values were imputed for some data points 
- Because data was very easy to work with, I just needed to filter relevant data and sort it. I want to webscrape and analyze data that may not be so cleanly formatted for further practice. 

# Practice Run 2: Data Retrieval + Cleaning on Gwinnett County's Permits Issued Data 12/30/2024 - 1/3/2025

- Dataset: Permits Issued for Gwinnett County between 12/30/2024 - 1/3/2025
- Data Source: https://www.gwinnettcounty.com/static/departments/planning/pdf/2025_activity/gwinnett-county-building-permits-12302024-01032025.pdf 

### Documentation 
Parsing and cleaning data took the most effort for this practice run as data was from a pdf that is not in csv or table/row format.
pdfplumber (pdf equivalent of BS4) was used for converting pdf to raw text. I manually created headers for the data and spliced the relevant sections for each row entry. The list of each row is then converted to a pandas DataFrame and then filtering/organizing with pandas methods is possible.

### Notes
- Data was in pdf format
- Blanks in data not imputted or dropped
- Specifically if I were looking for permits for residential buildings with 5+ units, this was not the best data to use. There was a field for "NO. OF UNITS" in the data, but was blank for all cases. Instead, I had to find cases where the 'use' header was 'Townhouse'.
- Challenge for scraping dirty data and parsing with string splicing is that although I used pdfplumber for easy conversion, the resulting text was often broken for multilines and difficult to parse. E.g CASE NUMBER COMBLD2024-02469 was converted to CASE NUMBER COMBLD2024-....other data...02469 instead of CASE NUMBER COMBLD2024-02469 or CASE NUMBER COMBLD2024-\n02469
