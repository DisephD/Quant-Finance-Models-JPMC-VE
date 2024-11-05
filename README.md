# Quantitative Research Virtual Experience

![image](/assets/Screenshot-4.png)

This repository contains four tasks completed as part of my Quantitative Research Virtual Internship with JP Morgan Chase. Each task demonstrates my ability to analyze financial data, build machine learning models, and apply statistical methods to solve real-world business problems.

## Table of Contents
1. Overview
2. Data
3. What I Learnt
4. Task Descriptions
- Task 1: Investigate and Analyze Price Data
- Task 2: Price a Commodity Storage Contract
- Task 3: Credit Risk Analysis
- Task 4: Bucket FICO Scores
5. Technologies Used
6. Images
7. Contact

## Overview
During the virtual experience, I was exposed to the quantitative aspects of financial services, particularly focusing on commodity pricing, credit risk analysis, and data modeling. I employed various tools and machine learning algorithms to deliver insights and build working prototypes. This repository documents the work done on four key tasks, each representing a different business problem tackled using Python and data analysis techniques.]

## Data Source
The datasets used for the tasks were provided during the program. You can find it in the [data](/data) folder.

## What I Learnt
From this experience, I gained hands-on skills in:
- Applying statistical formulas to solve business problems
- Breaking down large datasets using machine learning methods
- Selecting the most relevant independent variables for predicting target outcomes
- Leveraging data to predict customer trends and actions
- Writing functions to price commodity contracts based on specific inputs
- Extrapolating data to generate insights from external feeds

## Task Details

### Task 1: Investigate and Analyze Price Data
In this task, I was provided with natural gas storage contract data to forecast prices for one year, assisting a client interested in trading. I analyzed the data to estimate the purchase price of gas for any past date and projected the prices into the future.

### Task 2: Price a Commodity Storage Contract
This task involved building a prototype pricing model to generate automated quotes for clients. The script returns the contract price for the specified date based on these parameters/inputs:
- Injection dates
- Withdrawal dates
- Commodity prices (purchase/sale)
- Injection/withdrawal rates
- Maximum storage volume
- Storage costs

### Task 3: Credit Risk Analysis
In this task, I trained a machine learning model to estimate the probability of default based on customer characteristics. Five models were trained and all models surpassed 99% Accuaracy. The models used for this task are shown below:
| Model | Accuracy |
| ----- | -------- |
| Random Forest | 99.7% |
| Gradient Boosting | 99.65 |
| Logistic Regression | 99.5% |
| K-Nearest Neighbors | 99.3% |
| Support Vector Machine | 99.2% |

### Task 4: Bucket FICO Scores
A FICO score is a standardized credit score that reflects the creditworthiness of a borrower, ranging from 300 to 850. In this task, I used Python to strategically bucket customers by their FICO scores to determine the probability of default.
To achieve this, I applied quantization and dynamic programming techniques. I also calculated mean squared error (MSE) and root mean squared error (RMSE) to evaluate the accuracy of my model.

## Technologies Used
- Python: Core programming language used for all tasks
- Pandas: Data manipulation and analysis
- Matplotlib: Data visualization
- Scikit-learn: Machine learning and model evaluation
- Streamlit: Web app development
- ARIMA: Time series forecasting
- NumPy: Numerical operations
  
## Images
![image](/assets/Screenshot-1.png)
![image](/assets/Screenshot-5.png)
![image](/assets/Screenshot-3.png)
![image](/assets/Screenshot-2.png)

## Contact
If you have any questions or are interested in my work, feel free to send me an email or via LinkedIn.

