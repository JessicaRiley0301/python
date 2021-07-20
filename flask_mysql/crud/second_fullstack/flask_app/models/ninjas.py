from flask_app.config.mysqlconnection2 import connectToMySQL

from flask_app.models import dojos
#import file not class
class Ninja:
    def __init__(self, data):
        # data is a diction that contains all of the data from a row in the database
        # we need an attribute for each field in our table
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        if data['dojo_id']:
            self.dojo = dojos.Dojo.get_one({"id": data['dojo_id']})


    # in general, a CRUD application needs 5 methods
    # Create has 1 method
    # Read has 2 methods
        # Read Many things
        # Read one thing
    # Update has 1 method
    # Delete has 1 method
    # all of these methods are class methods

    @classmethod
    def create(cls, data):

        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
        # this query returns the new ninja id
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        # results is always a list of dictionaries

        all_ninjas = []

        for row in results:
            # row is each individual dictionary in the results list
            # cls(row) is instantiaing a Dog object 
            # appending to a our list of dog objects
            all_ninjas.append(cls(row))

        return all_ninjas

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        # results is a list of dictionaries
        # results[0] is the dict at index of 0

        return cls(results[0])

