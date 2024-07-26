# Generated by Django 5.0.7 on 2024-07-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('books', '0003_book_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='authors.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.CharField(choices=[('Livro', 'Livro'), ('Manga', 'Manga'), ('LightNovel', 'LightNovel'), ('Novel', 'Novel'), ('HQ', 'HQ')], default='Livro', max_length=20),
        ),
    ]
