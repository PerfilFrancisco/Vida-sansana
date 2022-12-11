from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
    



class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Carrera(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carrera'

class Puntuacion(models.Model):
    puntuacion = models.IntegerField()
    id_puntuacion = models.AutoField(primary_key=True)
    usu_rut = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    publ_id = models.ForeignKey('PublicacionPy', on_delete=models.CASCADE)

    class Meta:
        db_table = 'puntuacion'

class Comentario(models.Model):
    comentario = models.TextField(blank=True, null=True)
    comentario_id = models.AutoField(primary_key=True)
    usu_rut = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    publ_id = models.ForeignKey('PublicacionPy', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comentario'

class Dia(models.Model):
    dia_id = models.IntegerField(primary_key=True)
    dia_nombre = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dia'
    def __str__(self):
        return self.dia_nombre

class DiaTaller(models.Model):
    dia = models.OneToOneField(Dia, models.DO_NOTHING, primary_key=True)
    tall = models.ForeignKey('Taller', models.DO_NOTHING)
    dt_hora_incio = models.CharField(max_length=6, blank=True, null=True)
    dt_hora_fin = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dia_taller'
        unique_together = (('dia', 'tall'),)
    def __str__(self):
        return self.dia

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hito(models.Model):
    hito_id = models.AutoField(primary_key=True)
    hito_actividad = models.TextField(blank=True, null=True)
    hito_docencia = models.TextField(blank=True, null=True)
    hito_reglamentario = models.TextField(blank=True, null=True)
    hito_fecha_inicio = models.DateField(blank=True, null=True)
    hito_fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hito'


class HitoSede(models.Model):
    hito = models.OneToOneField(Hito, models.DO_NOTHING, primary_key=True)
    sede = models.ForeignKey('Sede', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hito_sede'
        unique_together = (('hito', 'sede'),)


class PublicacionPy(models.Model):
    publ_id = models.IntegerField(primary_key=True)
    publ_nombre = models.CharField(max_length=45)
    publ_descripcion = models.CharField(max_length=45)
    publ_ubicacion = models.CharField(max_length=45)
    publ_precio = models.CharField(max_length=45)
    publ_creacion = models.CharField(max_length=45)
    publ_stock = models.CharField(max_length=45)
    publ_visibilidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicacion_py'


class Sede(models.Model):
    sede_id = models.AutoField(primary_key=True)
    sede_nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sede'
    def __str__(self):
        return self.sede_nombre


class TallUsuario(models.Model):
    usu_rut = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='usu_rut', primary_key=True)
    tall = models.ForeignKey('Taller', models.DO_NOTHING)

    def save(self,*args,**kwargs):
        super(TallUsuario, self).save(*args,**kwargs)

    class Meta:
        managed = False
        db_table = 'tall_usuario'
        unique_together = (('usu_rut', 'tall'),)


class Taller(models.Model):
    tall_id = models.AutoField(primary_key=True)
    tall_nombre = models.CharField(max_length=45, blank=True, null=True)
    tall_profesor = models.CharField(max_length=45, blank=True, null=True)
    tall_descripcion = models.TextField(blank=True, null=True)
    tall_cupo_act = models.IntegerField(blank=True, null=True)
    tall_cupo_max = models.IntegerField(blank=True, null=True)
    tall_estado = models.IntegerField(blank=True, null=True)
    tall_ubicacion = models.CharField(max_length=45, blank=True, null=True)
    sede = models.ForeignKey(Sede, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taller'
    def __str__(self):
        return self.tall_nombre

class TipoUsuario(models.Model):
    tipo_usu_id = models.AutoField(primary_key=True)
    tu_nombre = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'
    # def __str__(self):
    #     return self.tu_nombre


class Usuario(models.Model):
    usu_rut = models.CharField(primary_key=True, max_length=14)
    usu_nombre = models.CharField(max_length=45, blank=True, null=True)
    usu_apellido = models.CharField(max_length=45, blank=True, null=True)
    usu_correo = models.CharField(max_length=45, blank=True, null=True)
    usu_contrasena = models.CharField(max_length=14, blank=True, null=True)
    sede = models.ForeignKey(Sede, models.DO_NOTHING)
    tipo_usu = models.ForeignKey(TipoUsuario, models.DO_NOTHING)
    car = models.ForeignKey(Carrera, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.usu_rut


class UsuarioPubl(models.Model):
    usu_rut = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='usu_rut', primary_key=True)
    publ = models.ForeignKey(PublicacionPy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario_publ'
        unique_together = (('usu_rut', 'publ'),)
