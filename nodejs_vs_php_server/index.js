const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.get('/', (req, res) => {
  res.json({
    status: "success",
    first_name: "Quan",
    last_name: "Khuc"
  })
});

app.post('/', (req, res) => {
  const { first_name, last_name } = req.body;
  res.json({
    status: "success",
    first_name,
    last_name
  })
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
});