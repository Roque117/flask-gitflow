# Sistema de Procesamiento Aritmético: Arquitectura Distribuida con Flask

![Python](https://img.shields.io/badge/Backend-Python_3.13-3776AB)
![Flask](https://img.shields.io/badge/Framework-Flask-000000)
![API](https://img.shields.io/badge/Architecture-REST_API-blue)
![Status](https://img.shields.io/badge/Dev-Virtualization_Technologies-orange)

Este sistema es una aplicación web de alto rendimiento que implementa una arquitectura cliente-servidor para el procesamiento de operaciones aritméticas complejas. A diferencia de las soluciones basadas exclusivamente en el lado del cliente, este proyecto delega la lógica de cómputo a un backend robusto en Python, garantizando un control total sobre la integridad del procesamiento y la seguridad de los datos.

---

## Especificaciones del Sistema

### Arquitectura de API REST
El servidor Flask expone múltiples endpoints especializados (como `/api/sumar` y `/api/calcular`) diseñados para gestionar peticiones asíncronas. La comunicación entre capas se realiza mediante el intercambio de objetos **JSON**, asegurando una transferencia de datos ligera y eficiente.

### Seguridad y Validación de Datos
Se ha implementado una capa de seguridad basada en filtrado por **expresiones regulares (Regex)** en el backend. Esto permite mitigar riesgos de inyección de código y garantiza que el motor de cálculo solo procese caracteres numéricos y operadores aritméticos válidos.

### Interfaz de Usuario Dinámica (Frontend)
Desarrollada con **CSS3 avanzado** y lógica de programación en **JavaScript**. El sistema permite la actualización dinámica del DOM, lo que ofrece una experiencia de usuario fluida al procesar resultados en tiempo real sin necesidad de recargar la página.

### Gestión Avanzada de Excepciones
El backend está programado para identificar, capturar y reportar errores críticos de ejecución, tales como:
* División por cero.
* Errores de sintaxis inválida.
* Desbordamiento de memoria.
Cada excepción es comunicada al cliente mediante códigos de estado HTTP estandarizados.

### Escalabilidad y Modularidad
La estructura interna del código sigue principios de diseño modular, lo que facilita la integración futura de funciones científicas avanzadas o la persistencia de datos mediante la conexión a sistemas de bases de datos relacionales.

---

## Guía de Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Roque117/Virtualization-Project.git](https://github.com/Roque117/Virtualization-Project.git)
