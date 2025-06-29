
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Carrera, Usuario, Evento, ModalidadEvento, Inscripcion, EstadoInscripcion, ArchivoRequisito, Asistencia, Certificado, Notificacion


def inicio(request):
    return render(request, "inicio.html")



# Vistas para Carrera
def carrera(request):
    registros = Carrera.objects.all()
    return render(request, "carrera.html", {'carreras': registros})


def nuevoCarrera(request):
    return render(request, "nuevoCarrera.html")


def guardarCarrera(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "Carrera guardado exitosamente")
    return redirect('/carrera')


def eliminarCarrera(request, id):
    registro = get_object_or_404(Carrera, id=id)
    registro.delete()
    messages.success(request, "Carrera eliminado exitosamente")
    return redirect('/carrera')


def editarCarrera(request, id):
    registro = get_object_or_404(Carrera, id=id)
    return render(request, "editarCarrera.html", {'carrera': registro})


def procesarEdicionCarrera(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(Carrera, id=id)
    registro.save()
    messages.success(request, "Carrera actualizado exitosamente")
    return redirect('/carrera')



# Vistas para Usuario
def usuario(request):
    registros = Usuario.objects.all()
    return render(request, "usuario.html", {'usuarios': registros})


def nuevoUsuario(request):
    return render(request, "nuevoUsuario.html")


def guardarUsuario(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "Usuario guardado exitosamente")
    return redirect('/usuario')


def eliminarUsuario(request, id):
    registro = get_object_or_404(Usuario, id=id)
    registro.delete()
    messages.success(request, "Usuario eliminado exitosamente")
    return redirect('/usuario')


def editarUsuario(request, id):
    registro = get_object_or_404(Usuario, id=id)
    return render(request, "editarUsuario.html", {'usuario': registro})


def procesarEdicionUsuario(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(Usuario, id=id)
    registro.save()
    messages.success(request, "Usuario actualizado exitosamente")
    return redirect('/usuario')



# Vistas para Evento
def evento(request):
    registros = Evento.objects.all()
    return render(request, "evento.html", {'eventos': registros})


def nuevoEvento(request):
    return render(request, "nuevoEvento.html")


def guardarEvento(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "Evento guardado exitosamente")
    return redirect('/evento')


def eliminarEvento(request, id):
    registro = get_object_or_404(Evento, id=id)
    registro.delete()
    messages.success(request, "Evento eliminado exitosamente")
    return redirect('/evento')


def editarEvento(request, id):
    registro = get_object_or_404(Evento, id=id)
    return render(request, "editarEvento.html", {'evento': registro})


def procesarEdicionEvento(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(Evento, id=id)
    registro.save()
    messages.success(request, "Evento actualizado exitosamente")
    return redirect('/evento')



# Vistas para ModalidadEvento
def modalidadevento(request):
    registros = ModalidadEvento.objects.all()
    return render(request, "modalidadevento.html", {'modalidadeventos': registros})


def nuevoModalidadEvento(request):
    return render(request, "nuevoModalidadEvento.html")


def guardarModalidadEvento(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "ModalidadEvento guardado exitosamente")
    return redirect('/modalidadevento')


def eliminarModalidadEvento(request, id):
    registro = get_object_or_404(ModalidadEvento, id=id)
    registro.delete()
    messages.success(request, "ModalidadEvento eliminado exitosamente")
    return redirect('/modalidadevento')


def editarModalidadEvento(request, id):
    registro = get_object_or_404(ModalidadEvento, id=id)
    return render(request, "editarModalidadEvento.html", {'modalidadevento': registro})


def procesarEdicionModalidadEvento(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(ModalidadEvento, id=id)
    registro.save()
    messages.success(request, "ModalidadEvento actualizado exitosamente")
    return redirect('/modalidadevento')



# Vistas para Inscripcion
def inscripcion(request):
    registros = Inscripcion.objects.all()
    return render(request, "inscripcion.html", {'inscripcions': registros})


def nuevoInscripcion(request):
    return render(request, "nuevoInscripcion.html")


def guardarInscripcion(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "Inscripcion guardado exitosamente")
    return redirect('/inscripcion')


def eliminarInscripcion(request, id):
    registro = get_object_or_404(Inscripcion, id=id)
    registro.delete()
    messages.success(request, "Inscripcion eliminado exitosamente")
    return redirect('/inscripcion')


def editarInscripcion(request, id):
    registro = get_object_or_404(Inscripcion, id=id)
    return render(request, "editarInscripcion.html", {'inscripcion': registro})


def procesarEdicionInscripcion(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(Inscripcion, id=id)
    registro.save()
    messages.success(request, "Inscripcion actualizado exitosamente")
    return redirect('/inscripcion')



# Vistas para EstadoInscripcion
def estadoinscripcion(request):
    registros = EstadoInscripcion.objects.all()
    return render(request, "estadoinscripcion.html", {'estadoinscripcions': registros})


def nuevoEstadoInscripcion(request):
    return render(request, "nuevoEstadoInscripcion.html")


def guardarEstadoInscripcion(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "EstadoInscripcion guardado exitosamente")
    return redirect('/estadoinscripcion')


def eliminarEstadoInscripcion(request, id):
    registro = get_object_or_404(EstadoInscripcion, id=id)
    registro.delete()
    messages.success(request, "EstadoInscripcion eliminado exitosamente")
    return redirect('/estadoinscripcion')


def editarEstadoInscripcion(request, id):
    registro = get_object_or_404(EstadoInscripcion, id=id)
    return render(request, "editarEstadoInscripcion.html", {'estadoinscripcion': registro})


def procesarEdicionEstadoInscripcion(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(EstadoInscripcion, id=id)
    registro.save()
    messages.success(request, "EstadoInscripcion actualizado exitosamente")
    return redirect('/estadoinscripcion')



# Vistas para ArchivoRequisito
def archivorequisito(request):
    registros = ArchivoRequisito.objects.all()
    return render(request, "archivorequisito.html", {'archivorequisitos': registros})


def nuevoArchivoRequisito(request):
    return render(request, "nuevoArchivoRequisito.html")


def guardarArchivoRequisito(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "ArchivoRequisito guardado exitosamente")
    return redirect('/archivorequisito')


def eliminarArchivoRequisito(request, id):
    registro = get_object_or_404(ArchivoRequisito, id=id)
    registro.delete()
    messages.success(request, "ArchivoRequisito eliminado exitosamente")
    return redirect('/archivorequisito')


def editarArchivoRequisito(request, id):
    registro = get_object_or_404(ArchivoRequisito, id=id)
    return render(request, "editarArchivoRequisito.html", {'archivorequisito': registro})


def procesarEdicionArchivoRequisito(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(ArchivoRequisito, id=id)
    registro.save()
    messages.success(request, "ArchivoRequisito actualizado exitosamente")
    return redirect('/archivorequisito')



# Vistas para Asistencia
def asistencia(request):
    registros = Asistencia.objects.all()
    return render(request, "asistencia.html", {'asistencias': registros})


def nuevoAsistencia(request):
    return render(request, "nuevoAsistencia.html")


def guardarAsistencia(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "Asistencia guardado exitosamente")
    return redirect('/asistencia')


def eliminarAsistencia(request, id):
    registro = get_object_or_404(Asistencia, id=id)
    registro.delete()
    messages.success(request, "Asistencia eliminado exitosamente")
    return redirect('/asistencia')


def editarAsistencia(request, id):
    registro = get_object_or_404(Asistencia, id=id)
    return render(request, "editarAsistencia.html", {'asistencia': registro})


def procesarEdicionAsistencia(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(Asistencia, id=id)
    registro.save()
    messages.success(request, "Asistencia actualizado exitosamente")
    return redirect('/asistencia')



# Vistas para Certificado
def certificado(request):
    registros = Certificado.objects.all()
    return render(request, "certificado.html", {'certificados': registros})


def nuevoCertificado(request):
    return render(request, "nuevoCertificado.html")


def guardarCertificado(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "Certificado guardado exitosamente")
    return redirect('/certificado')


def eliminarCertificado(request, id):
    registro = get_object_or_404(Certificado, id=id)
    registro.delete()
    messages.success(request, "Certificado eliminado exitosamente")
    return redirect('/certificado')


def editarCertificado(request, id):
    registro = get_object_or_404(Certificado, id=id)
    return render(request, "editarCertificado.html", {'certificado': registro})


def procesarEdicionCertificado(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(Certificado, id=id)
    registro.save()
    messages.success(request, "Certificado actualizado exitosamente")
    return redirect('/certificado')



# Vistas para Notificacion
def notificacion(request):
    registros = Notificacion.objects.all()
    return render(request, "notificacion.html", {'notificacions': registros})


def nuevoNotificacion(request):
    return render(request, "nuevoNotificacion.html")


def guardarNotificacion(request):
    # Aquí debes adaptar según los campos reales del modelo
    messages.success(request, "Notificacion guardado exitosamente")
    return redirect('/notificacion')


def eliminarNotificacion(request, id):
    registro = get_object_or_404(Notificacion, id=id)
    registro.delete()
    messages.success(request, "Notificacion eliminado exitosamente")
    return redirect('/notificacion')


def editarNotificacion(request, id):
    registro = get_object_or_404(Notificacion, id=id)
    return render(request, "editarNotificacion.html", {'notificacion': registro})


def procesarEdicionNotificacion(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    registro = get_object_or_404(Notificacion, id=id)
    registro.save()
    messages.success(request, "Notificacion actualizado exitosamente")
    return redirect('/notificacion')
