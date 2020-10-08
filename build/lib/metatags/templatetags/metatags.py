from django import template
from django.utils.safestring import mark_safe
from metatags.models import MetaTag
from django.db.models import F, Value, CharField



register = template.Library()


@register.simple_tag
def metatags(site_slug):
    try:
        meta = MetaTag.objects.annotate(site_slug_field=Value(site_slug, output_field=CharField())).filter(site_slug_field__contains=F('slug'))[0]
        metaData = f'''
        
    <meta name="description" content="{meta.desc}">
    <meta name="keywords" content="{meta.keywords}">
    <meta name="author" content="{meta.author}">
    <meta name="title" content="{meta.title}">       
        '''
        if meta.index:
            metaData += ''' 
    <meta name="googlebot" content="index" />
    <meta name="robots" content="index" />
            '''
        else:
            metaData += ''' 
    <meta name="googlebot" content="noindex" />
    <meta name="robots" content="noindex" />
            '''

        if meta.follow:
            metaData += ''' 
    <meta name="googlebot" content="follow" />
    <meta name="robots" content="follow" />
            '''
        else:
            metaData += ''' 
    <meta name="googlebot" content="nofollow" />
    <meta name="robots" content="nofollow" />
            '''


        return mark_safe(metaData)
    except:
        return mark_safe('')