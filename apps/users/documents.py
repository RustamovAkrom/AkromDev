# from django_elasticsearch_dsl import Document, Index
# from django_elasticsearch_dsl.registries import registry
# from .models import UserAccount


# my_model_index = Index("mymodels")

# my_model_index.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )

# @registry.register_document
# @my_model_index.doc_type
# class UserAccountDocument(Document):
#     class Django:
#         model = UserAccount
#         fields = (
#             "first_name",
#             "last_name",
#             "username",
#             "email",
#             "bio",
#             "birthday",
#             "phone_number",
#             "gender",
#             "country",
#         )