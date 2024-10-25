
# JSON Web Token (JWT)

## ¿Qué es un JSON Web Token?

Un **JSON Web Token** (JWT) es un estándar abierto (RFC 7519) que define una forma segura de representar *claims* (afirmaciones) entre dos partes. JWT se utiliza principalmente para la autenticación y autorización de usuarios en aplicaciones web. Este token es autoverificable y permite transmitir información de manera segura en formato JSON a través de una cadena de texto compacta y segura.

Un JWT se utiliza para:
- Validar la identidad de un usuario en un sistema o servicio.
- Autorizar el acceso a diferentes recursos de una aplicación.
- Mantener la información de autenticación de forma segura y no manipulable en el lado del cliente.

## Estructura de un JWT

Un JWT está compuesto por tres partes principales, separadas por puntos (`.`):

```
HEADER.PAYLOAD.SIGNATURE
```

Cada una de estas partes tiene un propósito específico:

### 1. Header (Encabezado)

El **Header** (encabezado) describe el tipo de token y el algoritmo de cifrado que se usará para generar la firma. Generalmente, el Header incluye los siguientes atributos:

```json
{
  "alg": "HS256", // Algoritmo de cifrado (ejemplo: HMAC SHA-256)
  "typ": "JWT" // Tipo de token
}
```

Este fragmento se codifica en Base64 para formar la primera parte del JWT.

### 2. Payload (Carga útil)

La **Payload** es la parte que contiene las afirmaciones o datos específicos que queremos transmitir. Este puede incluir información sobre el usuario y datos personalizados, como:

- **sub**: Identificador único del usuario (ID).
- **name**: Nombre del usuario.
- **iat**: Fecha de emisión del token (timestamp).
- **exp**: Tiempo de expiración del token.

Ejemplo de Payload:

```json
{
  "sub": "1234567890",
  "name": "Dominic Villanueva",
  "iat": 1698614400,
  "exp": 1699220000
}
```

Esta sección también se codifica en Base64 para formar la segunda parte del JWT.

### 3. Signature (Firma)

La **Signature** se crea usando el encabezado codificado, la carga útil codificada, una clave secreta (en el caso de HMAC SHA-256) y el algoritmo especificado en el encabezado. La firma asegura que el mensaje no haya sido alterado. 

Ejemplo de creación de firma:

```text
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret
)
```

La **Signature** es la tercera parte del JWT y asegura que el token solo pueda ser validado con la clave secreta adecuada, protegiendo la integridad de los datos transmitidos.

## Representación Completa de un JWT

Un JWT completo podría tener el siguiente aspecto:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkRvbWluaWMgVmlsbGFuZXV2YSIsImlhdCI6MTY5ODYxNDQwMCwiZXhwIjoxNjk5MjIwMDAwfQ.-YZ0vTuw6zEQBNWy9jG09ev6jJ2lT2D6YOIgbgPZhF8
```

Cada parte de este JWT está codificada en Base64:
1. Encabezado: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`
2. Carga útil: `eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkRvbWluaWMgVmlsbGFuZXV2YSIsImlhdCI6MTY5ODYxNDQwMCwiZXhwIjoxNjk5MjIwMDAwfQ`
3. Firma: `-YZ0vTuw6zEQBNWy9jG09ev6jJ2lT2D6YOIgbgPZhF8`

## Conclusión

Los JSON Web Tokens (JWT) son útiles para autenticar y autorizar usuarios en sistemas distribuidos. Su estructura sencilla y su capacidad de incluir información personalizada los convierten en una herramienta valiosa en aplicaciones web modernas.
