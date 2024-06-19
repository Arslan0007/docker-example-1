// var cors = require('cors')
// var app = express()
// const cors = require('cors')
// app.use(cors())

// const fetchPromise = fetch("http://localhost:8000/'");
        
//         fetchPromise
//             .then((response) => response.json())
//             .then((data) => {
//                 console.log(data);
//             });
        // const express = require('express');
        // const app = express();

        // app.get("http://localhost:8000/", function (req, res) {
        //     res.send("Hello world");
        // });
const express = require('express');
const cors = require('cors');
const app = express();

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