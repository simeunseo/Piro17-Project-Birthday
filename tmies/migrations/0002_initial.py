<<<<<<< Updated upstream
# Generated by Django 4.1 on 2022-08-17 09:12
=======
# Generated by Django 4.1 on 2022-08-17 06:18
>>>>>>> Stashed changes

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< Updated upstream
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tmies', '0001_initial'),
=======
        ('tmies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> Stashed changes
    ]

    operations = [
        migrations.AddField(
            model_name='tmimessage',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL),
        ),
    ]
