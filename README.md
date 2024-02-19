# Word Count AWS Lambda Function

This AWS Lambda function is designed to be triggered whenever a new text file is added to an Amazon S3 bucket. Upon triggering, the function counts the number of words in the text file and sends an email notification containing the file name and word count using Amazon SNS.

## Prerequisites

Before deploying and using this Lambda function, ensure the following:

- You have an AWS account.
- You have the necessary permissions to create and manage Lambda functions, S3 buckets, and SNS topics.
- You have the AWS CLI configured with appropriate credentials.

## Deployment

1. Clone this repository to your local machine or download the `lambda_function.py` file.
2. Ensure you have the `boto3` library installed. You can install it via pip:

    ```
    pip install boto3
    ```

3. Customize the Lambda function:
   - Replace `<Topic Arn>` in the `lambda_function.py` file with the actual ARN of your SNS topic.
   - Modify the error handling or logging as per your requirements.

4. Zip the `lambda_function.py` file and any dependencies:

    ```
    zip -r word_count_lambda.zip lambda_function.py
    ```

5. Create the Lambda function:
   - Go to the AWS Lambda console.
   - Click on "Create function".
   - Choose "Author from scratch".
   - Configure the function:
     - Name: Enter a name for your function.
     - Runtime: Choose Python 3.x.
     - Execution role: Choose an existing role with necessary permissions or create a new one.
   - Upload the zip file created in step 4 as the function code.
   - Set the handler to `lambda_function.lambda_handler`.
   - Click on "Create function".

6. Configure the S3 trigger:
   - In the Lambda function configuration, click on "Add trigger".
   - Select "S3" as the trigger type.
   - Choose the bucket where you want to monitor for new files.
   - Configure the event type (e.g., "All object create events").
   - Click on "Add".

7. Test the Lambda function:
   - Upload a text file to the S3 bucket configured in step 6.
   - Check the email associated with the SNS topic for the word count notification.

## Usage

This Lambda function automatically runs whenever a new text file is added to the specified S3 bucket. It counts the number of words in the file and sends an email notification via SNS with the file name and word count.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
