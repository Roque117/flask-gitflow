Proyecto Flask de Tecnologías de Virtualización.

Este sistema es una aplicación web robusta que implementa una arquitectura cliente-servidor para el procesamiento de operaciones aritméticas. A diferencia de soluciones basadas únicamente en el navegador, este proyecto delega la lógica de cálculo a un backend en Python, garantizando mayor control y seguridad.

Especificaciones del Sistema
Arquitectura de API REST: El servidor Flask expone múltiples endpoints (/api/sumar, /api/calcular, etc.) que gestionan peticiones asíncronas mediante el protocolo JSON.

Seguridad y Validación: Implementa filtrado por expresiones regulares (Regex) en el backend para mitigar riesgos de inyección de código y asegurar que solo se procesen caracteres numéricos y operadores válidos.

Interfaz de Usuario (Frontend): Diseñada con CSS3 avanzado y una lógica en JavaScript que permite la actualización dinámica del DOM sin recargar la página.

Manejo de Excepciones: El sistema está programado para identificar y reportar errores críticos, como la división por cero o sintaxis inválida, mediante códigos de estado HTTP adecuados.

Escalabilidad: La estructura modular del código facilita la integración futura de funciones científicas complejas o la conexión con bases de datos para el almacenamiento persistente de operaciones.
