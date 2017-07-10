# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ShowRoomApphook(CMSApp):
    name = _("Showroom")
    app_name = "showroom"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["showroom.urls"]

apphook_pool.register(ShowRoomApphook)
