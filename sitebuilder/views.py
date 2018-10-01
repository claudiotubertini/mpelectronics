import os
import json

from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.template.loader_tags import BlockNode
from django.utils._os import safe_join
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from sitebuilder.forms import ContactForm

# def contattiView(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # cd = form.cleaned_data
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#         try:
#             send_mail(subject, message, from_email, ['developers@clueb.it'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         context = {
#             'slug': 'success',
#             'page': page,
#             'form': form
#         }
#         return render(request, "/success.html", context)
#     if request.method == 'GET':
#         #return page(request, slug='contatti')
#         return render(request, "/contatti.html")


# def successView(request):
#     # return HttpResponse('Success! Thank you for your message.')
#     return page(request, slug='success')

def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        # html = markdown.markdown(f.read())
        page = Template(f.read())

    meta = None
    for i, node in enumerate(list(page.nodelist)):
        if isinstance(node, BlockNode) and node.name == 'context':
            meta = page.nodelist.pop(i)
            break
    page._meta = meta
    return page


def page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }
    if page._meta is not None:
        meta = page._meta.render(Context())
        extra_context = json.loads(meta)
        context.update(extra_context)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = 'This is the message: {} from the email: {}'.format(form.cleaned_data['message'], from_email)
        try:
            send_mail(subject, message,'developers@clueb.it', [from_email], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        context = {
            'slug': 'success',
            'page': page,
        }
        return render(request, "success.html", context)
    else:
        return render(request, 'page.html', context)




