import asyncio
import os

import tornado


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
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
    uri = os.environ.get('POSTER_URI_PREFIX', f'http://127.0.0.1:8888/')
    print(banner)
    app = make_app()
    app.listen(port=8888, address='0.0.0.0')
    print('Listening at ', uri)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
