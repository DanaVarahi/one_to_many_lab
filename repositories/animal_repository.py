from db.run_sql import run_sql
import pdb
from models.animal import Animal
from models.owner import Owner
import repositories.owner_repository as owner_repository

def save(animal):
    sql = "INSERT INTO animals (animal_name, owner_id, species, age) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [animal.animal_name, animal.owner.id, animal.species, animal.age]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

def delete_all():
    sql = "DELETE  FROM animals"
    run_sql(sql)

def delete(id):
    sql = 'DELETE FROM animals WHERE id = %s'
    values =[id]
    run_sql(sql, values)

def select_all():
    animals =[]

    sql ='SELECT * FROM animals'
    results = run_sql(sql)

    for row in results:
        owner = owner_repository.select(row['owner_id'])
        animal = Animal(row['animal_name'], row['species'], row['age'], owner,row['id'])
        animals.append(animal)

    return animals
