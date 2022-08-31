from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment
from django.contrib.auth.models import Group, User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@receiver(post_save, sender=Appointment)
def notify_post_created(sender, instance, created, **kwargs):
    recipient_list = []
    if post.category.name = "sport"
    sport_subscribers_group = Group.objects.get(name='sport_subscribers')
    users = User.objects.all()
    for users in sport_subscribers_group:
        email = user.email
        recipient_list.append(email)

    html_content = render_to_string("newss/mail_subscribers.html", {"post": instance})
    msg = EmailMultiAlternatives(
        subject = f"{instance.title_post}",
        from_email = "ya.dernov13@yandex.ru",
        to = recipient_list
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()

post_save.connect(notify_post_created, sender=Appointment)



