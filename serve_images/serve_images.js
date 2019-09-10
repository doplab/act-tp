const express = require('express');
const app = new express();

const port = 3010;

app.get('/images/:img', (req, res) => res.sendFile(`${__dirname}/images/${req.params.img}`));

app.listen(port, () => console.log(`Running on port ${port}!`));
