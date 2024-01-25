# CoverLetterGenerator
This is a simple project for generating personalized Cover letters with Python. 
The purpose is to use Python to generate and multiply personalized cover letters when applying for multiple companies. The program allows you to write your cover letter text in a templatefile and replace company name, position title and employer name with a simple prompt. You can then easily copy the results and use them as you wish. 

# How to use
1. Write your cover letter text into the coverLetterTemplate.txt file using the variables defined below
2. Wrap your preffered variables with { variable_name }
3. Run the program with `python main.py` and use the results as you wish

## Example template provided:
Fill this template with your cover letter text
You can use the variables
EmployerName:{EmployerName} 
CompanyName:{CompanyName}
PositionTitle:{PositionTitle}
And they will be replaced with your given inputs.
More information in README.md

# Suported Variables:
- EmployerName
- PositionTitle
- CompanyName
- (add tyour own in code)
