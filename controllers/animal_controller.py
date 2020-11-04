from flask import Blueprint

from flask import Flask, render_template, request, redirect
from repositories import animal_repository
from repositories import owner_repository
from models.animal import Animal

animals_blueprint = Blueprint("animals", __name__)

# GET '/animals' 

@animals_blueprint.route('/animals')
def animals():
    animals = animal_repository.select_all()
    return render_template('animals/index.html', all_animals=animals)

# show 

@animals_blueprint.route('/animals/<id>/delete')
def delete_animal(id):
    animal_repository.delete(id)
    return redirect('index.html')