import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db

@app.teardown_appcontext
def 
teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """Present some documentation"""

    # Open the README file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class HeartRate(Resource):
    # def get(self):
        # shelf = get_db()
        # keys = list(shelf.keys())

        # devices = []

        # for key in keys:
        #     devices.append(shelf[key])

        # return {'message': 'Success', 'data': ''}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('date', required=True)
        parser.add_argument('time', required=True)
        parser.add_argument('data', required=True)
        # Parse the arguments into an object
        args = parser.parse_args()


        return {'message': 'ok', 'data':'success'}, 200


# class StatusStress(Resource):
#     def get(self, identifier):

#         return {'message': 'Device found', 'data': shelf[identifier]}, 200

#     def delete(self, identifier):

#         return '', 204


api.add_resource(HeartRate, '/hearrate')
# api.add_resource(StatusStress, '/statusstress/<string:identifier>')




