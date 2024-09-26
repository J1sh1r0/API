const express = require('express');
const  cors  = require ('cors'); 
const path = require('path');

const app = express();
app.use(cors());                //Middleware de Terceros

app.use(express.json());        //Middleware Incorporado en Express

app.get('/senFile',cors(),(req,res)=>{
    let archivo=path.join(__dirname, '/Imagenes/Lambo.jpg')
    res.sendFile(archivo);
})
app.get('/download',cors(),(req,res)=>{
    let archivo=path.join(__dirname, '/Imagenes/Lambo.jpg')
    res.download(archivo);
})
app.get('/attachment',cors(),(req,res)=>{ //Adjuntas el archivo de la respuesta
    let archivo=path.join(__dirname, '/Imagenes/Lambo.jpg')
    res.attachment(archivo);
    res.send()
})

//download y attachment hacen lo mismo

app.listen(3000,()=>{
    console.log('Server Express Escuchando en puerto 3000')
})