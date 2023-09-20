# AWS Lambda Python Request Module Fix 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

This AWS Lambda function solves the problem of using the `request` module, which was deprecated after Python 3.7. It makes HTTP requests using the modern `urllib3` library.

## 📋 Table of Contents
- [Problem](#problem)
- [Solution](#solution)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

Tired of the deprecated `request` module in Python 3.7+? This AWS Lambda Python code shows you how to make HTTP requests using `urllib3` in a serverless environment.

## 📜 Problem
```
[ERROR] Runtime.ImportModuleError: Unable to import module 'lambda_function': No module named 'requests'
Traceback (most recent call last):
```
Python 3.7+ no longer supports the `request` module, and you need to make HTTP requests in your AWS Lambda function.

## 🛠️ Solution

This Lambda function uses `urllib3` to send a GET request to [Google](https://www.google.com) and prints the response content and status code.

## 🚀 Deployment Steps

Follow these steps to deploy and test the Lambda function:

1. **Create an AWS Lambda Function:**

   - Sign in to your AWS Management Console.
   - Navigate to AWS Lambda and create a new Lambda function.
   - Choose the Python 3.8 runtime or later.
   - Configure the necessary permissions and roles.

2. **Upload the Code:**

   - In the Lambda function configuration, upload the provided Python code.

3. **Test the Function:**

   - Create a new test event or use a sample event to trigger the Lambda function.
   - Run the test and verify that it makes a successful HTTP request to Google.

## 🛠️ Usage

You can modify and extend this Lambda function to make HTTP requests to other endpoints, perform more complex data processing, or integrate it into your AWS ecosystem. The provided code is a starting point for modernizing your Python 3.7 Lambda functions that rely on HTTP requests.

## 💡 Note

- Ensure that your Lambda function has the necessary IAM permissions to make outbound network requests.
- Keep in mind that the `urllib3` library is just one option for making HTTP requests in Python. Depending on your use case, you might consider other libraries like `requests`.

## 👤 Author

- [Abaid Gulshan](https://github.com/abaidgulshan)

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).
