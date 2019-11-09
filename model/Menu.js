const mongoose = require("mongoose");
const Schema = mongoose.Schema;

let Menu = new Schema(
  {
    Menu: {
      type: String
    },
    RestaurantID: {
      type: String
    },
    UserID: {
      type: String
    },
    Attribute: [{ item: String }, { item: String }]
  },
  {
    collection: "Menu"
  }
);

module.exports = mongoose.model("Menu", Menu);
