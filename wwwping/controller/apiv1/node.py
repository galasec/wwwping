from wwwping.util import jsonify


class NodeController:
    def get_nodes():
        return jsonify(status=501, code=100)

    def get_node(node_id):
        return jsonify(status=501, code=100)

    def create_node():
        return jsonify(status=501, code=100)

    def update_node(node_id):
        return jsonify(status=501, code=100)

    def delete_node(node_id):
        return jsonify(status=501, code=100)
