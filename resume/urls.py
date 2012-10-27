from django.conf.urls import patterns, include, url
"""Register the resources with the Api manager, under the general category of
'version 1' APIs.
"""
from tastypie.api import Api
from api import PersonResource, ResumeResource, EntrySectionResource, EntryResource

v1_api = Api(api_name='v1')
v1_api.register(PersonResource())
v1_api.register(ResumeResource())
v1_api.register(EntrySectionResource())
v1_api.register(EntryResource())

# Access these elements through urls like:
#   http://host/resume/api/v1/resume/1/?format=json
urlpatterns = patterns('',
	url(r'^api/', include(v1_api.urls)),
)
