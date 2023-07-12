import asyncio
import os
from os.path import join, dirname

from tornado.web import RequestHandler, StaticFileHandler, Application
import R, C


class BaseHandler(RequestHandler):

    def set_default_headers(self) -> None:
        origin_url = self.request.headers.get('Origin')
        if not origin_url: origin_url = '*'
        self.set_header('Access-Control-Allow-Methods', 'POST, PUT, DELETE, GET, OPTIONS')
        self.set_header('Puppyify', '0.1.0')
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Origin', origin_url)
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with,token,Content-type')

    def options(self):
        self.set_status(200)
        self.finish()

    def json(self, r: R):
        self.set_header('Content-Type', 'application/json;charset=UTF-8')
        self.write(r.json())


class BaseAuthHandler(BaseHandler):

    def prepare(self):
        self.check_token()

    def token(self):
        t = self.request.headers['token'] if 'token' in self.request.headers else None
        if not t:
            t = self.get_argument('token', None)
        if not t:
            t = self.get_body_argument('token', None)
        return t

    def check_token(self):
        t = self.token()
        if not t:
            self.json(R.expire('not token'))
            return self.finish()
        if not C.check_token(t):
            self.json(R.expire())
            return self.finish()


class MainHandler(BaseAuthHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return Application([
        ('/', MainHandler),
        (r'/(.*)$', StaticFileHandler, {"path": join(dirname(__file__), 'static'), "default_filename": "index.html"})
    ])


async def main():
    if __name__ == "__main__":
        banner = '''
.______    __    __  .______   .______   ____    ____  __   ___________    ____ 
|   _  \  |  |  |  | |   _  \  |   _  \  \   \  /   / |  | |   ____\   \  /   / 
|  |_)  | |  |  |  | |  |_)  | |  |_)  |  \   \/   /  |  | |  |__   \   \/   /  
|   ___/  |  |  |  | |   ___/  |   ___/    \_    _/   |  | |   __|   \_    _/   
|  |      |  `--'  | |  |      |  |          |  |     |  | |  |        |  |     
| _|       \______/  | _|      | _|          |__|     |__| |__|        |__|     
                                                                                                          
                                                         puppyify(v0.1.0)     
                                                         https://puppyify.cn/doc/   
                                                                                    '''
    uri = os.environ.get('PUPPYIFY_URI', f'http://127.0.0.1:8888/')
    print(banner)
    app = make_app()
    app.listen(port=8888, address='0.0.0.0')
    print('Listening at ', uri)
    C.init()

    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
