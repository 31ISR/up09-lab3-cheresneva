# Generated by Django 4.2.2 on 2024-12-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_alter_communities_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='communities',
            name='avatar',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]