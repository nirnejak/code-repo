# flask_sqlalchemy/schema.py

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from models import db_session, Department as DepartmentModel, Employee as EmployeeModel

class Department(SQLAlchemyObjectType):
	class Meta:
		model = DepartmentModel
		interfaces = (relay.Node, )

class DepartmentConnection(relay.Connection):
	class Meta:
		node = Department

class Employee(SQLAlchemyObjectType):
	class Meta:
		model = EmployeeModel
		interfaces = (relay.Node, )

class EmployeeConnection(relay.Connection):
	class Meta:
		node = Employee

class Query(graphene.ObjectType):
	node = relay.Node.Field()
	# Allows sorting over multiple columns, be default over the primary key
	all_employees = SQLAlchemyConnectionField(EmployeeConnection)
	# Disable sorting over this field
	all_departments = SQLAlchemyConnectionField(DepartmentConnection, sort = None)

schema = graphene.Schema(query=Query)