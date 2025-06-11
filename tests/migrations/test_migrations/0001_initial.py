from django.db import migrations, models
import django_singlestore.schema


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            name='Tribble',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fluffy', models.BooleanField(default=True)),
                ('bool', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True)),
                ('age', models.IntegerField(default=0)),
                ('silly_field', models.BooleanField(default=False)),
            ],
            options={
                'unique_together': {('name', 'slug')},
            },
            managers=[
                ('objects', django_singlestore.schema.ModelStorageManager('ROWSTORE REFERENCE')),
            ],
        ),
    ]
    