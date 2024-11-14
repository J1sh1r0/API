const express = require('express');
const app = express();

const  cors  = require ('cors'); 
app.use(cors());                //Middleware de Terceros

app.get('/',cors(),(req,res)=>{
    res.json({mensaje: 'Server Express contestando a peticion get'})
})

app.listen(3002,()=>{
    console.log('Server Express Escuchando en puerto 3000')
})


