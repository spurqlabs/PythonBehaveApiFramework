# PythonAPIFramework

In this API BDD Testing Framework created alsong with python and behave to automate web test cases and api testing. I have also added the allure reports to display the full and detailed presentation of the test result. 

## Installation: 
  
  Run the following command and it will install all the packages listed in requirement.txt file
      
        pip install -r requirement.txt


## Execution:

  ## 1)To run all the feature file
        behave Features -f allure_behave.formatter:AllureFormatter -o Report_Json

  ## 2)To run single feature file
        behave Features/BMI_alculator.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

  ## 3)To run test cases using Tag name from single feature file                                    
        behave Features/BMI_alculator.feature --tags=mobile  -f allure_behave.formatter:AllureFormatter -o Report_Json

  ## 4)To run test cases using Tag name from all feature files
        behave Features --tags=mobile  -f allure_behave.formatter:AllureFormatter -o Report_Json

## Report Generation: 

  ## 5)To generate HTML report from JSON report
        allure generate Report_Json -o Report_Html --clean

## CI/CD Workflow:

In this is a Continuous Integration/Continuous Deployment (CI/CD) workflow for a Python API. It triggers a build whenever there is a push to the "main" branch. The workflow installs dependencies, runs tests using the Behave framework, generates test reports using the Allure formatter, and uploads the generated HTML reports as an artifact. It uses the Windows-latest operating system and Python version 3.8.9.
