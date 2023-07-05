from wwwping.wwwping import apiv1 as api

from .node import NodeResource

api.add_resource(NodeResource, "/nodes", methods=["GET", "POST"], endpoint="nodes")

api.add_resource(
    NodeResource, "/node/<node_id>", methods=["GET", "PATCH", "DELETE"], endpoint="node"
)
