const port = 3000
const express = require('express')
const swaggerUI     = require('swagger-ui-express'); 
const swaggerJsDoc  = require('swagger-jsdoc'); 

const app = express()


app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Servidor expres escuchando en el puerto: ${port}`)
})