
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Cost', models.FloatField()),
                ('Added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('Trip_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Contact_Person', models.CharField(max_length=200)),
                ('Department', models.CharField(max_length=200)),
                ('Place', models.CharField(max_length=200)),
                ('Purpose', models.CharField(max_length=200)),
                ('Date_Departed', models.DateField()),
                ('Time_Departed', models.TimeField()),
                ('Date_Returned', models.DateField()),
                ('Time_Returned', models.TimeField()),
                ('Is_Active', models.CharField(max_length=5)),
                ('Username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyExpenses',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='forms.Post')),
                ('DailyExpense_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Category', models.CharField(choices=[(b'Lodging', b'Lodging'), (b'Meal Tips', b'Meal Tips'), (b'Taxi', b'Taxi'), (b'Parking, Tolls', b'Parking, Tolls'), (b'Gasoline', b'Gasoline'), (b'Business Calls', b'Business Calls')], default=b'Lodging', max_length=30)),
            ],
            bases=('forms.post',),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='forms.Post')),
                ('Meal_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Meal_Category', models.CharField(choices=[(b'Breakfast', b'Breakfast'), (b'Lunch', b'Lunch'), (b'Dinner', b'Dinner')], default=b'Breakfast', max_length=30)),
                ('Tip', models.FloatField()),
            ],
            bases=('forms.post',),
        ),
        migrations.AddField(
            model_name='post',
            name='Trip_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Trip'),
        ),
    ]
