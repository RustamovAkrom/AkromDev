# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from apps.users.models.useraccount_model import UserAccount
# from apps.users.documents.user_document import UserModelDocument


# @receiver(post_save, sender=UserAccount)
# def update_document(sender, instance, **kwargs):
#     UserModelDocument().update(instance)


# @receiver(post_delete, sender=UserAccount)
# def delete_document(sender, instance, **kwargs):
#     UserModelDocument().delete(instance)
