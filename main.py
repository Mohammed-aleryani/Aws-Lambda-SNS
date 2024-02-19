import boto3

#Configure the lambda to be triggered in S3 put and post events

s3Client=boto3.client('s3')
snsClient=boto3.client('sns')

def lambda_handler(event, context):
    
    bucket= event['Records'][0]['s3']['bucket']['name']
    key=event["Records"][0]['s3']['object']['key']  #File name
    
    
    response=s3Client.get_object(Bucket=bucket,Key=key)
    
    file_content = response['Body'].read().decode("utf-8")
    words_count=len(file_content.split())
    sendEmail( key , words_count)
    


def sendEmail(file_name, count):
    
    message= 'The word count in the {} file is {} . '.format(file_name , count)

    
    snsClient.publish(
    	#Replace <Topic Arn>
        TopicArn='<Topic Arn>',
        Message=message,
        )
