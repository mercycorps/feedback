# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('djangocosign', '0003_auto_20151119_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, editable=False, blank=True)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('attachment', models.FileField(help_text=b'You may attach a file or screenshot if it helps to explain this issue better.', upload_to=b'uploads/issues/%Y/%m/%d/')),
                ('created_by', models.ForeignKey(related_name='feedback_attachment_created', blank=True, to='djangocosign.UserProfile', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, editable=False, blank=True)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('content', models.CharField(max_length=254)),
                ('path', models.CommaSeparatedIntegerField(max_length=250, editable=False)),
                ('depth', models.PositiveIntegerField(default=0)),
                ('created_by', models.ForeignKey(related_name='feedback_comment_created', blank=True, to='djangocosign.UserProfile', null=True)),
            ],
            options={
                'verbose_name': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, editable=False, blank=True)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('summary', models.CharField(help_text=b"<span style='color:red'>*</span> Provide a one sentence summary of the issue", max_length=80)),
                ('description', models.CharField(help_text=b"<span style='color:red'>*</span> Provide detail description of the problem/bug including steps to replicate it; if it is a feature request, describe how the feature should work and what probelm will it solve", max_length=254)),
                ('reference', models.URLField(help_text=b'Link to the page, where the issue occurs.', null=True, blank=True)),
                ('resolution', models.CharField(help_text=b'Explaining the action taken on this issue', max_length=254, null=True, blank=True)),
                ('annotation', models.CharField(help_text=b'Notes for the person working on resolving this issue.', max_length=250, null=True, blank=True)),
                ('votes_up', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('votes_dn', models.PositiveIntegerField(default=0, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='feedback_feedback_created', blank=True, to='djangocosign.UserProfile', null=True)),
            ],
            options={
                'verbose_name': 'User Feedback',
            },
        ),
        migrations.CreateModel(
            name='FeedbackVotesByUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, editable=False, blank=True)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('voted', models.BooleanField()),
                ('created_by', models.ForeignKey(related_name='feedback_feedbackvotesbyuser_created', blank=True, to='djangocosign.UserProfile', null=True)),
                ('feedback', models.ForeignKey(related_name='votes', blank=True, to='feedback.Feedback', null=True)),
                ('updated_by', models.ForeignKey(related_name='feedback_feedbackvotesbyuser_updated', blank=True, to='djangocosign.UserProfile', null=True)),
                ('voter', models.ForeignKey(related_name='votes', blank=True, to='djangocosign.UserProfile', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IssueStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, editable=False, blank=True)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('status', models.CharField(unique=True, max_length=100)),
                ('created_by', models.ForeignKey(related_name='feedback_issuestatus_created', blank=True, to='djangocosign.UserProfile', null=True)),
                ('updated_by', models.ForeignKey(related_name='feedback_issuestatus_updated', blank=True, to='djangocosign.UserProfile', null=True)),
            ],
            options={
                'verbose_name': 'Issue Status',
            },
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, editable=False, blank=True)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('issue_type', models.CharField(unique=True, max_length=100)),
                ('created_by', models.ForeignKey(related_name='feedback_issuetype_created', blank=True, to='djangocosign.UserProfile', null=True)),
                ('updated_by', models.ForeignKey(related_name='feedback_issuetype_updated', blank=True, to='djangocosign.UserProfile', null=True)),
            ],
            options={
                'verbose_name': 'Issue Type',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, editable=False, blank=True)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('message', models.CharField(max_length=250)),
                ('color', models.CharField(default=b'#cccccc', max_length=7)),
                ('icon', models.CharField(default=b'info', max_length=20)),
                ('seen', models.BooleanField(default=False)),
                ('seen_date', models.DateField(null=True, blank=True)),
                ('expiration_date', models.DateField(default=datetime.date(2016, 2, 3))),
                ('created_by', models.ForeignKey(related_name='feedback_notification_created', blank=True, to='djangocosign.UserProfile', null=True)),
                ('updated_by', models.ForeignKey(related_name='feedback_notification_updated', blank=True, to='djangocosign.UserProfile', null=True)),
                ('user', models.ForeignKey(related_name='notifications', to='djangocosign.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, editable=False, blank=True)),
                ('updated', models.DateTimeField(null=True, editable=False, blank=True)),
                ('tag', models.CharField(max_length=20)),
                ('created_by', models.ForeignKey(related_name='feedback_tag_created', blank=True, to='djangocosign.UserProfile', null=True)),
                ('updated_by', models.ForeignKey(related_name='feedback_tag_updated', blank=True, to='djangocosign.UserProfile', null=True)),
            ],
            options={
                'verbose_name': 'Tag',
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='issue_type',
            field=models.ForeignKey(related_name='feedback', to='feedback.IssueType', help_text=b"<span style='color:red'>*</span> The type of issue your are reporting."),
        ),
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.ForeignKey(related_name='feedback', blank=True, to='feedback.IssueStatus', null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='tags',
            field=models.ManyToManyField(help_text=b'Apply tags so that it is easier to find it later', related_name='feedback', to='feedback.Tag'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='updated_by',
            field=models.ForeignKey(related_name='feedback_feedback_updated', blank=True, to='djangocosign.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='feedback',
            field=models.ForeignKey(related_name='comments', to='feedback.Feedback'),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_by',
            field=models.ForeignKey(related_name='feedback_comment_updated', blank=True, to='djangocosign.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='attachment',
            name='feedback',
            field=models.ForeignKey(related_name='attachments', to='feedback.Feedback'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='updated_by',
            field=models.ForeignKey(related_name='feedback_attachment_updated', blank=True, to='djangocosign.UserProfile', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='feedbackvotesbyuser',
            unique_together=set([('voter', 'feedback')]),
        ),
    ]
