# Generated by Django 4.1 on 2022-08-26 21:19

from django.db import migrations, models
import stdimage.models
import stdimage.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_name', models.CharField(max_length=200)),
                ('stars', models.IntegerField()),
                ('image', stdimage.models.JPEGField(force_min_size=False, upload_to='images/', validators=[stdimage.validators.MinSizeValidator(400, 400)], variations={'thumbnail': (400, 400, True)})),
                ('drank_date', models.DateTimeField(auto_now_add=True, verbose_name='data published')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
