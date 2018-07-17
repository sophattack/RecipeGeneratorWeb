# Generated by Django 2.1b1 on 2018-07-17 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGener', '0003_auto_20180713_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AutoGener.CanGet')),
            ],
        ),
        migrations.AlterField(
            model_name='cando',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='compose',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AutoGener.CanDo'),
        ),
    ]