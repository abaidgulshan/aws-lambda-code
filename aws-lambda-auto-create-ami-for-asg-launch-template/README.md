# 🚀 Automating the creation of AMIs , create new version of Launch Template and the update of an Auto Scaling group 🖼️

The code is used for a CI/CD pipeline which updates an auto scaling group of EC2 instances and creates an AMI of this instances. Than a new launch template version is created with this AMI.


The [lambdacode.py](/lambdacode.py) is the code used by the Lambda function to create a new AMI and update the launch configuration.
To use it on a Lambda function you will need to set the timeout to 5 seconds and input the enviroment variables:

|Name|Stands For|
|----|-----|
|Auto_Scaling_Group_Name|Name of the Auto Scaling group that is going to be updated|
|EC2_Role_ARN|Instance Profile ARN not IAM ROLE ARN for the EC2|
|EC2_Security_Group_ID|Security Group's ID for the EC2 instances|
|Launch_Template_Name|Name of the Launch Tamplate that is used by the Auto Scailing group|
|Private_Key_Name|Name of the Private Key used to acess your EC2 instances|
|InstanceType|Name of Instance type |


## Usage

1. **Configuration**: Ensure that you have configured the necessary environment variables in your Lambda function. These include:
   - `Auto_Scaling_Group_Name`: The name of the Auto Scaling Group.
   - `Launch_Template_Name`: The name of the Launch Template.
   - `EC2_Role_ARN`: The ARN of the IAM role for EC2 instances.
   - `Private_Key_Name`: The name of the private key for EC2 instances.
   - `EC2_Security_Group_ID`: The ID of the EC2 Security Group.
   - `InstanceType`: The EC2 instance type.

2. **Execution**: Trigger the Lambda function. It will create an AMI for the latest instance in the specified Auto Scaling Group.

3. **Clean-up**: The Lambda function will also manage Launch Templates to ensure efficient resource usage. Older versions are deleted to keep only the latest version.
## 👤 Author

- [Abaid Gulshan](https://github.com/abaidgulshan)

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).
