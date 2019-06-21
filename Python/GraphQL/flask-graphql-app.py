from flask import Flask
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView

class Query(ObjectType):
	fname = String(description='fname')
	lname = String(description='lname')

	def resolve_fname(self, info):
		return 'Jitendra'

	def resolve_lname(self, info):
		return 'Nirnejak'
	
	def resolve_name(self, info):
		return 'Jitendra Nirnejak'

view_func = GraphQLView.as_view('graphql', schema=Schema(query=Query), graphiql = True)

app = Flask(__name__)
app.debug = True
app.add_url_rule('/', view_func = view_func)

if __name__ == '__main__':
    app.run()