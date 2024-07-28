import json


def lambda_handler(event, context):
    method = event['httpMethod']
    user_id = event['pathParameters']['id'] if 'id' in event['pathParameters'] else None
    if method == 'GET' and user_id:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'User {user_id} fetched'})
        }
    elif method == 'POST':
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'User created'})
        }
    elif method == 'PUT' and user_id:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'User {user_id} updated'})
        }
    elif method == 'DELETE' and user_id:
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'User {user_id} deleted'})
        }
    return {'statusCode': 400, 'body': 'Invalid Request'}
