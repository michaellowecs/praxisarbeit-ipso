from app import db


class Tenants(db.Model):
    """Tenants table"""

    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key=True)
    object_id = db.Column(db.Integer)
    object_name = db.Column(db.String)
    object_address = db.Column(db.String)
    tenant_name = db.Column(db.String)
    apartment_number = db.Column(db.String)
    rent_start = db.Column(db.String)
    rent_end = db.Column(db.String)
    rent_price = db.Column(db.Numeric)
