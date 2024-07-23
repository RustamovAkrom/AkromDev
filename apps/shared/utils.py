import os
from core.config import auth


def create_default_images():

    user_account_default_img = os.path.join("media/", auth.USER_ACCOUNT_DEFAULT_IMG)
    user_accoun_bg_default_img = os.path.join(
        "media/", auth.USER_ACCOUNT_BG_DEFAULT_IMG
    )

    if not os.path.exists(user_account_default_img):
        os.makedirs(user_account_default_img)

    if not os.path.exists(user_accoun_bg_default_img):
        os.makedirs(user_accoun_bg_default_img)

    if os.path.exists(auth.USER_ACCOUNT_IMG_PATH) and os.path.exists(
        auth.USER_ACCOUNT_BG_IMG_PATH
    ):
        with open(user_account_default_img + auth.USER_ACCOUNT_IMG_NAME, "wb") as file:
            with open(auth.USER_ACCOUNT_IMG_PATH, "rb") as img:
                file.write(img.read())

        with open(
            user_accoun_bg_default_img + auth.USER_ACCOUNT_BG_IMG_NAME, "wb"
        ) as file:
            with open(auth.USER_ACCOUNT_BG_IMG_PATH, "rb") as img:
                file.write(img.read())
        return
    print("User default images path not found !")
    exit(1)
