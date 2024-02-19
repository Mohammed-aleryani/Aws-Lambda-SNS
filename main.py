import boto3

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')
sns_topic_arn = '<Topic Arn>'  # Replace with your SNS topic ARN

def lambda_handler(event, context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']  # File name
        
        response = s3_client.get_object(Bucket=bucket, Key=key)
        file_content = response['Body'].read().decode('utf-8')
        words_count = len(file_content.split())
        
        send_email(key, words_count)
    except Exception as e:
        print(f'An error occurred: {e}')
        raise e  # Rethrow the exception to trigger a Lambda retry

def send_email(file_name, count):
    try:
        message = f'The word count in the {file_name} file is {count}.'
        sns_client.publish(TopicArn=sns_topic_arn, Message=message)
    except Exception as e:
        print(f'Failed to send email: {e}')

