from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class Recipe:
    schema = "recipes_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_thirty = data['under_thirty']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        if data['user_id']:
            self.user = user.User.get_by_id({"id": data['user_id']}) #the user object of th creator of the recipe

    
    # @classmethod
    # def create(cls, data):
    #     pass
    # @classmethod
    # def get_all(cls):
    #     pass
    # @classmethod
    # def get_one(cls, data):
    #     pass
    # @classmethod
    # def update(cls, data):
    #     pass
    # @classmethod
    # def delete(cls, data):
    #     pass
    # @staticmethod
    # def validate(post_data):
    #     pass

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO recipes (name, description, under_thirty, instructions, date_made, created_at, updated_at, user_id) 
            VALUES (%(name)s, %(description)s, %(under_thirty)s, %(instructions)s, %(date_made)s, NOW(), NOW(), %(user_id)s);
            """

        return connectToMySQL(cls.schema).query_db(query, data)
        #returns id of newly created recipe

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.schema).query_db(query)

        recipes = []
        for row in results:
            recipes.append(cls(row))
        
        return recipes
        
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(cls.schema).query_db(query, data)

        return cls(results[0])
    @classmethod
    def update(cls, data):
        query= """
            UPDATE recipe SET name = %(name)s, description = %(description)s, under_thirty = %(under_thirty)s, instructions = %(instructions)s,
            updated_at = NOW() WHERE id = %(id)s; 
            """
    @classmethod
    def delete(cls, data):
        query= "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(cls.schema).query_db(query, data)

    @staticmethod
    def validate(post_data):
        is_valid = True

        if len(post_data['name']) < 3:
            flash("must be at least three characters long")
            is_valid = False
        if len(post_data['description']) < 3:
            flash("must be at least three characters long")
            is_valid = False
        if len(post_data['instructions']) < 3:
            flash("must be at least three characters long")
            is_valid = False
        if len(post_data['date_made']) < 1:
            flash("must pick a date")
            is_valid = False
        if not 'under_thirty' in post_data:
            flash("must pick if under 30")
            is_valid= False
        
        return is_valid
#not sure how to validate that the radio button and date time filled out 

