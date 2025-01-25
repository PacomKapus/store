# Generated by Django 4.1.4 on 2024-07-07 05:14

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
            name='CreateProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField()),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('section', models.CharField(choices=[('ALL', 'All Goods'), ('PAINTINGS', 'Paintings'), ('WALL_PANELS', 'Wall Panels'), ('FIGURES', 'Figures'), ('LETTERING', 'Lettering')], default='ALL', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(related_name='liked_comments', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
