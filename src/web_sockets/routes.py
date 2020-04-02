from .resources import (
    notification_ws_get
)


def setup_socket_routes(app):
    app.router.add_route('GET', '/{code}', notification_ws_get)
