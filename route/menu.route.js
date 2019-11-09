// menu.route.js
const express = require("express");
const menuRoutes = express.Router();

// Require Menu model in our routes module
let Menu = require("../model/Menu");

// Defined store route
menuRoutes.route("/add").post(function(req, res) {
  console.log(req.body);
  let menu = new Menu(req.body);
  menu
    .save()
    .then(menu => {
      res.status(200).json({ Menu: "Menu has been added successfully" });
    })
    .catch(err => {
      res.status(400).send("Unable to save to database");
    });
});

// Defined get data(index or listing) route
menuRoutes.route("/").get(function(req, res) {
  Menu.find(function(err, menus) {
    if (err) {
      console.log(err);
    } else {
      res.json(menus);
    }
  });
});

// Defined edit route
menuRoutes.route("/edit/:id").get(function(req, res) {
  let id = req.params.id;
  Menu.findById(id, function(err, menu) {
    res.json(menu);
  });
});

//  Defined update route
menuRoutes.route("/update/:id").post(function(req, res) {
  Menu.updateOne(req.params.id, function(err, menu) {
    if (!menu) res.status(404).send("Record not found");
    else {
      menu.Menu = req.body.Menu;
      menu.RestaurantID = req.body.RestaurantID;
      menu.UserID = req.body.UserID;

      menu
        .save()
        .then(menu => {
          res.json("Update complete");
        })
        .catch(err => {
          res.status(400).send("Unable to update the database");
        });
    }
  });
});

// Defined delete | remove | destroy route
menuRoutes.route("/delete/:id").get(function(req, res) {
  Menu.deleteOne({ _id: req.params.id }, function(err, menu) {
    if (err) res.json(err);
    else {
      res.json("Successfully removed");
    }
  });
});

menuRoutes.route("/deleteAll").get(function(req, res) {
  Menu.deleteMany({}, function(err, obj) {
    if (err) res.json(err);
    else {
      res.json("Successfully removed");
    }
  });
});

module.exports = menuRoutes;
