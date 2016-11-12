#! /usr/bin/env python
#coding:utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from .signals import message_sent
from .utils import cached_attribute

MESSAGE_TYPE = (
    ('1', u'系统'),
    ('2', u'两人'),
    ('3', u'多人'),

)

@python_2_unicode_compatible
class Thread(models.Model):

    # subject = models.CharField(max_length=150)
    subject = models.CharField(choices=MESSAGE_TYPE, max_length=10)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through="UserThread")

    @classmethod
    def inbox(cls, user):
        # return cls.objects.filter(userthread__user=user, userthread__deleted=False)
        return cls.objects.filter(userthread__user=user, userthread__deleted=False)

    @classmethod
    def unread(cls, user):
        return cls.objects.filter(userthread__user=user, userthread__deleted=False, userthread__unread=True)

    def __str__(self):
        return "{}: {}".format(
            self.subject,
            ", ".join([str(user) for user in self.users.all()])
        )

    def get_absolute_url(self):
        return reverse("messages_thread_detail", args=[self.pk])

    # @property
    # @cached_attribute
    # def first_message(self):
    #     return self.messages.all()[0]
    #
    # @property
    # @cached_attribute
    # def latest_message(self):
    #     return self.messages.order_by("-sent_at")[0]
    #
    # @classmethod
    # def ordered(cls, objs):
    #     """
    #     Returns the iterable ordered the correct way, this is a class method
    #     because we don"t know what the type of the iterable will be.
    #     """
    #     objs = list(objs)
    #     objs.sort(key=lambda o: o.latest_message.sent_at, reverse=True)
    #     return objs


class UserThread(models.Model):

    thread = models.ForeignKey(Thread)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    unread = models.BooleanField()
    deleted = models.BooleanField()

    @property
    @cached_attribute
    def first_message(self):
        return self.thread.messages.filter(usermessage__deleted=False)[0]

    @property
    @cached_attribute
    def latest_message(self):
        return self.thread.messages.filter(usermessage__deleted=False).order_by("-sent_at")[0]

    @classmethod
    def ordered(cls, objs):
        """
        Returns the iterable ordered the correct way, this is a class method
        because we don"t know what the type of the iterable will be.
        """
        objs = list(objs)
        objs.sort(key=lambda o: o.latest_message.sent_at, reverse=True)
        return objs


class Message(models.Model):

    thread = models.ForeignKey(Thread, related_name="messages")

    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sent_messages")
    sent_at = models.DateTimeField(default=timezone.now)

    content = models.TextField()

    @classmethod
    def new_reply(cls, thread, user, content):
        msg = cls.objects.create(thread=thread, sender=user, content=content)
        thread.userthread_set.exclude(user=user).update(deleted=False, unread=True)
        message_sent.send(sender=cls, message=msg, thread=thread, reply=True)
        return msg

    @classmethod
    def new_message(cls, from_user, to_users, subject, content):
        thread = Thread.objects.create(subject=subject)
        for user in to_users:
            thread.userthread_set.create(user=user, deleted=False, unread=True)
        thread.userthread_set.create(user=from_user, deleted=True, unread=False)
        msg = cls.objects.create(thread=thread, sender=from_user, content=content)
        message_sent.send(sender=cls, message=msg, thread=thread, reply=False)
        return msg

    class Meta:
        ordering = ("sent_at",)

    def get_absolute_url(self):
        return self.thread.get_absolute_url()


class UserMessage(models.Model):

    message = models.ForeignKey(Message)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    unread = models.BooleanField()
    deleted = models.BooleanField()