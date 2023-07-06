from wwwping.model import Node
from wwwping.wwwping import ma


class NodeSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Node

    id = ma.auto_field(dump_only=True)
    name = ma.auto_field()
    region = ma.auto_field()
    ipv4_address = ma.auto_field()
    ipv6_address = ma.auto_field()
    domain = ma.auto_field()
    port = ma.auto_field()
    create_at = ma.auto_field(dump_only=True)
    last_update_at = ma.auto_field(dump_only=True)
    status = ma.auto_field(dump_only=True)
