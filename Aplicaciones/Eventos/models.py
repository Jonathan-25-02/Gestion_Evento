
from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    TIPO_USUARIO = [
        ('Estudiante', 'Estudiante'),
        ('Organizador', 'Organizador'),
        ('Administrador', 'Administrador'),
    ]
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    modalidad = models.CharField(max_length=50)
    lugar = models.CharField(max_length=100)
    cupo_maximo = models.IntegerField()
    requiere_requisitos = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Requisito(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f"{self.usuario} - {self.evento}"

class ArchivoRequisito(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='requisitos/', null=True, blank=True)

    def __str__(self):
        return f"Archivo - {self.inscripcion}"

class Asistencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_asistencia = models.DateTimeField(auto_now_add=True)
    qr_validado = models.BooleanField(default=False)

    def __str__(self):
        return f"Asistencia: {self.usuario} - {self.evento}"

class Certificado(models.Model):
    inscripcion = models.OneToOneField(Inscripcion, on_delete=models.CASCADE)
    archivo_certificado = models.FileField(upload_to='certificados/')
    generado = models.BooleanField(default=False)

    def __str__(self):
        return f"Certificado de {self.inscripcion.usuario}"

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=255)
    leido = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación a {self.usuario}"

class Historial(models.Model):
    usuario = models.CharField(max_length=100)
    actividad = models.CharField(max_length=210)
    fecha = models.DateField()
    resultado = models.TextField()
    logo = models.FileField(upload_to='cargos', null=True, blank=True)
    archivo = models.FileField(upload_to='documentos/', null=True, blank=True)

    def __str__(self):
        return f"{self.usuario} - {self.actividad} - {self.fecha}"
