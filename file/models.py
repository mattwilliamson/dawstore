# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db
from django.db.models import permalink, signals

class Account(db.Model):
	name = db.StringProperty(required=True)
	public_key = db.StringProperty(required=True)
	secret_key = db.StringProperty(required=True)
	
	def __unicode__(self):
		return u'Account: %s' % self.name

class File(db.Model):
	name = db.StringProperty(required=True)
	added_date = db.DateTimeProperty()
	data = db.BlobProperty(required=True)
	size  = db.IntegerProperty()
	owner = db.ReferenceProperty(Account, required=True, collection_name='owner_set')
	
	@permalink
	def get_absolute_url(self):
		return ('file.views.get', (), {'key': self.key()})
		
	def __unicode__(self):
		return u'File: %s' % self.key()
