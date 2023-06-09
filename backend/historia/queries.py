import graphene
from historia import models
from historia import types


# The Query class
class Query(graphene.ObjectType):
    site = graphene.Field(types.SiteType)

    def resolve_site(root, info):
        return (
            models.Site.objects.first()
        )
