# Generated by Django 4.1.5 on 2023-01-22 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_chart2_alter_chart_image_delete_chartgeo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название таблицы')),
                ('image', models.ImageField(default='', upload_to='chart2/', verbose_name='График')),
                ('topskills', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.topskills', verbose_name='График')),
            ],
        ),
    ]
