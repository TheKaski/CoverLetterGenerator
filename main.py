# This is a one file python script for using a coverLetterTemplate.txt file provided with this repo to easily generate personalized Cover Letter
# Please read the README.md for instructions how to use this

# Function for printing the first welcome prompt
def headerPrompt():
    print("This is a simple Python program for generating your cover letters \n")

# Function for returning the variables asked from the user
def inputVariables():
    variableNames = ["Employer name", "Position Title", "Company Name"]
    variables = {name: None for name in variableNames}

    for variableName in variableNames:
        variables[variableName] = input(f"Please define your variable for {variableName}: ")

    return variables

#Function for reading the template file and returning it
def readTemplateFile(fileName):
    # Read the cover letter template from the file
    try:
        with open(fileName, 'r') as file:
            template = file.read()
        return template
    except:
        print(f"There was an error reading the file  {fileName}")
# Fill the template with the stored input variables:
def fillTheTemplate(template, storedInput):
    return template.format(EmployerName=storedInput['Employer name'], PositionTitle=storedInput['Position Title'], CompanyName=storedInput['Company Name'])

#Function for outputting the results:
def output(result):
    print("Please copy the result below: \n")
    print(result)

def main():
    headerPrompt()
    storedInput = inputVariables()
    template = readTemplateFile('coverletterTemplate.txt')
    coverLetter = fillTheTemplate(template, storedInput)
    output(coverLetter)

if __name__ == "__main__":
    main()