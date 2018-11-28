import os

from django.shortcuts import render, redirect
from django.conf import settings

from . import login_required
from .models import Page

PATH_TEMPLATE = 'static_generator/templates/html_pages/%s.html'

@login_required
def edit(request, page_name= None):
	if request.method == 'POST':
		if page_name:
			page = Page.objects.filter(name= page_name).first()
			path = os.path.join(settings.BASE_DIR, PATH_TEMPLATE % request.POST['name'])
			if page:
				page.name = request.POST['name']
				page.path = path
			else:
				page = Page.objects.create(
					name= request.POST['name'],
					path= path
					)

			f = open(path, 'w')
			f.write(request.POST['html'])
			f.close()
			page.save()

			return render(request, 'default_pages/editor.html', {
				'id'   : page.id,
				'name' : page.name,
				'html' : request.POST['html'],
				})
		else:
			path = os.path.join(settings.BASE_DIR, PATH_TEMPLATE % request.POST['name'])
			try:
				page = Page.objects.create(
						name= request.POST['name'],
						path= path
						)
				f = open(path, 'w')
				f.write(request.POST['html'])
				f.close()
				page.save()
			except Exception as e:
				return render(request, 'default_pages/custom_error.html', {'error' : str(e)})
			
			return redirect('/edit/' + page.name)

	elif request.method == 'GET':
		if page_name:
			page = Page.objects.filter(name= page_name).first()
			if page:
				name = page.name
				html = page.html
				page_id = page.id
			else:
				name, html, page_id = page_name, '', ''
			return render(request, 'default_pages/editor.html', {
				'id'   : page_id,
				'name' : name,
				'html' : html,
				})
		else:
			return render(request, 'default_pages/editor.html', {
				'id'   : '',
				'name' : '',
				'html' : '',
				})
	else:
		return render(request, 'default_pages/method_not_allowed.html', {})

@login_required
def get_all(request):
	return render(
		request,
		'default_pages/pages_list.html',
		{
			'pages' : Page.objects.all()
		}
		)

def index(request):
	return render(request, 'html_pages/index.html', {})

def get(request, page_name):

	if request.method == 'GET':
		page = Page.objects.filter(name= page_name).first()

		if page:
			return render(
				request,
				page.path,
				{}
				)
		else:
			return render(
				request,
				'default_pages/page_not_found.html',
				{}
				)

	else:
		return render(request, 'default_pages/method_not_allowed.html', {})