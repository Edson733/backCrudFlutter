import pymysql
import json


def lambda_handler(event, context):
    body = json.loads(event['body'])
    id = body['id']
    nombre = body['nombre']
    raza = body['raza']
    edad = body['edad']
    color = body['color']

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='crud_flutter'
    )

    try:
        with connection.cursor() as cursor:
            query = "UPDATE animal SET "
            updates = []
            values = []

            if nombre is not None:
                updates.append("nombre = %s")
                values.append(nombre)
            if raza is not None:
                updates.append("raza = %s")
                values.append(raza)
            if edad is not None:
                updates.append("edad = %s")
                values.append(edad)
            if color is not None:
                updates.append("color = %s")
                values.append(color)

            query += ", ".join(updates) + " WHERE id = %s"
            values.append(id)
            cursor.execute(query, tuple(values))
            connection.commit()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS',
            },
            'body': json.dumps('Animal actualizado correctamente')
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": "Ocurrió un error inesperado."})
        }
    finally:
        connection.close()
