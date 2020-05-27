import xadmin
from .models import Faq, Profile, Certifications, Contactus, Culture, Factory, Blog


class FaqModelAdmin(object):
    list_display = ["context"]


xadmin.site.register(Faq, FaqModelAdmin)


class ProfileModelAdmin(object):
    list_display = ["context"]


xadmin.site.register(Profile, ProfileModelAdmin)


class CertificationsModelAdmin(object):
    list_display = ["context"]


xadmin.site.register(Certifications, CertificationsModelAdmin)


class ContactusModelAdmin(object):
    list_display = ["context"]


xadmin.site.register(Contactus, ContactusModelAdmin)


class CultureModelAdmin(object):
    list_display = ["context"]


xadmin.site.register(Culture, CultureModelAdmin)


class FactoryModelAdmin(object):
    list_display = ["context"]


xadmin.site.register(Factory, FactoryModelAdmin)


class BlogModelAdmin(object):
    list_display = ["title"]


xadmin.site.register(Blog, BlogModelAdmin)
