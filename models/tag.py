from db import db

class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)#unique=True aynı tagda iki obje olamaz demek
    store_id = db.Column(db.String(), db.ForeignKey("stores.id"), nullable=False)#Store_id farklıysa iki aynı isimli tag olabilir
    
    store = db.relationship("StoreModel", back_populates="tags")
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")