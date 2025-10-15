from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True


    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ropa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('talla', models.TextField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_fabricacion', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]