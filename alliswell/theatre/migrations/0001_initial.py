# Generated by Django 4.0.5 on 2022-07-26 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_movie_delete_movies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(choices=[('KATHMANDU', 'kathmandu'), ('BHAKTAPUR', 'bhaktapur'), ('LALITPUR', 'lalitpur'), ('BUTWAL', 'butwal'), ('POKHARA', 'pokhara'), ('CHITWAN', 'chitwan')], max_length=9)),
                ('address', models.CharField(max_length=30)),
                ('no_of_screen', models.IntegerField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theatre.theatre')),
            ],
        ),
    ]
