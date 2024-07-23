from apps.shared.utils import create_default_images

AUTH_USER_MODEL = "users.User"

USER_ACCOUNT_IMG_PATH = "core/images/avatar.jpg"
USER_ACCOUNT_DEFAULT_IMG = "avatar/default/"
USER_ACCOUNT_IMG_NAME = "avatar.jpg"


USER_ACCOUNT_BG_IMG_PATH = "core/images/bg.jpg"
USER_ACCOUNT_BG_DEFAULT_IMG = "bg/default/"
USER_ACCOUNT_BG_IMG_NAME = "bg.jpg"

create_default_images()
