from db.run_sql import run_sql

from models.animal import Animal
from models.owner import Owner

import repositories.animal_repository as animal_repository

def save(owner):
    sql = 'INSERT INTO owners (first_name) VALUES (%s) RETURNING *'
    values = [owner.first_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id =id
    return owner

def delete_all():
    sql = "DELETE  FROM owners"
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM owners WHERE id =%s'
    values =[id]
    run_sql(sql, values)

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        owner = Owner(result['first_name'], result['id'])
    return owner

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['first_name'], row['id'])

        owners.append(owner)

    return owners




