## Automating the creation of AMIs , create new version of Launch Template and the update of an Auto Scaling group 

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


## License

This library is licensed under the MIT-0 License. See the LICENSE file.

