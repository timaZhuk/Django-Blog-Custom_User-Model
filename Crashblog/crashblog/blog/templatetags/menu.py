from django import template
from blog.models import Category
register = template.Library() # we register our template
# template/core folder
@register.inclusion_tag('core/menu.html') # we need add the menu.html 
# we can list all categories here in menu.html
def menu():
    categories = Category.objects.all()
    return {'categories':categories}