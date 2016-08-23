from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class PublishManager(models.Model):
    # @property
    def get_query(self):
        return super(PublishManager,
                     self).get_queryset()\
                          .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title   = models.CharField(max_length=250)
    slug    = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author  = models.ForeignKey(User,
                               related_name='blog_posts')
    body    = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()  # default manager
    published = PublishManager()  # Our custom manager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    '''
    Note that we are using the strftime() function to build the URL using month
    and day with leading zeros. We will use the get_absolute_url() method in
    our templates.
    '''
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])
