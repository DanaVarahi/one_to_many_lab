from models.animal import Animal
from models.owner import Owner

import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository

animal_repository.delete_all()
owner_repository.delete_all()

owner_1 = Owner('Marta')
owner_2 = Owner('Toby')

owner_repository.save(owner_1)
owner_repository.save(owner_2)

animal_1 = Animal('Fluffy', 'Cat', 3, owner_1)
animal_2 = Animal('Rex', 'Dog', 10, owner_2)
animal_3 = Animal('Madness', 'Rat', 1, owner_2)

animal_repository.save(animal_1)
animal_repository.save(animal_2)
animal_repository.save(animal_3)

# print(animal_repository.select_all())
print(owner_repository.select_all())