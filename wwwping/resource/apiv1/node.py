from flask_restful import Resource

from wwwping.controller.apiv1 import NodeController


class NodeResource(Resource):
    def get(self, node_id=None):
        """
        GET /api/v1/nodes           --> Get all nodes.
        GET /api/v1/node/<node_id>  --> Get a node.
        """
        if node_id is None:
            return NodeController.get_nodes()
        else:
            return NodeController.get_node(node_id)

    def post(self):
        """
        POST /api/v1/nodes           --> Create a node.
        POST /api/v1/node/<node_id>  --> Not allowed.
        """
        return NodeController.create_node()

    def patch(self, node_id):
        """
        PATCH /api/v1/nodes           --> Not allowed.
        PATCH /api/v1/node/<node_id>  --> Update a node.
        """
        return NodeController.update_node(node_id)

    def delete(self, node_id):
        """
        DELETE /api/v1/nodes           --> Not allowed.
        DELETE /api/v1/node/<node_id>  --> Delete a node.
        """
        return NodeController.delete_node(node_id)
