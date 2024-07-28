import json


def lambda_handler(event, context):
    method = event['httpMethod']
    address_id = event['pathParameters']['id'] if 'id' in event['pathParameters'] else None
    if method == 'GET' and address_id:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'address {address_id} fetched'})
        }
    elif method == 'POST':
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'address created'})
        }
    elif method == 'PUT' and address_id:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'address {address_id} updated'})
        }
    elif method == 'DELETE' and address_id:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'address {address_id} deleted'})
        }
    return {'statusCode': 400, 'body': 'Invalid Request'}
