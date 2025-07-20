
from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class ModalidadEvento(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo


class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    clave = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20)  # estudiante, docente, admin
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True)
    semestre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_completo


class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupos = models.PositiveIntegerField()
    modalidad = models.ForeignKey(ModalidadEvento, on_delete=models.SET_NULL, null=True)
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='eventos_organizados')
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class EstadoInscripcion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoInscripcion, on_delete=models.SET_NULL, null=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} inscrito en {self.evento}"


class ArchivoRequisito(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='requisitos/')
    tipo_archivo = models.CharField(max_length=50)
    fecha_subida = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Archivo para {self.inscripcion}"


class Asistencia(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_validacion = models.CharField(max_length=50)  # QR, manual, etc.

    def __str__(self):
        return f"Asistencia de {self.inscripcion}"


class Certificado(models.Model):
    inscripcion = models.OneToOneField(Inscripcion, on_delete=models.CASCADE)
    archivo_pdf = models.FileField(upload_to='certificados/')
    codigo_verificacion = models.CharField(max_length=100, unique=True)
    fecha_emision = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Certificado para {self.inscripcion}"


class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)  # leída, no leída

    def __str__(self):
        return f"Notificación para {self.usuario}"
