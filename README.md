# DevOps Project: S3 File Upload Notification on WhatsApp

## Overview

This project demonstrates how to set up a notification system that sends a WhatsApp message whenever a file is uploaded to an AWS S3 bucket. The solution uses AWS Lambda, Amazon SNS, and the Meta Developer API.

## Repository Contents

- **lambda_function.py**: The main Lambda function script.
- **python.zip**: A ZIP file containing the `requests` module, necessary for the Lambda function to send HTTP requests.

## Prerequisites

1. **AWS Account**: To create S3 buckets, Lambda functions, and SNS topics.
2. **Meta Developer Account**: To use the official Meta Developer API for sending WhatsApp messages.
3. **Python 3.8 or later**: For running the Lambda function.

## Steps to Achieve This

### 1. Set Up an S3 Bucket

1. Log in to your AWS Management Console.
2. Navigate to the S3 service.
3. Create a new bucket and name it appropriately.

### 2. Create an SNS Topic

1. Navigate to the SNS service in the AWS Management Console.
2. Create a new topic and name it appropriately.
3. Note down the Topic ARN for later use.

### 3. Create a Lambda Function

1. Navigate to the Lambda service in the AWS Management Console.
2. Create a new function:
   - Choose "Author from scratch."
   - Name your function (e.g., `S3ToWhatsAppNotification`).
   - Choose Python 3.8 as the runtime.
3. In the function code section, upload the `lambda_function.py` script.

### 4. Attach a Layer to Use the Requests Module

1. Create a new Lambda layer:
   - Navigate to the Lambda Layers section.
   - Create a new layer and upload the `python.zip` file.
2. Attach the newly created layer to your Lambda function.

### 5. Set Up S3 Event Notifications

1. Navigate back to your S3 bucket.
2. Go to the "Properties" tab and find the "Event notifications" section.
3. Create a new event notification:
   - Set the event type to "All object create events."
   - Choose the SNS topic you created earlier.

### 6. Configure Lambda to Send WhatsApp Messages

1. Open your Lambda function in the AWS Management Console.
2. Add the necessary environment variables:
   - `META_API_URL` (e.g., `https://graph.facebook.com/v12.0/me/messages`)
   - `ACCESS_TOKEN` (your Meta API access token)
   - `PHONE_NUMBER` (the recipient's WhatsApp number)
3. Ensure your Lambda function has permissions to publish to the SNS topic and access the internet.

### 7. Test the Workflow

1. Upload a file to your S3 bucket.
2. Check the specified WhatsApp number for the notification message.

## Lambda Function Code

Here's a snippet of the Lambda function code (located in `lambda_function.py`):
```python
import json
import boto3
import requests

def lambda_handler(event, context):
    message = "New file uploaded to S3 bucket!"
    phone_number = 'your-whatsapp-number'
    meta_api_url = 'https://graph.facebook.com/v12.0/me/messages'
    access_token = 'your-access-token'
    payload = {
        'messaging_product': 'whatsapp',
        'to': phone_number,
        'type': 'text',
        'text': {'body': message},
    }
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(meta_api_url, json=payload, headers=headers)
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent!')
    }
```

### Conclusion
This project showcases how to integrate AWS services and the Meta Developer API to automate notifications for S3 bucket uploads. Feel free to fork the repository and customize it for your own use cases.

If you have any questions or run into any issues, please open an issue in the repository or contact me directly.

Happy coding! 🚀

