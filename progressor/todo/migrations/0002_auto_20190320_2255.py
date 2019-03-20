# Generated by Django 2.1 on 2019-03-20 17:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtask', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Todoentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_date', models.DateField(null=True)),
                ('important', models.BooleanField(default=False)),
                ('basedir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Directory')),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='which_entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Todoentry'),
        ),
    ]