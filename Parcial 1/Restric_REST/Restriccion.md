# API REST

Una **API REST** (Representational State Transfer) es un estilo arquitectónico utilizado para la creación de servicios web que permiten la interacción entre sistemas a través de HTTP. REST no es un protocolo o estándar, sino un conjunto de principios o restricciones que se utilizan para diseñar APIs simples y escalables. La clave de una API REST es la comunicación entre un cliente y un servidor utilizando recursos representados por URLs y mediante métodos estándar de HTTP, como **GET**, **POST**, **PUT**, y **DELETE**.

## Restricciones de REST

Para que una API se considere RESTful, debe cumplir con un conjunto de restricciones que definen cómo debe comportarse la API. Estas restricciones son:

### 1. **Arquitectura Cliente-Servidor**
   - Separa las responsabilidades entre cliente y servidor. El cliente maneja la interfaz de usuario y la solicitud de recursos, mientras que el servidor gestiona los datos y recursos.
   - Esto permite mayor portabilidad de la interfaz de usuario y escalabilidad del servidor.

### 2. **Sin Estado (Stateless)**
   - Cada solicitud del cliente al servidor debe contener toda la información necesaria para que el servidor la procese.
   - El servidor no almacena el estado de interacción del cliente entre solicitudes, lo que mejora la escalabilidad.

### 3. **Caché**
   - Las respuestas del servidor deben indicar si son cacheables o no. Esto permite que las respuestas se almacenen temporalmente en el cliente o intermediarios, mejorando el rendimiento.
   - El uso adecuado de caché reduce la latencia y la carga en el servidor.

### 4. **Interfaz Uniforme**
   - La API debe tener una interfaz coherente que facilite la interacción entre el cliente y el servidor. Esto incluye:
     - **Identificación de Recursos**: Los recursos deben estar identificados por URLs.
     - **Representaciones de Recursos**: Los recursos pueden representarse en diferentes formatos, como JSON o XML.
     - **Autodescriptivo**: Los mensajes de solicitud y respuesta deben ser comprensibles y contener la información necesaria para su procesamiento.
     - **HATEOAS (Hypermedia as the Engine of Application State)**: Los clientes deben poder navegar por la API usando los enlaces proporcionados en las respuestas del servidor.

### 5. **Sistemas en Capas**
   - Una API REST puede tener varias capas intermedias entre el cliente y el servidor (cachés, proxies, balanceadores de carga).
   - Estas capas son transparentes para el cliente, lo que mejora la escalabilidad y la seguridad.

### 6. **Código bajo demanda (Opcional)**
   - Aunque es opcional, una API REST puede enviar código ejecutable (como scripts) al cliente, para extender la funcionalidad de la aplicación del lado del cliente.

## Características de una API RESTful

Al cumplir con las restricciones anteriores, una API RESTful presenta las siguientes características:

### 1. **Escalabilidad**
   - La separación cliente-servidor y la ausencia de estado permiten que las aplicaciones sean más escalables y puedan manejar grandes volúmenes de solicitudes.

### 2. **Eficiencia**
   - El uso de caché, junto con la arquitectura en capas, reduce la cantidad de interacciones innecesarias con el servidor, mejorando la eficiencia general del sistema.

### 3. **Facilidad de uso**
   - La interfaz uniforme y el uso de estándares como HTTP, junto con recursos identificables y mensajes autodescriptivos, facilitan el desarrollo, uso y mantenimiento de la API.

### 4. **Simplicidad**
   - La simplicidad del diseño es uno de los beneficios principales de REST. Al seguir estas restricciones, se logra una API más fácil de entender, mantener y expandir.

## Componentes de una API REST:

- **Servidor**: Es el componente que procesa las solicitudes del cliente. Al ser sin estado, el servidor no debe almacenar información sobre la interacción previa.
- **Cliente**: El cliente interactúa con el servidor a través de las URL de los recursos, utilizando métodos HTTP para realizar las operaciones.

## Ventajas del Caché en APIs REST:
- El **caché** mejora el rendimiento, ya que reduce la cantidad de solicitudes que llegan al servidor, almacenando temporalmente las respuestas para futuras solicitudes idénticas.

## Ejemplo de Uso de una API REST:
- Imaginemos una API REST que gestione información de usuarios. El cliente puede hacer una solicitud **GET** a `https://api.example.com/users` para obtener la lista de usuarios. Si se desea agregar un nuevo usuario, se realizaría una solicitud **POST** a `https://api.example.com/users` con los datos del nuevo usuario en el cuerpo de la solicitud.

## Métodos HTTP Comunes:
- **GET**: Recuperar información de un recurso.
- **POST**: Enviar datos al servidor para crear un nuevo recurso.
- **PUT**: Actualizar un recurso existente.
- **DELETE**: Eliminar un recurso.

## Conclusión:
Las restricciones de REST son las reglas clave que definen cómo debe comportarse una API para ser considerada RESTful. Estas restricciones ayudan a garantizar que las APIs sean escalables, eficientes y fáciles de usar. Cumplir con estas restricciones ofrece numerosas ventajas como la simplicidad, la facilidad de mantenimiento y la eficiencia.
