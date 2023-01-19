import boto3
quantity = int(input('Enter Number of ec2 Instances to Create: '))
ami = 'ami-0b5eea76982371e91'
keyname = 'demoKey'
def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId = ami,
        MinCount = quantity,
        MaxCount = quantity,
        InstanceType = 't2.micro',
        KeyName = keyname,)

create_instance() 