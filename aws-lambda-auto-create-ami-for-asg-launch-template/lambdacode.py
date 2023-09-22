import os
import boto3
import json
import datetime

start_date = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
autoScalingGroupName = os.environ['Auto_Scaling_Group_Name']
launchTemplateName = os.environ['Launch_Template_Name']
ec2RoleARN = os.environ['EC2_Role_ARN']
keyName = os.environ['Private_Key_Name']
ec2SecurityGroupID = os.environ['EC2_Security_Group_ID']
instancetype = os.environ['InstanceType']

def lambda_handler(event, context):
    

        client = boto3.client('autoscaling')
        autoscaling = client.describe_auto_scaling_groups(
            AutoScalingGroupNames=[
            autoScalingGroupName
            ]
        )

        instanceID = autoscaling['AutoScalingGroups'][0]['Instances'][0]['InstanceId']
        client = boto3.client('ec2')
        name= "Lambda for " + autoScalingGroupName + " from "+ start_date
        description= "AMI for " + autoScalingGroupName + " created by lambda"

        image = client.create_image(
            Description=description,
            DryRun=False, 
            NoReboot=True,
            InstanceId=instanceID, 
            Name=name)

        launch_template= client.create_launch_template_version(
            DryRun=False,
            LaunchTemplateName = launchTemplateName,
            SourceVersion="$Latest",
            VersionDescription = name,
            LaunchTemplateData={
                'IamInstanceProfile': {
                    'Arn': ec2RoleARN
                },
                'ImageId': image['ImageId'],
                'InstanceType': instancetype,
                'KeyName': keyName,
                'SecurityGroupIds': [
                    ec2SecurityGroupID,
                ]
            }
        )
        
        response = client.modify_launch_template(
            LaunchTemplateName=launchTemplateName,
            DefaultVersion="$Latest"
        )
        print("Default launch template set to $Latest.")
        previous_version = str(
            int(response["LaunchTemplate"]["LatestVersionNumber"]) - 4)
        response = client.delete_launch_template_versions(
            LaunchTemplateName=launchTemplateName,
            Versions=[
                previous_version,
            ]
        )        
        launch_template_status = launch_template
        print(launch_template_status)
        
        return json.dumps(response)  