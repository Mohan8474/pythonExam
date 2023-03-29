from flask import Flask, render_template, request, jsonify

import json
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = os.urandom(32)
db = SQLAlchemy(app)
app.app_context().push()


class Invent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accessory = db.Column(db.Text, nullable=False)
    quantordered = db.Column(db.Integer, nullable=False)
    quantremaining = db.Column(db.Integer, nullable=False)
    vendorname = db.Column(db.Text, nullable=False)
    cpitem = db.Column(db.Integer)
    spitem = db.Column(db.Integer)

    def __repr__(self):
        return f"Todo   ( '{self.id}', '{self.accessory}','{self.quantordered}', '{self.quantremaining}'," \
               f" '{self.vendorname}', '{self.cpitem}', '{self.spitem}')"


@app.route("/", methods=['GET', 'POST'])
def home():
    inventory_list = Invent.query.all()
    return render_template("home.html", inventory_list=inventory_list)


@app.route("/getallitems", methods = ["GET"])
def items():
    inventory_list = Invent.query.all()
    return jsonify([{'id': t.id, 'accessory': t.accessory, 'quantordered': t.quantordered,"quantremaining": t.quantremaining,
                     "vendorname":t.vendorname,"cpitem": t.cpitem,"spitem": t.spitem} for t in inventory_list])



@app.route("/add", methods=["POST"])
def add():
    item_data = request.get_json()
    accessory = item_data["accessory"]
    quantordered = item_data["quantordered"]
    quantremaining = item_data["quantremaining"]
    vendorname = item_data["vendorname"]
    cpitem = item_data["cpitem"]
    spitem = item_data["spitem"]
    new_invent = Invent(accessory=accessory, quantordered=quantordered, quantremaining=quantremaining,
                        vendorname=vendorname, cpitem=cpitem, spitem=spitem)
    db.session.add(new_invent)
    db.session.commit()
    return jsonify({'message': 'Item Added successfully!'})

@app.route("/update/<int:invent_id>", methods=["PUT"])
def update(invent_id):
    item = Invent.query.get(invent_id)
    item_data = request.get_json()
    item.accessory = item_data["accessory"]
    item.quantordered = item_data["quantordered"]
    item.quantremaining = item_data["quantremaining"]
    item.vendorname = item_data["vendorname"]
    item.cpitem = item_data["cpitem"]
    item.spitem = item_data["spitem"]
    db.session.commit()
    return jsonify({'message': 'Item Updated successfully!'})

@app.route("/delete/<int:invent_id>")
def delete(invent_id):
    item = Invent.query.get(invent_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item Deleted successfully!'})

db.create_all()

