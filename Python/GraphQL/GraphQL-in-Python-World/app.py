from flask import Flask
from flask_graphql import GraphQLView

from models import db_session
from schema import schema

app = Flask(__name__)

app.add_url_rule('/graphql',
		# setting the view function
		view_func = GraphQLView.as_view(
				'graphql',

				# we set the schema that we generate
				schema = schema,

				# we say that we *do* want a graphiql interface
				graphiql = True
			)
	)

#@app.route('/graphiql')
#def view_func():
#	GrapheQLView.as_view('graphql', schema = schema, graphiql = True)

@app.teardown_appcontext
def remove_session(exception=None):
	db_session.remove()

if __name__=='__main__':
	app.run(debug=True)