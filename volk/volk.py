from volk.utils.logging import log


class Volk:

    server_running = False

    def __init__(self):
        pass

    def serve(self):
        self.server_running = True
        while self.server_running:
            log.info("Running server on http://localhost:8888")
            self.server_running = False
