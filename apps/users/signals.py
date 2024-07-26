# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from .models import UserAccount
# from .documents import UserAccountDocument


# @receiver(post_save, sender=UserAccount)
# def update_document(sender, instance, **kwargs):
#     UserAccountDocument().update(instance)


# @receiver(post_delete, sender=UserAccount)
# def delete_document(sender, instance, **kwargs):
#     UserAccountDocument().delete(instance)