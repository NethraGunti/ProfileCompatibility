# Generated by Django 3.1 on 2020-08-19 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.TextField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(help_text='(F)emale, (M)ale, (O)thers', max_length=1)),
                ('phone', models.TextField(max_length=10)),
                ('address', models.TextField(max_length=300)),
                ('social_media', models.TextField(help_text='Your social media link so we can know more about you', max_length=1000)),
                ('education', models.TextField(help_text='Details of your highest education', max_length=500)),
                ('current_company', models.TextField(help_text='Where do you work', max_length=500)),
                ('current_salary', models.TextField(help_text='Your current salary', max_length=500)),
                ('about', models.TextField(help_text='Write about yourself', max_length=500)),
                ('status', models.IntegerField(default=-1, editable=False)),
                ('question_fields', models.TextField(default=users.models.generate_questions, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
