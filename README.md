# 🎬 Netflix Data Cleaning Project
##  Objective
This project focuses on cleaning and preprocessing a raw Netflix dataset by handling missing values, duplicates, and inconsistent formats.

## Tools Used
- Python
- Pandas
-
## Dataset
The dataset contains information about Netflix movies and TV shows such as:
- Title
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
##  Data Cleaning Steps
1. Loaded dataset using pandas
2. Checked missing values using isnull()
3. Handled missing values using fillna()
4. Removed duplicate records using drop_duplicates()
5. Cleaned column names (lowercase, removed spaces)
6. Converted date format using to_datetime()
7. Standardized text values (lowercase, removed spaces)

## Files in this Repository
- netflix_data.csv → Raw dataset  
- clean_data_netflix.csv → Cleaned dataset  
- cleaning.py → Python script  
## Output
A clean and structured dataset ready for data analysis and visualization.
##  Learning Outcome
- Learned data cleaning techniques
- Gained hands-on experience with Pandas
- Improved problem-solving skills
