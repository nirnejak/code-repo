import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.Argument(
        graphene.String, default_value="stranger"))

    def resolve_hello(self, args, context, info):
        return 'Hello ' + args['name']

def main():
    schema = graphene.Schema(query=Query)
    result = schema.execute('{hello}')
    print(result.data['hello'])

if __name__ == '__main__':
    main()
