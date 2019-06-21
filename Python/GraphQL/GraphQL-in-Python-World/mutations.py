from contextlib import contextmanager

import graphene
from sqlalchemy.exc import SQLAlchemyError

from models import User, db_session, Todo, TodoItem
from objects import UserObject

@contextmanager
def make_session_scope(Session=db_session):
	session = Session()
	session.expire_on_commit = False

	try:
		yield session
	except SQLAlchemyError:
		session.rollback()
		raise
	finally:
		session.close()

class CreateUser(graphene.Mutation):
	# Your Inputs
	class Input:
		username = graphene.String()
		email = graphene.String()

	# What you are returning
	user = graphene.Field(lambda: UserObject)
	ok = graphene.Boolean()

	# You might why this is not a class method
	# I honestly do not know the answer
	def mutate(self, args, request, info):
		with make_session_scope() as sess:
			u = User(**args)
			sess.add(u)
			sess.commit()
			return CreateUser(user = u, ok = True)

#class DeleteUser(graphene.Mutation):
#	class Input:
#		id = graphene.Int()

#	ok = graphene.Boolean()

#	def mutate(self, args, request, info):
#		with make_session_scope() as sess:
