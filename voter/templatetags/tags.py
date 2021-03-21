from django import template

register = template.Library()
# if you click a vote before reloading time of another vote its showing a glitch 
# which we think will be resolved when we cahnge the vote to choice fields intead
# of buttons in templates
@register.filter
def to_char(value):
    return chr(value+64)

@register.filter('startswith')
def startswith(text):
    return text.startswith("Current")
    