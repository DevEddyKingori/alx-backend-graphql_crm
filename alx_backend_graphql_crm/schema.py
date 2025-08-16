import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello, GraphQL!")


shema = graphene.Schema(query=Query)
