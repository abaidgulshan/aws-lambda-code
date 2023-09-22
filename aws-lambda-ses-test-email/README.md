# AWS Lambda Function: Sending Email using Amazon SES 🚀

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

This AWS Lambda function sends an email using Amazon Simple Email Service (SES) with SMTP credentials. It's a basic example to demonstrate sending an email through AWS SES using Python.

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Configuration](#configuration)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

## 🛠️ Prerequisites

Before deploying this Lambda function, you need to set up the following:

1. **Amazon SES SMTP Credentials**: Obtain your SES SMTP credentials from the AWS Console.

2. **Verified Email Addresses**: Ensure that the "From" address (SENDER) is verified in your SES console.

## 🚀 Configuration

Edit the Lambda function code to configure the following:

- `SENDER`: Your verified "From" address.
- `SENDERNAME`: Your sender name.
- `RECIPIENT`: The recipient's email address.
- `USERNAME_SMTP`: Your SES SMTP username.
- `PASSWORD_SMTP`: Your SES SMTP password.
- `HOST`: The SES SMTP host (e.g., `email-smtp.us-east-1.amazonaws.com`).
- `PORT`: The SES SMTP port (587 by default).
- `SUBJECT`: The subject line of the email.
- `BODY_HTML`: The HTML content of the email.

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


## 👤 Author

- [Abaid Gulshan](https://github.com/abaidgulshan)

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).
