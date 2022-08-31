import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from NewsPaper.news.models import Post
from django.core.mail import send_mail
from django.contrib.auth.models import Group, User


logger = logging.getLogger(__name__)


def my_job():
    posts = Post.objects.filter(category_id = 5).values("title")
    send_mail(
        subject= 'Еженедельная рассылка категории "sport"',
        message = posts,
        from_email = 'ya.dernov13@yandex.ru',
        recipient_list=[]
    )
    if post.category.name = "sport"
    sport_subscribers_group = Group.objects.get(name='sport_subscribers')
    users = User.objects.all()
    for users in sport_subscribers_group:
        email = user.email
        recipient_list.append(email)



def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="my_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")