const express = require('express');
const cors = require('cors');
const multer = require('multer');
const mysql = require('mysql2/promise');  // Importar la versión promise para usar async/await
const bodyParser = require('body-parser');
require('body-parser-xml')(bodyParser);

const app = express();
const upload = multer();

// Función para crear la conexión
async function createConnection() {
  return await mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',  // Coloca tu contraseña aquí si es necesario
    database: 'biblioteca',  // Cambia el nombre de la base de datos si es necesario
  });
}

let connection;

// Inicia la conexión y maneja posibles errores
async function startServer() {
  try {
    connection = await createConnection();
    console.log('Conexión a la base de datos establecida');

    // Aquí se configura el servidor
    app.use(cors());                                // Middleware de terceros
    app.use(express.json());                        // Middleware incorporado en Express
    app.use(express.text());                        // Middleware para texto
    app.use(express.urlencoded({ extended: true })); // Middleware para parsear un formulario URL en Code
    app.use(upload.none());                         // Middleware para parsear form-data
    app.use(bodyParser.xml());                      // Parseador de XML

    // Ruta para obtener el usuario por Id_Usuario
    app.get('/usuario', async (req, res) => {
      const idUsuario = req.query.Id_Usuario;  // Obtiene el parámetro de la URL

      if (!idUsuario) {
        return res.status(400).json({ error: 'Id_Usuario es requerido' });
      }

      try {
        const [results, fields] = await connection.execute(
          'SELECT * FROM usuarios WHERE Id_Usuario = ?',
          [idUsuario]  // Parámetro de la consulta
        );

        if (results.length > 0) {
          return res.json(results[0]);  // Devuelve solo el primer resultado
        } else {
          return res.status(404).json({ error: 'Usuario no encontrado' });
        }
      } catch (err) {
        console.error('Error en la consulta:', err);
        return res.status(500).json({ error: 'Error interno del servidor' });
      }
    });

    app.listen(3000, () => {
      console.log('Server Express escuchando en puerto 3000');
    });

  } catch (error) {
    console.error('Error al conectar a la base de datos:', error);
  }
}

startServer();
