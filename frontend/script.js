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