const express = require('express');
const cors = require('cors');
const multer = require('multer');
const mysql = require('mysql2/promise');  // Usar Promises para manejo asíncrono
const bodyParser = require('body-parser');
require('body-parser-xml')(bodyParser);

const app = express();
const upload = multer();

// Función para crear la conexión a la base de datos
async function createConnection() {
  try {
    const connection = await mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: '',  // Coloca tu contraseña aquí si es necesario
      database: 'biblioteca',  // Cambia el nombre de la base de datos si es necesario
    });
    console.log('Conexión a la base de datos establecida');
    return connection;
  } catch (err) {
    console.error('Error al conectar a la base de datos:', err);
    throw new Error('No se pudo conectar a la base de datos');
  }
}

let connection;

// Inicia la conexión y maneja posibles errores
async function startServer() {
  try {
    connection = await createConnection();

    // Configurar el servidor
    app.use(cors());                                // Middleware de terceros
    app.use(express.json());                        // Middleware incorporado en Express
    app.use(express.text());                        // Middleware para manejar texto
    app.use(express.urlencoded({ extended: true })); // Middleware para formularios
    app.use(upload.none());                         // Middleware para parsear form-data
    app.use(bodyParser.xml());                      // Middleware para XML

    // Ruta para obtener el usuario por Id_Usuario o todos si no se pasa ID
    app.get('/usuario', async (req, res) => {
      const idUsuario = req.query.Id_Usuario;  // Obtiene el parámetro de la URL

      let consulta = '';
      let parametros = [];

      // Si no se proporciona un ID, obtener todos los usuarios
      if (!idUsuario) {
        consulta = 'SELECT * FROM usuarios';
      } else {
        consulta = 'SELECT * FROM usuarios WHERE Id_Usuario = ?';
        parametros = [idUsuario];
      }

      try {
        const [results, fields] = await connection.execute(consulta, parametros);

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

    // Ruta POST para agregar un nuevo usuario
    app.post('/usuario', async (req, res) => {
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

    // Ruta DELETE para eliminar un usuario por Id_Usuario
    app.delete('/usuario', async (req, res) => {
      const idUsuario = req.query.Id_Usuario;

      if (!idUsuario) {
        return res.status(400).json({ error: 'Id_Usuario es requerido para eliminar un usuario' });
      }

      try {
        const [result] = await connection.execute('DELETE FROM usuarios WHERE Id_Usuario = ?', [idUsuario]);

        if (result.affectedRows > 0) {
          return res.json({ mensaje: 'Usuario eliminado exitosamente' });
        } else {
          return res.status(404).json({ error: 'Usuario no encontrado' });
        }
      } catch (err) {
        console.error('Error al eliminar usuario:', err);
        return res.status(500).json({ error: 'Error al eliminar el usuario en la base de datos' });
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