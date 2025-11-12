from bobtail import BobTail, AbstractRoute, Request, Response
from bobtail_logger import BobtailLogger
from bobtail_cors import BobtailCORS
from bobtail_upload import BobtailUpload
from bobtail_jinja2 import BobtailJinja2
from volk import Volk


class StaticRoute:

    def get(self, req: Request, res: Response) -> None:
        res.set_static(req.path)


class Article:

    def get(self, req, res):
        res.set_headers({
            "Content-Type": "text/plain",
        })
        data = {}
        res.jinja2.render(res, "home.jinja2", data=data)


routes = [
    (StaticRoute(), "/static/*"),
    (Article(), "/")
]


app = BobTail(routes=routes)

app.use(BobtailLogger())
app.use(BobtailCORS())
app.use(BobtailUpload())
app.use(BobtailJinja2(template_dir="api"))


if __name__ == "__main__":
    volk = Volk(wsgi_application=app)
    volk.serve()
