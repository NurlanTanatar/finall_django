# Generated by Django 4.0.3 on 2022-05-24 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookJournalBase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='processing.bookjournalbase')),
                ('num_pages', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
            ],
            bases=('processing.bookjournalbase',),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='processing.bookjournalbase')),
                ('publisher', models.CharField(max_length=255)),
            ],
            bases=('processing.bookjournalbase',),
        ),
    ]
