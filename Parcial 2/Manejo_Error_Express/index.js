const express = require('express');
const app = express();

const  cors  = require ('cors'); 
app.use(cors());


app.get('/',(req,res)=>{
    if(tru){
        res.json({message:'Server Express contestando a peticion get'})
    }
    else{
        res.json({message:'Server Express contestando a peticion get'})
            next(err);
    }
})

app.use((err,req,res,next)=>{
    console.log(err);
    res.status(501);
    res.json({error:err.message});
});

app.listen(3000,()=>{
    console.log('Server Express Escuchando en el Puerto 3000')
})