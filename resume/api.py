import sys
from django.core.serializers import json
from django.utils import simplejson
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie import fields
from tastypie.serializers import Serializer
from tastypie.constants import ALL

from models import Person, Resume, EntrySection, Entry

class CustomJSONSerializer(Serializer):
	"""A simple pretty-print serializer for JSON data."""
	json_indent = 2
	def to_json(self, data, options=None):
		options = options or {}
		data = self.to_simple(data, options)
		if 'objects' in data:
			data['rows'] = data['objects']
			del data['objects']
		else:
			d = {}
			d['rows'] = [data,]
			data = d
		data['records'] = len(data['rows'])
		data['total'] = data['records']
		data['page'] = 1
		return simplejson.dumps(data, cls=json.DjangoJSONEncoder,
				sort_keys=True, ensure_ascii=False, indent=self.json_indent)

class CommonMeta:
	"""There are a variety of common elements for this API.

	All elements use a common JSON pretty-print serializer, no authentication,
	no authorization, and only allow 'GET' operations (no writing of data).
	"""
	serializer = CustomJSONSerializer()
	authentication = Authentication();
	authorization = Authorization()
	allowed_methods = ['get']

class PersonResource(ModelResource):
	resumes = fields.ToManyField('resume.api.ResumeResource', 'resume_set',
			full=False)
	class Meta(CommonMeta):
		queryset = Person.objects.all()

class ResumeResource(ModelResource):
	person = fields.ToOneField(PersonResource, 'person', full=True)
	sections = fields.ToManyField('resume.api.EntrySectionResource',
			'section_set', full=True)
	class Meta(CommonMeta):
		queryset = Resume.objects.all()
	
class EntrySectionResource(ModelResource):
	entries = fields.ToManyField('resume.api.EntryResource',
			'entry_set', full=True)
	class Meta(CommonMeta):
		queryset = EntrySection.objects.all()
	
class EntryResource(ModelResource):
	class Meta(CommonMeta):
		queryset = Entry.objects.all()
	

