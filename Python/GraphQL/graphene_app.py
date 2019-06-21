import graphene

class Query(graphene.ObjectType):
	"""docstring for Query"""
	fname = graphene.String()
	lname = graphene.String()

	def resolve_fname(self, info):
		return 'Jitendra'

	def resolve_lname(self, info):
		return 'Nirnejak'

schema = graphene.Schema(query=Query)

result_dict = schema.execute('''
	query{
		fname
		lname
	}
''')


print(result_dict.data['fname'])

result = dict(result_dict.data)
print(result)