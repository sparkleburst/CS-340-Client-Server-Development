from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31889
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
        # Create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print(f"Error during insertion: {e}")
                return False
        else:
            raise Exception("Nothing to save because the data parameter is empty")
            
# Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            result = list(self.collection.find(query))
            return result
        else:
            raise Exception("Cannot perform read operation without a valid query")
            
# Create method to implement the R in CRUD.
    def update(self, query, new_data):
        if query is not None and new_data is not None:
            self.collection.update_one(query, {"$set": new_data})
            return True
        else:
            raise Exception("Both query and new_data parameters are required for update operation")

# Create method to implement the R in CRUD.
    def delete(self, query):
        if query is not None:
            self.collection.delete_one(query)
            return True
        else:
            raise Exception("Cannot perform delete operation without a valid query")


# Example usage:
# With an instance of AnimalShelter called "shelter"
#shelter = AnimalShelter()

# Example usage of create method:
#new_animal_data = {
#    'animal_type': 'Cat',
#    'breed': 'Persian',
#    'color': 'White',
#    'date_of_birth': '2021-10-20',
#    'name': 'Fluffy',
#    # ... add other attributes as needed
#}

#shelter.create(new_animal_data)

# Example usage of read method:
#query = {'animal_type': 'Dog'}
#results = shelter.read(query)

# Test the update functionality
#update_criteria = {'name': 'Fluffy'}
#new_data = {'color': 'Gray'}
#shelter.update(update_criteria, new_data)

# Test the delete functionality
#delete_criteria = {'name': 'Fluffy'}
#shelter.delete(delete_criteria)