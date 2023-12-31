# Generated by Django 4.2.7 on 2023-11-26 15:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(default='perfil/iconuser.jpg', null=True, upload_to='perfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'db_table': 'Perfil',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Precio', models.IntegerField()),
                ('Tamaño', models.CharField(max_length=50, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='images')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('ProductoOfrecido', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'Proveedor',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('idTienda', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('CategoriaTienda', models.CharField(max_length=50)),
                ('Piso', models.IntegerField(null=True)),
                ('imagen', models.ImageField(null=True, upload_to='tiendas')),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
                'db_table': 'Tienda',
            },
        ),
        migrations.CreateModel(
            name='TiendaxProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.proveedor')),
                ('idTienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tienda')),
            ],
            options={
                'verbose_name': 'Proveedor tienda',
                'verbose_name_plural': 'Proveedores tiendas',
                'db_table': 'ProveedorxTienda',
            },
        ),
        migrations.CreateModel(
            name='ReseñaxTienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Puntuacion', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('Comentario', models.CharField(max_length=100)),
                ('Fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('idTienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tienda')),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.perfil')),
            ],
            options={
                'verbose_name': 'Reseña tienda',
                'verbose_name_plural': 'Reseñas tienda',
                'db_table': 'ReseñaxTienda',
            },
        ),
        migrations.CreateModel(
            name='ReseñaProducto',
            fields=[
                ('idReseña', models.AutoField(primary_key=True, serialize=False)),
                ('Puntuacion', models.IntegerField()),
                ('Comentario', models.CharField(max_length=50)),
                ('Fecha', models.DateField()),
                ('idProducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.producto')),
                ('idUsuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reseña producto',
                'verbose_name_plural': 'Reseñas productos',
                'db_table': 'ReseñaxProducto',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='idTienda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.tienda'),
        ),
        migrations.CreateModel(
            name='EventoxTienda',
            fields=[
                ('idEvento', models.AutoField(primary_key=True, serialize=False)),
                ('NroParticipantes', models.IntegerField()),
                ('Beneficio', models.CharField(max_length=50)),
                ('FechaInicio', models.DateField()),
                ('FechaFinal', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='images')),
                ('idTienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tienda')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'db_table': 'EventoxTienda',
            },
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('idDescuento', models.AutoField(primary_key=True, serialize=False)),
                ('PorcentajeDesc', models.IntegerField()),
                ('FechaInicio', models.DateField()),
                ('FechaFinal', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='otros')),
                ('idTienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tienda')),
            ],
            options={
                'verbose_name': 'Descuento',
                'verbose_name_plural': 'Descuentos',
                'db_table': 'Descuento',
            },
        ),
    ]
