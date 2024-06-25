import json
import boto3
import requests

def lambda_handler(event, context):
    for record in event['Records']:
        # Extract S3 information from the SQS message
        message = json.loads(record['body'])
        sns_message = json.loads(message['Message'])
        s3_info = sns_message['Records'][0]['s3']
        
        bucket_name = s3_info['bucket']['name']
        file_name = s3_info['object']['key']
        
        # Prepare the WhatsApp message with dynamic fields you can use your own template 
        whatsapp_message = {
            "messaging_product": "whatsapp",
            "to": "whatsapp:123456789",  # Replace with recipient's WhatsApp number
            "type": "template",
            "template": {
                "name": "pubsub",  # Replace with your custom template name
                "language": {
                    "code": "en_US"
                },
                "components": [
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": file_name
                            },
                            {
                                "type": "text",
                                "text": bucket_name
                            }
                        ]
                    }
                ]
            }
        }
        
        # Send the message via WhatsApp using Facebook Graph API
        graph_api_url = 'https://graph.facebook.com/v19.0/123456789101112/messages' # replace with your whatsapp api url
        access_token = 'ACCESSTOKEN'  # Replace with your Facebook access token
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(graph_api_url, data=json.dumps(whatsapp_message), headers=headers)
        
        if response.status_code != 200:
            raise ValueError(f"Request to WhatsApp via Facebook Graph API returned an error {response.status_code}, the response is:\n{response.text}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent to WhatsApp')
    }
