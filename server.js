// Dependencies
const express = require("express"),
  path = require("path"),
  bodyParser = require("body-parser"),
  cors = require("cors"),
  mongoose = require("mongoose"),
  config = require("./config/DB");

// routes.js
const menuRoute = require("./route/menu.route");

// Mongoose
mongoose.connect(config.DB, {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// On error & connected database
var db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", function() {
  console.log("we're connected!");
});

const app = express();

//Body Parser Middleware
app.use(bodyParser.json());

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

// CORS Middleware
app.use(cors());

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  if (req.method === "OPTION") {
    res.header("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,PATCH");
    return res.status(200).json({});
  }
  next();
});

app.use("/menu", menuRoute);

app.get("/", (req, res, next) => {
  res.send("Backend home");
});

// Port Number
let port = process.env.PORT || 4000;

// Start Server
const server = app.listen(port, function() {
  console.log("Listening on port " + port + " 🚀");
});
