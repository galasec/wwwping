from wwwping.util import now, uuidgen
from wwwping.wwwping import db


class Node(db.Model):
    __tablename__ = "nodes"
    id = db.Column(db.String(32), primary_key=True, nullable=False, default=uuidgen)
    name = db.Column(db.String(32), index=True, nullable=False)
    region = db.Column(db.String(32), index=True, nullable=False)
    ipv4_address = db.Column(db.String(16), nullable=False)
    ipv6_address = db.Column(db.String(40), nullable=True)
    domain = db.Column(db.String(255), nullable=True)
    port = db.Column(db.String(5), nullable=False, default="80")
    created_at = db.Column(db.DateTime, nullable=False, default=now)
    last_update_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return f"<Node id='{self.id}' name='{self.name}'>"
