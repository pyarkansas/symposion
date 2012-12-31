from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("symposion.sponsorship.views",
    url(r"^$", "list_all_sponsors", name="sponsor_levels"),
    url(r"^apply/$", "sponsor_apply", name="sponsor_apply"),
    url(r"^(?P<pk>\d+)/$", "sponsor_detail", name="sponsor_detail"),
)
