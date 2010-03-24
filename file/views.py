# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from ragendja.template import render_to_response
from file.models import File, Account
from mimetypes import guess_type
from ragendja.dbutils import get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime

def get(request, key):
	# raise key
	file = get_object_or_404(File, key)
	
	return HttpResponse(file.data, content_type=guess_type(file.name)[0] or 'application/octet-stream')
		
def put(request, public_key, secret_key):
	account = get_object_or_404(Account, 'public_key =', public_key, 'secret_key =', secret_key)
	request_file = request.FILES['myfile']
	file = File(
		name = request_file.name,
		data = request_file.read(),
		owner = account,
		added_date = datetime.now(),
		size = request_file.size
	)
	
	file.put()
	
	return HttpResponse(file.key())

def delete(request, public_key, secret_key, key):
	account = get_object_or_404(Account, 'public_key =', public_key, 'secret_key =', secret_key)
	file = get_object_or_404(File, key)
	file.delete()

	return HttpResponse('ok')
