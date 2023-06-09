import graphene
import graphql_jwt
from graphene_file_upload.scalars import Upload
from historia import models, types


# Mutation sends data to the database


# Customize the ObtainJSONWebToken behavior to include the user info
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(types.UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)


class CreateUser(graphene.Mutation):
    user = graphene.Field(types.UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = models.User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class UpdateUserProfile(graphene.Mutation):
    user = graphene.Field(types.UserType)

    class Arguments:
        user_id = graphene.ID(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        avatar = Upload(required=False)
        bio = graphene.String(required=False)
        location = graphene.String(required=False)
        website = graphene.String(required=False)

    def mutate(self, info, user_id, first_name='', last_name='', avatar='', bio='', location='', website=''):
        user = models.User.objects.get(pk=user_id)

        user.first_name = first_name
        user.last_name = last_name
        user.avatar = avatar
        user.bio = bio
        user.location = location
        user.website = website

        user.save()

        return UpdateUserProfile(user=user)


class Mutation(graphene.ObjectType):
    # Tokens
    token_auth = ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_user = CreateUser.Field()

    update_user_profile = UpdateUserProfile.Field()