from django.utils.translation import gettext_lazy as _


class AkromDevSite:
    site_title: str = _("AkromDev")
    site_header: str = _("AkromDev")
    site_url: str = "/"
    site_brand: str = _("AkromDev")
    site_icon: str = "img/icon.png"
    site_logo: str = "ing/icon.png"
    site_user_avatar: str = "img/avatar.png"
    topmenu_links: list[dict] = [
        {"name": "Home", "url": "/"},
        {"name": "About", "url": "about/"},
        {"name": "Contact", "url": "contacts/"},
        {"name": "Blog", "url": "blogs/"},
        {"name": "Pictures", "url": "pictures/"},
        {"name": "Videos", "url": "videos/"},
    ]
