from django.urls import path
from . import views

urlpatterns = [

    path('', views.perfil_view, name='perfil'),  # Login es la página principal
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('registroDocente/', views.registro_docente, name='registroDocente'),

    # Carrera
    path('carrera', views.carrera, name='carrera'),
    path('nuevoCarrera', views.nuevoCarrera, name='nuevoCarrera'),
    path('guardarCarrera', views.guardarCarrera, name='guardarCarrera'),
    path('eliminarCarrera/<int:id>', views.eliminarCarrera, name='eliminarCarrera'),
    path('editarCarrera/<int:id>', views.editarCarrera, name='editarCarrera'),
    path('procesarEdicionCarrera/<int:id>', views.procesarEdicionCarrera, name='procesarEdicionCarrera'),

    # Usuario
    path('usuario', views.usuario, name='usuario'),
    path('nuevoUsuario', views.nuevoUsuario, name='nuevoUsuario'),
    path('guardarUsuario', views.guardarUsuario, name='guardarUsuario'),
    path('eliminarUsuario/<int:id>', views.eliminarUsuario, name='eliminarUsuario'),
    path('editarUsuario/<int:id>', views.editarUsuario, name='editarUsuario'),
    path('procesarEdicionUsuario/<int:id>', views.procesarEdicionUsuario, name='procesarEdicionUsuario'),

    # Evento
    path('evento', views.evento, name='evento'),
    path('nuevoEvento', views.nuevoEvento, name='nuevoEvento'),
    path('guardarEvento', views.guardarEvento, name='guardarEvento'),
    path('eliminarEvento/<int:id>', views.eliminarEvento, name='eliminarEvento'),
    path('editarEvento/<int:id>', views.editarEvento, name='editarEvento'),
    path('procesarEdicionEvento/<int:id>', views.procesarEdicionEvento, name='procesarEdicionEvento'),

    # ModalidadEvento
    path('modalidadevento', views.modalidadevento, name='modalidadevento'),
    path('nuevaModalidadEvento', views.nuevaModalidadEvento, name='nuevaModalidadEvento'),
    path('guardarModalidadEvento', views.guardarModalidadEvento, name='guardarModalidadEvento'),
    path('eliminarModalidadEvento/<int:id>', views.eliminarModalidadEvento, name='eliminarModalidadEvento'),
    path('editarModalidadEvento/<int:id>', views.editarModalidadEvento, name='editarModalidadEvento'),
    path('procesarEdicionModalidadEvento/<int:id>', views.procesarEdicionModalidadEvento, name='procesarEdicionModalidadEvento'),

    # Inscripcion
    path('inscripcion', views.inscripcion, name='inscripcion'),
    path('nuevaInscripcion', views.nuevaInscripcion, name='nuevaInscripcion'),
    path('guardarInscripcion', views.guardarInscripcion, name='guardarInscripcion'),
    path('eliminarInscripcion/<int:id>', views.eliminarInscripcion, name='eliminarInscripcion'),
    path('editarInscripcion/<int:id>', views.editarInscripcion, name='editarInscripcion'),
    path('procesarEdicionInscripcion/<int:id>', views.procesarEdicionInscripcion, name='procesarEdicionInscripcion'),

    # EstadoInscripcion
    path('estadoinscripcion', views.estadoinscripcion, name='estadoinscripcion'),
    path('nuevoEstadoInscripcion', views.nuevoEstadoInscripcion, name='nuevoEstadoInscripcion'),
    path('guardarEstadoInscripcion', views.guardarEstadoInscripcion, name='guardarEstadoInscripcion'),
    path('eliminarEstadoInscripcion/<int:id>', views.eliminarEstadoInscripcion, name='eliminarEstadoInscripcion'),
    path('editarEstadoInscripcion/<int:id>', views.editarEstadoInscripcion, name='editarEstadoInscripcion'),
    path('procesarEdicionEstadoInscripcion/<int:id>', views.procesarEdicionEstadoInscripcion, name='procesarEdicionEstadoInscripcion'),

    # ArchivoRequisito
    path('archivorequisito', views.archivorequisito, name='archivorequisito'),
    path('nuevoArchivoRequisito', views.nuevoArchivoRequisito, name='nuevoArchivoRequisito'),
    path('guardarArchivoRequisito', views.guardarArchivoRequisito, name='guardarArchivoRequisito'),
    path('eliminarArchivoRequisito/<int:id>', views.eliminarArchivoRequisito, name='eliminarArchivoRequisito'),
    path('editarArchivoRequisito/<int:id>', views.editarArchivoRequisito, name='editarArchivoRequisito'),
    path('procesarEdicionArchivoRequisito/<int:id>', views.procesarEdicionArchivoRequisito, name='procesarEdicionArchivoRequisito'),

    # Asistencia
    path('asistencia', views.asistencia, name='asistencia'),
    path('nuevaAsistencia', views.nuevaAsistencia, name='nuevaAsistencia'),
    path('guardarAsistencia', views.guardarAsistencia, name='guardarAsistencia'),
    path('eliminarAsistencia/<int:id>', views.eliminarAsistencia, name='eliminarAsistencia'),
    path('editarAsistencia/<int:id>', views.editarAsistencia, name='editarAsistencia'),
    path('procesarEdicionAsistencia/<int:id>', views.procesarEdicionAsistencia, name='procesarEdicionAsistencia'),
    path('generar_qr/<int:inscripcion_id>/', views.generar_qr, name='generar_qr'),
    path('registrar_asistencia/<int:inscripcion_id>/', views.registrar_asistencia, name='registrar_asistencia'),
    path('asistencia_completada/<int:id>/', views.asistencia_completada, name='asistencia_completada'),



    # Certificado
    path('certificado', views.certificado, name='certificado'),
    path('nuevoCertificado', views.nuevoCertificado, name='nuevoCertificado'),
    path('guardarCertificado', views.guardarCertificado, name='guardarCertificado'),
    path('eliminarCertificado/<int:id>', views.eliminarCertificado, name='eliminarCertificado'),
    path('editarCertificado/<int:id>', views.editarCertificado, name='editarCertificado'),
    path('procesarEdicionCertificado/<int:id>', views.procesarEdicionCertificado, name='procesarEdicionCertificado'),

    # Notificacion
    path('notificacion', views.notificacion, name='notificacion'),
    path('nuevaNotificacion', views.nuevaNotificacion, name='nuevaNotificacion'),
    path('guardarNotificacion', views.guardarNotificacion, name='guardarNotificacion'),
    path('eliminarNotificacion/<int:id>', views.eliminarNotificacion, name='eliminarNotificacion'),
    path('editarNotificacion/<int:id>', views.editarNotificacion, name='editarNotificacion'),
    path('procesarEdicionNotificacion/<int:id>', views.procesarEdicionNotificacion, name='procesarEdicionNotificacion'),

    # dashboard
    # urls.py
    path('dashboard/', views.dashboard_view, name='dashboard'),

    path('exportar_eventos_pdf/', views.exportar_eventos_pdf, name='exportar_eventos_pdf'),
    path('exportar_eventos_excel/', views.exportar_eventos_excel, name='exportar_eventos_excel'),

    path('calendario/', views.calendario_eventos, name='calendario_eventos'),






]
