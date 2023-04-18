# **API BDD Python Test Automation Framework**

[![LinkedIn](https://img.shields.io/badge/@LinkedIn-SpurQLabs-orange.svg)](https://www.linkedin.com/company/spurqlabs/mycompany/)

[![Blog](https://img.shields.io/badge/@Blog-SpurQLabs_Blogs-blue.svg)](https://spurqlabs.com/blogs/)

## **Description**

This repository contains a Python Behave API framework for automated testing of APIs using the Behave library. The framework is designed to provide a structured and organized approach to API testing, making it easy to write, execute, and manage API tests with Behave.

### **Create BDD Framework**

- [Learn how to create a BDD API Test Automation Framework using Python's Behave Library](https://spurqlabs.com/python-behave-api-testing-bdd-framework/)

## **Features**

- Utilizes Playwright and Playwright Test libraries for interacting with APIs.
- Supports running tests in headless mode for faster execution.
- Generates screenshots for failed test steps for better error analysis.
- Supports configuration through environment variables for easy customization.
- Includes built-in reporting using Cucumber for easy test result visualization
- Provides a set of utility functions and configurations for common test scenarios

## **Table of Contents**
- [Pre-Requitesites](#Pre-Requitesites)
- [Technology](#Technology_used_in_Framework)
- [Installation](#Installation)
- [Execution](#Execution)
- [Report-Generation](#Report_Generation )
- [Framework Structure](#Fmework_Structure)
- [Reports](#Generated_Reports)

## Pre-Requisite
### *Required tools for the project*

- Python
- allure-behave: 2.10.0
- allure-python-commons: 2.10.0
- behave: 1.2.6
- requests: 2.28.2


## Technology_used_in_Framework
#### AUTOMATION:
- `Python`
- `requests`
- `Behave`

#### REPORTING TOOL :
- `allure-behave- ^2.10.0`
- `allure-python-commons - ^2.10.0`
#### FRAMEWORK DESIGN PATTERN :
- `Behavior Driven Development (BDD)`
#### OS for Execution on Local:
- `Windows`
#### OS for Execution on CI/CD:
- `Windows`

**Note:** 
##### Please make sure you have all technologies in your local machine installed or configured.

## Installation
### To Clone this repository to a local directory
Commands to clone and run the test cases<br />
- #### git clone: 
`https://github.com/spurqlabs/PythonBehaveApiFramework.git`

This command clone this repository to your local VS code.
- #### Install the dependencies mentioned in prerequisite
    
    Run the following command and it will install all the packages listed in requirement.txt file
      
        pip install -r requirement.txt

## Execution

#### To run all the feature file
        behave Features -f allure_behave.formatter:AllureFormatter -o Report_Json

#### To run single feature file
        behave Features/API.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

## Report_Generation 

#### To generate HTML report from JSON report
        allure generate Report_Json -o Report_Html --clean

## Github_Workflow_File 
This repository contains a CI/CD pipeline for automated testing of Python APIs using Behave and generating Allure reports. The pipeline is configured to run on every push to the "main" branch, and it performs the following steps:

#### *Set up Python:*
Sets up the Python environment using the actions/setup-python action, specifying the Python version to use as 3.8.9.

#### *Install Dependencies:* 
Upgrades pip and installs the dependencies listed in the requirement.txt file using the pip command.

#### *Install Allure:* 
Installs the Allure Command Line tool globally using the npm install command, which allows generating HTML reports for test results.

#### *Run Tests:* 
Executes the API tests using the Behave library with the allure_behave formatter, which generates JSON reports in the Report_Json directory.

#### *Generate HTML Report:* 
Generates HTML reports from the JSON reports using the Allure Command Line tool, which are stored in the Report_Html directory.

#### *Upload Artifact:* 
Uploads the HTML reports as an artifact using the actions/upload-artifact action, making it accessible for further analysis.

### **Usage**
#### To use the CI/CD workflow in your own project, follow these steps:

- Create a .github/workflows directory in the root of the GitHub repository, if it doesn't already exist.

- Copy the contents of the api.yml file from this repository into a new file with the same name (api.yml) in the .github/workflows directory of the repository.

- Commit and push the changes to the repository.

- The CI/CD workflow will now be automatically triggered to run on every push or pull request to the master branch of the repository.

## Framework_Structure

![image](https://user-images.githubusercontent.com/110516709/232682880-c712d514-88ae-4ed8-9b95-52b8f13452bd.png)

### *Features*

- The feature file contains the test scenarios described in Gherkin Language. 
- The Scenarios are described in steps format using the keywords like Give, when, And, Then.
- The feature is easy to understand and can be written in the English language so that a non-technical person can understand the flow of the test scenario. In this framework we will be automating the four basic API request methods i.e. POST, PUT, GET and DELETE. 

### *Steps*

- The step file is used to map the steps described in the feature file.
- The fiel contains the multiple step files for each feature file and has the respective steps included
- Python’s behave library is very accurate to map the steps with the steps described in the feature file.

### *Resources*

- The resources has config.json file which contains the key and value pairs of the most frequently used data in the framework. For example api url.

### *Utility*

- The utility file contains the API methods and the endpoints to perform the specific action like, POST, PUT, GET, or DELETE.
- The request body i.e. payload and the response body will be captured using the methods present in the utility file. 

## Generated_Reports

### Report1:

![image](https://user-images.githubusercontent.com/110516709/232682745-c846b850-e487-4bea-a237-cb72ea2a3460.png)

### Report2: 

![image](https://user-images.githubusercontent.com/110516709/232682807-f74b261c-88e4-40d3-bf9e-5bc4787759bf.png)
