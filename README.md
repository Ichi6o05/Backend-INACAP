# Back-end

Proyectos de asignatura Back-end de INACAP sede Santiago Centro
* Credenciales: **root** **1234**

---

## 📁 Estructura del Proyecto
Accede al código de cada etapa aquí:

* [📂 Sprint 1: Estructura y Navegación](./Sprint1/)
* [📂 Sprint 2: Modelos y Persistencia](./Sprint2/)
* [📂 Sprint 3: Seguridad y APIs](./Sprint3/)

---

## 🚀 Sprint 1: Estructura Base y Navegación
>*Enfoque: Arquitectura inicial, manejo de archivos estáticos y paso de datos mediante diccionarios de contexto.*

En el primer Sprint, se solicitó realizar lo siguiente:

- [x] **Arquitectura de Plantillas:** Creación de 3 vistas principales:
 - Home
 - Página Secundaria
 - Formulario.
- [x] **Navegación:** Implementación de un menú global (Navbar) funcional en todas las secciones.
- [x] **Recursos Estáticos:** Integración de imágenes, hipervínculos y estilos CSS para un diseño uniforme.
- [x] **Lógica de Vistas:** Configuración de URLs y envío de información a los templates mediante diccionarios de contexto.
- [x] **Formulario de Contacto:** Diseño de interfaz para captura de datos (Nombre, Email, Teléfono, Comentario).

---

## 📊 Sprint 2: Modelos y Base de Datos
>*Enfoque: Transformación del sitio estático a dinámico mediante el ORM de Django.*

En el segundo Sprint se solicitó realizar lo siguiente:

- [x] **Modelado de Datos:** Creación de modelos en Django para la gestión de información.
- [x] **Dinamismo en Contenidos:** Migración de la página secundaria para cargar información directamente desde la base de datos.
- [x] **Persistencia de Contactos:** Configuración del formulario para registrar y almacenar mensajes en el modelo.
- [x] **Visualización de Registros:** Nueva página con listas o tablas HTML para mostrar los usuarios/clientes registrados.
- [x] **Optimización de Código:** Uso de plantillas genéricas para mantener un diseño coherente y reutilizable.

---

## 🔒 Sprint 3: Seguridad y Servicios API
>*Enfoque: Implementación de autenticación y consumo de servicios de datos externos.*

En el tercer Sprint se solicitó realizar lo siguiente:

- [x] **Servicio de Autenticación:** Implementación de sistema de Login nativo de Django.
- [x] **Control de Acceso:** Restricción de navegación en el menú para usuarios no autenticados.
- [x] **Consumo de APIs:** Generación de una nueva página que consume y despliega información de una API externa o vía Django REST Framework (DRF).
- [x] **Gestión de Usuarios:** Registro de nuevos perfiles mediante el módulo de administración o vistas personalizadas.
- [x] **Seguridad de Datos:** Mejoras en la integridad de la información y manejo de sesiones.

---

## 🛠️ Tecnologías Utilizadas
* **Editor de código:** Visual Studio Code
* **Backend:** Python & Django
* **Base de Datos:** SQLite
* **Frontend:** HTML5, CSS3, JavaScript
* **Integraciones:** JSON APIs / Django REST Framework

---

## 🔧 Instalación y Uso
1. Clona el repositorio.
2. Crea un entorno virtual (opcional): `python -m venv venv`
3. Instala las dependencias (debo colocarlo a futuro): `pip install -r requirements.txt`
4. Ejecuta las migraciones: `python manage.py migrate` o `python -m manage migrate`
5. Efectua las migraciones: `Python manage.py makemigrations`
6. Inicia el servidor: `python manage.py runserver`



