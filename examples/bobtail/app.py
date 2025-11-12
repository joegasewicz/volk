from bobtail import BobTail, AbstractRoute, Request, Response
from volk import Volk, WSGIApplication

class Article:

    def get(self, req, res):
        res.set_body([
            {"id": 1},
            {"id": 2},
        ])

routes = [
    (Article(), "/articles")
]


app = BobTail(routes=routes)

if __name__ == "__main__":
    volk = Volk(wsgi_application=app)
    volk.serve()
