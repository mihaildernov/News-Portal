from django import template
import random
from datetime import datetime


register = template.Library()


@register.filter()
def censor(text):
   chars = ["*", "*", "*", "*", "*", "*"]
   bad_words = ["сука", "херня", "пердун", "мудила", "лох", "кретин", "дерьмо", "даун", "говно"]
   new_text = text.lower().split(' ')
   for word in new_text:
        if word in bad_words:
            temp = random.sample(chars, len(word))
            i = ''.join(temp)
            new_text = [x.replace(word, i) for x in new_text]
            res = ' '.join(new_text)
            return res


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
   return datetime.utcnow().strftime(format_string)


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()