import pymysql
import json


def lambda_handler(event, context):
    connection = pymysql.connect(
        host='crudflutter.c38wyyquynep.us-east-2.rds.amazonaws.com',
        user='admin',
        password='admin123',
        database='crud_flutter'
    )

    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM animal"
            cursor.execute(query)
            result = cursor.fetchall()
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': '*',
                    'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
                },
                'body': json.dumps(result)
            }
    except Exception:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Ocurrió un error inesperado."})
        }
    finally:
        connection.close()