import  boto3

print('Welcome to HippiusFlow')

s3 = boto3.client('s3', endpoint_url = 'https://s3.hippius.com')


