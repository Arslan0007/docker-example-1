const express = require('express');
const app = express();
const router = express.Router();
const cors = require('cors')

app.use(cors())

const path = __dirname + '/views/';
const port = 80;

router.use(function (req,res,next) {
  console.log('/' + req.method);
  next();
});

router.get('/', function(req,res){
  res.sendFile(path + 'index.html');
});

app.use(express.static(path));
app.use('/', router);

app.listen(port, function () {
  console.log('Example app listening on port 80!')
})


const whitelist = ['http://localhost:80'];

const corsOptions = {
    origin: function (origin, callback) {
        if (whitelist.indexOf(origin) !== -1) {
            callback(null,true)
        } else {
            callback(new Error('Not allowed by CORS'))
        }
    }
}

app.use(cors(corsOptions));

app.get('https://api.coindesk.com/v1/bpi/currentprice.json', (req, res) => {

});


app.listen(8000, () => {
    console.log('Server running on port 8000');
});