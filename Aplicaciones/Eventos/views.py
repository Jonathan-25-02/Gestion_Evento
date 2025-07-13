
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
    nombre = request.POST["nombre"]
    nuevaCarrera = Carrera.objects.create(nombre=nombre)
    messages.success(request, "Carrera guardado exitosamente")
    return redirect('/carrera')


def eliminarCarrera(request, id):
    carreraEliminar = get_object_or_404(Carrera, id=id)
    carreraEliminar.delete()

    return redirect('/carrera')


def editarCarrera(request, id):
    carreraEditar = get_object_or_404(Carrera, id=id)
    return render(request, "editarCarrera.html", {'carreraEditar': carreraEditar})


def procesarEdicionCarrera(request, id):
    nombre = request.POST["nombre"]
    # Aquí debes adaptar según los campos reales del modelo
    carreraEditar = get_object_or_404(Carrera, id=id)
    carreraEditar.nombre = nombre
    carreraEditar.save()
    messages.success(request, "Carrera actualizado exitosamente")
    return redirect('/carrera')



# Vistas para Usuario
def usuario(request):
    registros = Usuario.objects.all()
    return render(request, "usuario.html", {'usuarios': registros})


def nuevoUsuario(request):
    carreras = Carrera.objects.all()
    return render(request, "nuevoUsuario.html", {'carreras': carreras})



def guardarUsuario(request):
    nombre_completo = request.POST["nombre_completo"]
    correo = request.POST["correo"]
    tipo = request.POST["tipo"]
    carrera_id = request.POST["carrera"]  # Aquí recibes el ID, no el nombre
    semestre = request.POST["semestre"]

    carrera_obj = get_object_or_404(Carrera, id=carrera_id)  # 🔥 Aquí obtienes la instancia

    nuevoUsuario = Usuario.objects.create(
        nombre_completo=nombre_completo,
        correo=correo,
        tipo=tipo,
        carrera=carrera_obj,  # ✅ Asignas el objeto Carrera, no un string
        semestre=semestre
    )
    messages.success(request, "Usuario guardado exitosamente")
    return redirect('/usuario')



def eliminarUsuario(request, id):
    usuarioEliminar = get_object_or_404(Usuario, id=id)
    usuarioEliminar.delete()

    return redirect('/usuario')


def editarUsuario(request, id):
    usuarioEditar = get_object_or_404(Usuario, id=id)
    carreras = Carrera.objects.all()
    return render(request, "editarUsuario.html", {
        'usuarioEditar': usuarioEditar,
        'carreras': carreras
    })

def procesarEdicionUsuario(request, id):
    usuarioEditar = get_object_or_404(Usuario, id=id)
    usuarioEditar.nombre_completo = request.POST["nombre_completo"]
    usuarioEditar.correo = request.POST["correo"]
    usuarioEditar.tipo = request.POST["tipo"]

    carrera_id = request.POST["carrera"]
    carrera_obj = get_object_or_404(Carrera, id=carrera_id)  # ✅ esto es importante
    usuarioEditar.carrera = carrera_obj  # ✅

    usuarioEditar.semestre = request.POST["semestre"]
    usuarioEditar.save()
    messages.success(request, "Usuario actualizado exitosamente")
    return redirect('/usuario')



# Vistas para Evento
def evento(request):
    eventos = Evento.objects.all()
    return render(request, "evento.html", {'eventos': eventos})


def nuevoEvento(request):
    modalidades = ModalidadEvento.objects.all()
    organizadores = Usuario.objects.filter(tipo='docente')  # Asumiendo que los docentes son los organizadores
    return render(request, "nuevoEvento.html", {'modalidades': modalidades, 'organizadores': organizadores})


def guardarEvento(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    cupos = request.POST["cupos"]
    modalidad_id = request.POST["modalidad"]
    organizador_id = request.POST["organizador"]
    modalidad = ModalidadEvento.objects.get(id=modalidad_id)
    organizador = Usuario( id=organizador_id)

    nuevoevento = Evento.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        cupos=cupos,
        modalidad=modalidad,
        organizador=organizador
    )
    messages.success(request, "Evento guardado exitosamente")
    return redirect('/evento')


def eliminarEvento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    messages.success(request, "Evento eliminado exitosamente")
    return redirect('/evento')


def editarEvento(request, id):
    eventoEditar = get_object_or_404(Evento, id=id)
    modalidades = ModalidadEvento.objects.all()
    organizadores = Usuario.objects.filter(tipo='docente')  # Asumiendo que los docentes son los organizadores
    return render(request, "editarEvento.html", {
        'eventoEditar': eventoEditar,
        'modalidades': modalidades,
        'organizadores': organizadores
    })


def procesarEdicionEvento(request, id):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_fin = request.POST["fecha_fin"]
    cupos = request.POST["cupos"]
    modalidad_id = request.POST["modalidad"]
    organizador_id = request.POST["organizador"]

    eventoEditar = get_object_or_404(Evento, id=id)
    eventoEditar.nombre = nombre
    eventoEditar.descripcion = descripcion
    eventoEditar.fecha_inicio = fecha_inicio
    eventoEditar.fecha_fin = fecha_fin
    eventoEditar.cupos = cupos
    eventoEditar.modalidad = get_object_or_404(ModalidadEvento, id=modalidad_id)
    eventoEditar.organizador = get_object_or_404(Usuario, id=organizador_id)
    eventoEditar.save()
    messages.success(request, "Evento actualizado exitosamente")
    return redirect('/evento')



# Vistas para ModalidadEvento
def modalidadevento(request):
    registros = ModalidadEvento.objects.all()
    return render(request, "modalidadevento.html", {'modalidad_eventos': registros})


def nuevaModalidadEvento(request):
    return render(request, "nuevaModalidadEvento.html")


def guardarModalidadEvento(request):
    tipo = request.POST["tipo"]
    nuevoModalidad = ModalidadEvento.objects.create(
        tipo=tipo
    )
    messages.success(request, "Modalidad del Evento guardado exitosamente")
    return redirect('/modalidadevento')


def eliminarModalidadEvento(request, id):
    registro = get_object_or_404(ModalidadEvento, id=id)
    registro.delete()
    messages.success(request, "ModalidadEvento eliminado exitosamente")
    return redirect('/modalidadevento')


def editarModalidadEvento(request, id):
    modalidadEventoEditar = get_object_or_404(ModalidadEvento, id=id)

    return render(request, "editarModalidadEvento.html", {'modalidadevento': modalidadEventoEditar})


def procesarEdicionModalidadEvento(request, id):
    tipo = request.POST["tipo"]
    registro = get_object_or_404(ModalidadEvento, id=id)
    registro.tipo = tipo
    registro.save()
    messages.success(request, "ModalidadEvento actualizado exitosamente")
    return redirect('/modalidadevento')



# Vistas para Inscripcion
def inscripcion(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, "inscripcion.html", {'inscripciones': inscripciones})


def nuevaInscripcion(request):
    usuarios = Usuario.objects.all()
    eventos = Evento.objects.all()
    estados = EstadoInscripcion.objects.all()
    return render(request, "nuevaInscripcion.html", {
        'usuarios': usuarios,
        'eventos': eventos,
        'estados': estados
    })


def guardarInscripcion(request):
    # Aquí debes adaptar según los campos reales del modelo
    usuario_id = request.POST["usuario"]
    evento_id = request.POST["evento"]
    estado_id = request.POST["estado"]
    fecha_inscripcion = request.POST["fecha_inscripcion"]

    nuevaInscripcion = Inscripcion.objects.create(
        usuario_id=usuario_id,
        evento_id=evento_id,
        estado_id=estado_id,
        fecha_inscripcion=fecha_inscripcion
    )
    messages.success(request, "Inscripcion guardado exitosamente")
    return redirect('/inscripcion')


def eliminarInscripcion(request, id):
    inscripcionEliminar = get_object_or_404(Inscripcion, id=id)
    inscripcionEliminar.delete()
    messages.success(request, "Inscripcion eliminado exitosamente")
    return redirect('/inscripcion')


def editarInscripcion(request, id):
    inscripcionEditar = get_object_or_404(Inscripcion, id=id)
    usuarios = Usuario.objects.all()
    eventos = Evento.objects.all()
    estados = EstadoInscripcion.objects.all()
    return render(request, "editarInscripcion.html", {
        'inscripcion': inscripcionEditar,
        'usuarios': usuarios,
        'eventos': eventos,
        'estados': estados
    })


def procesarEdicionInscripcion(request, id):
    # Aquí debes adaptar según los campos reales del modelo
    usuario = request.POST["usuario"]
    evento = request.POST["evento"]
    estado = request.POST["estado"]
    fecha_inscripcion = request.POST["fecha_inscripcion"]
    inscripcion = get_object_or_404(Inscripcion, id=id)
    inscripcion.usuario = usuario
    inscripcion.evento = evento
    inscripcion.estado = estado
    inscripcion.fecha_inscripcion = fecha_inscripcion
    inscripcion.save()
    messages.success(request, "Inscripcion actualizado exitosamente")
    return redirect('/inscripcion')



# Vistas para EstadoInscripcion
def estadoinscripcion(request):
    listadoEstadoInscripcion = EstadoInscripcion.objects.all()
    return render(request, "estadoinscripcion.html", {'Inscripciones': listadoEstadoInscripcion})


def nuevoEstadoInscripcion(request):
    return render(request, "nuevoEstadoInscripcion.html")


def guardarEstadoInscripcion(request):
    nombre = request.POST["nombre"]
    nuevoEstadoInscripcion = EstadoInscripcion.objects.create(nombre=nombre)

    messages.success(request, "EstadoInscripcion guardado exitosamente")
    return redirect('/estadoinscripcion')


def eliminarEstadoInscripcion(request, id):
    estadoInscripcionEliminar = get_object_or_404(EstadoInscripcion, id=id)
    estadoInscripcionEliminar.delete()
    messages.success(request, "EstadoInscripcion eliminado exitosamente")
    return redirect('/estadoinscripcion')


def editarEstadoInscripcion(request, id):
    estadoInscripcionEditar = get_object_or_404(EstadoInscripcion, id=id)
    return render(request, "editarEstadoInscripcion.html", {'estadoInscripcionEditar': estadoInscripcionEditar})


def procesarEdicionEstadoInscripcion(request, id):
    nombre = request.POST["nombre"]
    estadoinscripcion = get_object_or_404(EstadoInscripcion, id=id)
    estadoinscripcion.nombre = nombre
    estadoinscripcion.save()
    messages.success(request, "EstadoInscripcion actualizado exitosamente")
    return redirect('/estadoinscripcion')



# Vistas para ArchivoRequisito
def archivorequisito(request):
    listadoArchivoRequisito = ArchivoRequisito.objects.all()
    return render(request, "archivorequisito.html", {'archivos_requisitos': listadoArchivoRequisito})


def nuevoArchivoRequisito(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, "nuevoArchivoRequisito.html", {'inscripciones': inscripciones})

def guardarArchivoRequisito(request):
    inscripcion_id = request.POST["inscripcion"]
    archivo = request.FILES["archivo"]
    tipo_archivo = request.POST["tipo_archivo"]
    fecha_subida = request.POST["fecha_subida"]
    nuevoArchivoRequisito = ArchivoRequisito.objects.create(
        inscripcion_id=inscripcion_id,
        archivo=archivo,
        tipo_archivo=tipo_archivo,
        fecha_subida=fecha_subida
    )
    messages.success(request, "ArchivoRequisito guardado exitosamente")
    return redirect('/archivorequisito')


def eliminarArchivoRequisito(request, id):
    archivoRequisitoEliminar = get_object_or_404(ArchivoRequisito, id=id)
    archivoRequisitoEliminar.delete()
    messages.success(request, "ArchivoRequisito eliminado exitosamente")
    return redirect('/archivorequisito')


def editarArchivoRequisito(request, id):
    archivoRequisitoEditar = get_object_or_404(ArchivoRequisito, id=id)
    inscripciones = Inscripcion.objects.all()
    return render(request, "editarArchivoRequisito.html", {
        'archivoRequisitoEditar': archivoRequisitoEditar,
        'inscripciones': inscripciones
    })


def procesarEdicionArchivoRequisito(request, id):
    inscripcion_id = request.POST["inscripcion"]
    archivo = request.FILES["archivo"]
    tipo_archivo = request.POST["tipo_archivo"]
    fecha_subida = request.POST["fecha_subida"]
    archivoRequisito = ArchivoRequisito.objects.get(id=id)
    archivoRequisito.inscripcion = Inscripcion.objects.get(id=inscripcion_id)
    archivoRequisito.archivo = archivo
    archivoRequisito.tipo_archivo = tipo_archivo
    archivoRequisito.fecha_subida = fecha_subida
    archivoRequisito.save()
    messages.success(request, "ArchivoRequisito actualizado exitosamente")
    return redirect('/archivorequisito')



# Vistas para Asistencia
def asistencia(request):
    listadoAsistencia = Asistencia.objects.all()
    return render(request, "asistencia.html", {'asistencias': listadoAsistencia})


def nuevaAsistencia(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, "nuevaAsistencia.html", {'inscripciones': inscripciones})


def guardarAsistencia(request):
    inscripcion_id = request.POST["inscripcion"]
    fecha = request.POST["fecha"]
    metodo_validacion = request.POST["metodo_validacion"]
    inscripcion = Inscripcion.objects.get(id=inscripcion_id)
    nuevaAsistencia = Asistencia.objects.create(
        inscripcion=inscripcion,
        fecha=fecha,
        metodo_validacion=metodo_validacion
    )
    messages.success(request, "Asistencia guardado exitosamente")
    return redirect('/asistencia')


def eliminarAsistencia(request, id):
    asistenciaEliminar = get_object_or_404(Asistencia, id=id)
    asistenciaEliminar.delete()
    messages.success(request, "Asistencia eliminado exitosamente")
    return redirect('/asistencia')


def editarAsistencia(request, id):
    asistenciaEditar = get_object_or_404(Asistencia, id=id)
    inscripciones = Inscripcion.objects.all()
    return render(request, "editarAsistencia.html", {'asistenciaEditar': asistenciaEditar, 'inscripciones': inscripciones})


def procesarEdicionAsistencia(request, id):
    inscripcion_id = request.POST["inscripcion"]
    fecha = request.POST["fecha"]
    metodo_validacion = request.POST["metodo_validacion"]
    asistencia = get_object_or_404(Asistencia, id=id)
    asistencia.inscripcion = Inscripcion.objects.get(id=inscripcion_id)
    asistencia.fecha = fecha
    asistencia.metodo_validacion = metodo_validacion
    asistencia.save()
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


def nuevaNotificacion(request):
    return render(request, "nuevaNotificacion.html")


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
