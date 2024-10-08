const express = require('express');
const cors = require('cors');
const multer = require('multer');
const mysql = require('mysql2/promise');
const bodyParser = require('body-parser');
require('body-parser-xml')(bodyParser);
const jwt = require('jsonwebtoken');  // Para manejar los JWT
const bearerToken = require('express-bearer-token'); // Middleware para el token Bearer

const app = express();
const upload = multer();

const JWT_SECRET = 'your_secret_key';  // Reemplaza con una clave secreta más fuerte

// Función para crear la conexión a la base de datos
async function createConnection() {
  try {
    const connection = await mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: '',
      database: 'biblioteca',
    });
    console.log('Conexión a la base de datos establecida');
    return connection;
  } catch (err) {
    console.error('Error al conectar a la base de datos:', err);
    throw new Error('No se pudo conectar a la base de datos');
  }
}

let connection;

async function startServer() {
  try {
    connection = await createConnection();

    app.use(cors());
    app.use(express.json());
    app.use(express.text());
    app.use(express.urlencoded({ extended: true }));
    app.use(upload.none());
    app.use(bodyParser.xml());
    app.use(bearerToken()); // Middleware para obtener el token Bearer

    // Ruta de autenticación para generar un token JWT
    app.post('/login', async (req, res) => {
      const { Nombre_de_Usuario, Contraseña } = req.body;

      if (!Nombre_de_Usuario || !Contraseña) {
        return res.status(400).json({ error: 'Faltan datos de autenticación' });
      }

      try {
        const [results] = await connection.execute(
          'SELECT * FROM usuarios WHERE Nombre_de_Usuario = ? AND Contraseña = ?',
          [Nombre_de_Usuario, Contraseña]
        );

        if (results.length > 0) {
          const user = results[0];

          // Generar el token JWT
          const token = jwt.sign({ id: user.Id_Usuario, rol: user.Rol }, JWT_SECRET, {
            expiresIn: '1h',  // El token expira en 1 hora
          });

          return res.json({ token });
        } else {
          return res.status(401).json({ error: 'Credenciales inválidas' });
        }
      } catch (err) {
        console.error('Error en la autenticación:', err);
        return res.status(500).json({ error: 'Error en la autenticación' });
      }
    });

    // Middleware para verificar el token
    function authenticateToken(req, res, next) {
      const token = req.token;

      if (!token) {
        return res.status(401).json({ error: 'Acceso no autorizado' });
      }

      jwt.verify(token, JWT_SECRET, (err, user) => {
        if (err) {
          return res.status(403).json({ error: 'Token no válido o expirado' });
        }

        req.user = user;  // Añadir la información del usuario al request
        next();
      });
    }

    // Ruta protegida (requiere autenticación con token JWT)
    app.get('/usuario', authenticateToken, async (req, res) => {
      const idUsuario = req.query.Id_Usuario;

      let consulta = '';
      let parametros = [];

      if (!idUsuario) {
        consulta = 'SELECT * FROM usuarios';
      } else {
        consulta = 'SELECT * FROM usuarios WHERE Id_Usuario = ?';
        parametros = [idUsuario];
      }

      try {
        const [results] = await connection.execute(consulta, parametros);

        if (results.length > 0) {
          return res.json(results);
        } else {
          return res.status(404).json({ error: 'Usuario no encontrado' });
        }
      } catch (err) {
        console.error('Error en la consulta SQL:', err);
        return res.status(500).json({ error: 'Error al ejecutar la consulta en la base de datos' });
      }
    });

    // Ruta POST protegida (solo accesible con token válido)
    app.post('/usuario', authenticateToken, async (req, res) => {
      const { Nombre, Apellido_Paterno, Apellido_Materno, Correo_Electronico, Nombre_de_Usuario, Contraseña, Rol } = req.body;

      if (!Nombre || !Apellido_Paterno || !Correo_Electronico || !Nombre_de_Usuario || !Contraseña || !Rol) {
        return res.status(400).json({ error: 'Faltan datos obligatorios' });
      }

      try {
        const [result] = await connection.execute(
          'INSERT INTO usuarios (Nombre, Apellido_Paterno, Apellido_Materno, Correo_Electronico, Nombre_de_Usuario, Contraseña, Rol) VALUES (?, ?, ?, ?, ?, ?, ?)',
          [Nombre, Apellido_Paterno, Apellido_Materno || null, Correo_Electronico, Nombre_de_Usuario, Contraseña, Rol]
        );

        if (result.affectedRows > 0) {
          return res.json({ mensaje: 'Usuario agregado exitosamente', idUsuario: result.insertId });
        }
      } catch (err) {
        console.error('Error al insertar usuario:', err);
        return res.status(500).json({ error: 'Error al insertar el usuario en la base de datos' });
      }
    });

    // Escuchar en el puerto 3000
    app.listen(3000, () => {
      console.log('Servidor Express escuchando en el puerto 3000');
    });

  } catch (error) {
    console.error('Error crítico al iniciar el servidor:', error);
  }
}

startServer();
