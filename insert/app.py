import pymysql
import json


def lambda_handler(event, context):
    body = json.loads(event['body'])
    nombre = body['nombre']
    raza = body['raza']
    edad = body['edad']
    color = body['color']

    connection = pymysql.connect(
        host='crudflutter.c38wyyquynep.us-east-2.rds.amazonaws.com',
        user='admin',
        password='admin123',
        database='crud_flutter'
    )

    try:
        with connection.cursor() as cursor:
            query = """INSERT INTO animal(nombre, raza, edad, color) VALUES(%s, %s, %s, %s);"""
            cursor.execute(query, (nombre, raza, edad, color))
            connection.commit()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
            },
            'body': json.dumps("Animal creado correctamente")
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Ocurrió un error inesperado."})
        }
    finally:
        connection.close()