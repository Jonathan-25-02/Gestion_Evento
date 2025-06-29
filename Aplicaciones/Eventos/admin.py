from django.contrib import admin
from .models import Carrera, ModalidadEvento, Usuario, Evento, EstadoInscripcion, Inscripcion, ArchivoRequisito, Asistencia,Certificado,Notificacion


admin.site.register(Carrera)
admin.site.register(ModalidadEvento)
admin.site.register(Usuario)
admin.site.register(Evento)
admin.site.register(EstadoInscripcion)
admin.site.register(Inscripcion)
admin.site.register(ArchivoRequisito)
admin.site.register(Asistencia)
admin.site.register(Certificado)
admin.site.register(Notificacion)
