DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS animals;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255)
);


CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    animal_name VARCHAR(255),
    species VARCHAR(225),
    age INT,
    owner_id INT REFERENCES owners(id)
);