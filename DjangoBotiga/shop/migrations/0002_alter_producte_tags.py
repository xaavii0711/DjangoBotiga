# Generated by Django 5.0.3 on 2024-03-21 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producte',
            name='tags',
            field=models.ManyToManyField(blank=True, to='shop.tag'),
        ),
    ]