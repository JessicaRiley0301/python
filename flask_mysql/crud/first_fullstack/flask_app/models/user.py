from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        # data is a diction that contains all of the data from a row in the database
        # we need an attribute for each field in our table
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


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

        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('user_schema').query_db( query, data )


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("user_schema").query_db(query)
        # results is always a list of dictionaries

        all_users = []

        for row in results:
            # row is each individual dictionary in the results list
            # cls(row) is instantiaing a Dog object 
            # appending to a our list of dog objects
            all_users.append(cls(row))

        return all_users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("user_schema").query_db(query, data)

        # results is a list of dictionaries
        # results[0] is the dict at index of 0

        return cls(results[0])


    @classmethod
    def update(cls, data):
        query = """
            UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s,
            updated_at = NOW() WHERE id = %(id)s;
        """

        connectToMySQL("user_schema").query_db(query, data)


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        connectToMySQL("user_schema").query_db(query, data)