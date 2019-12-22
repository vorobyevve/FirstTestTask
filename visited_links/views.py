from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from visited_links.models import Link


# Create your views here.

def remove_str_from_links(links):
    list_str_remove = ['https://', 'http://']
    for remove in list_str_remove:
        links = links.replace(remove, '', 1)

    list_special_characters = ['?', '/']
    for character in list_special_characters:
        links = links.split(character, 1)[0]
    return links

def generate_html(found_link):
    if len(found_link) == 0:
        return '<h1>По вашему запросу не найдено ни одной ссылки!</h1>'
    else:
        base_html = '<h1>Ссылки по запросу:</h1>'
        found_link = list(set(found_link))
        damains = f'"domains":<br> {found_link}'
        
        return base_html + damains
    

def links(request):
        list_links = request.POST('links')
        processed_links = []
        for item in list_links:
            l = Link(name=remove_str_from_links(item), visiting_time=datetime.now())
            l.save()

        
