# Generated by Django 4.2.3 on 2023-08-05 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_recipe_photo_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]