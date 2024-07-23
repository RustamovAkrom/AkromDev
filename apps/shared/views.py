from typing import Any
from django.views import View


class BaseSharedView(View):
    def __init__(self, **kwargs: Any):

        super().__init__(**kwargs)
