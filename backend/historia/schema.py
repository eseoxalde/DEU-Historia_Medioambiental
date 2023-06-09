import graphene
from historia import queries, mutations


schema = graphene.Schema(query=queries.Query, mutation=mutations.Mutation)