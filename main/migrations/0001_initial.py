# Generated by Django 4.2.6 on 2024-06-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logdata',
            fields=[
                ('contact', models.CharField(default='none', max_length=15)),
                ('expire', models.DateField(default=None)),
                ('payment', models.CharField(default='none', max_length=999)),
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
