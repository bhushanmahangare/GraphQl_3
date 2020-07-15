import graphene
import graphql_jwt
import links.schema
import users.schema

class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass


# Mutations are used for sending data and queries for getting data
class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType,):
    #token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    #verify_token = graphql_jwt.verify.Field()
    #refresh_token = graphql_jwt.Refresh.Field()
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)