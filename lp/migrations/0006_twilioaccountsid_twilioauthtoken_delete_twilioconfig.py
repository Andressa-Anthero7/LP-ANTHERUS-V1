# Generated by Django 4.1.6 on 2023-04-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0005_twilioconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwilioAccountSid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editado_por', models.CharField(max_length=50)),
                ('data_atualizacao', models.CharField(max_length=15)),
                ('twilio_account_sid', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TwilioAuthToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editado_por', models.CharField(max_length=50)),
                ('data_atualizacao', models.CharField(max_length=15)),
                ('twilio_auth_token', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='TwilioConfig',
        ),
    ]