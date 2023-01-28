# Generated by Django 4.1.5 on 2023-01-28 13:09

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Todu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('discreption', models.CharField(max_length=50)),
                ('chekt', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='todu', to='todu_list_app.user')),
            ],
        ),
    ]
