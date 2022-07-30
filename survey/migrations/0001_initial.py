# Generated by Django 4.0.6 on 2022-07-30 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_question', models.CharField(max_length=100, verbose_name='Poll question')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated date')),
            ],
            options={
                'verbose_name': 'Poll',
                'verbose_name_plural': 'Polls',
                'db_table': 'polls',
            },
        ),
        migrations.CreateModel(
            name='ListChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=100, verbose_name='Choice text')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to='survey.poll', verbose_name='Poll')),
            ],
            options={
                'verbose_name': 'LictChoice',
                'verbose_name_plural': 'LictChoices',
                'db_table': 'listChoices',
            },
        ),
    ]
