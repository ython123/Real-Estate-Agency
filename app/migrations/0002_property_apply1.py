# Generated by Django 4.0.8 on 2022-12-04 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property_apply1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_image', models.ImageField(upload_to='app/image/property_apply/profile_pic')),
                ('need', models.CharField(max_length=300)),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
                ('adhar_card', models.FileField(upload_to='app/image/property_apply/adhar_card')),
                ('pan_card', models.FileField(upload_to='app/image/property_apply/pan_card')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.agent')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.property_detail')),
            ],
        ),
    ]
