from pprint import pprint
import json
import boto3
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name='eu-west-2') 
    table = dynamodb.Table('VisitorCounter')
    response = table.get_item(
        Key={
            "Site":0,
        }
        )
    item = response['Item']
    table.update_item(
        Key={
            "Site":0,
        },
        UpdateExpression='SET Visits = :val1',
        ExpressionAttributeValues={
            ':val1': item['Visits'] + 1
        }
    )
    return {
      "statusCode": 200,
      "body": json.dumps({"Visit_Count": str(item['Visits'] + 1)})
    }
