from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# class Usuario(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     correo = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     fecha_nacimiento = models.DateField()
#     def __str__(self):
#         return self.nombre + " " + self.apellido
#     
#     class Meta:
#         db_table = 'usuario'
#         verbose_name = "Usuario"
#         verbose_name_plural = "Usuarios"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='perfil', null=True, default='perfil/iconuser.png')
    
    def __str__(self):
        return f'Perfil: {self.id}'
    
    class Meta: 
        verbose_name = 'perfil'
        verbose_name_plural = "perfiles"
        db_table = "Perfil"

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

    class Meta: 
        verbose_name = 'categoria'
        verbose_name_plural = "Categorias"
        db_table = "Categoria"
    
class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=50)
    ProductoOfrecido = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        db_table = "Proveedor"

class Tienda(models.Model):
    idTienda = models.AutoField(primary_key=True, null=False)
    Nombre = models.CharField(max_length=50)
    CategoriaTienda = models.CharField(max_length=50)
    Piso = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to='tiendas', null=True)

    def __str__(self):
        return self.Nombre

    class Meta:
        verbose_name = "Tienda"
        verbose_name_plural = "Tiendas"
        db_table = "Tienda"

class Descuento(models.Model):
    idDescuento = models.AutoField(primary_key=True)
    PorcentajeDesc = models.IntegerField()
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='otros', null=True)

    def __str__(self):
        return f'idDescuento = {self.idDescuento}'

    class Meta:
        verbose_name = "Descuento"
        verbose_name_plural = "Descuentos"
        db_table = "Descuento"

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Precio = models.IntegerField()
    Tamaño = models.CharField(max_length=50, null=True)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return f'Producto: {self.Nombre} - Tienda: {self.idTienda}'

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        db_table = "Producto"

class ReseñaProducto(models.Model):
    idReseña = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    idUsuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Puntuacion = models.IntegerField()
    Comentario = models.CharField(max_length=50)
    Fecha = models.DateField()

    def __str__(self):
        return f"Reseña id: {self.idReseña}"

    class Meta:
        verbose_name = "Reseña producto"
        verbose_name_plural = "Reseñas productos"
        db_table = "ReseñaxProducto"

class ReseñaxTienda(models.Model):
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    Puntuacion = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
     )
    Comentario = models.CharField(max_length=100)
    Fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Usuario: {self.idUsuario.user.username} Tienda: {self.idTienda.Nombre}"

    class Meta:
        verbose_name = "Reseña tienda"
        verbose_name_plural = "Reseñas tienda"
        db_table = "ReseñaxTienda"

class TiendaxProveedor(models.Model):
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Proveedor: {self.idProveedor} Tienda: {self.idTienda}"
    
    class Meta:
        verbose_name = "Proveedor tienda"
        verbose_name_plural = "Proveedores tiendas"
        db_table = "ProveedorxTienda"

class EventoxTienda(models.Model):
    idEvento = models.AutoField(primary_key=True)
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    NroParticipantes = models.IntegerField()
    Beneficio = models.CharField(max_length=50)
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    imagen = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return f"Evento id: {self.idEvento}"

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        db_table = "EventoxTienda"
    