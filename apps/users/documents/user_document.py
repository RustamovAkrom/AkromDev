from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry
from apps.users.models.useraccount_model import UserAccount


user_model_index = Index("useraccountmodels")

user_model_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@registry.register_document
@user_model_index.doc_type
class UserModelDocument(Document):
    class Django:
        model = UserAccount
        fields = [
            # "first_name",
            # "last_name",
            # "username",
            # "email",
        ]

__all__ = ("UserModelDocument", )