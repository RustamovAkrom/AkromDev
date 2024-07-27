import graphene
from graphene_django.types import DjangoObjectType
from apps.users.models.useraccount_model import UserAccount


class UserAccountType(DjangoObjectType):
    class Meta:
        model = UserAccount

    
class Query(graphene.ObjectType):
    all_user_accounts = graphene.List(UserAccountType)

    def resolve_all_user_accounts(root, info):
        return UserAccount.objects.all()
    
schema = graphene.Schema(query=Query)

__all__ = ("schema", )