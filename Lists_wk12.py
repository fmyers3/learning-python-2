aws_services = ['EC2', 'Python', 'Lambda']

print(aws_services)

print (len(aws_services)) 

aws_services.append('s3')

aws_services.insert(0,'DynamoDB')

print(aws_services)

print (len(aws_services)) 

aws_services.remove('s3')
aws_services.remove('Lambda')

print (len(aws_services))

print(aws_services)