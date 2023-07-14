import asyncio
import os

import tornado.web
import tornado.ioloop
import tornado.httpserver

class LogHandler(tornado.web.RequestHandler):
    clients = set()

    def initialize(self):
        self.set_header('Content-Type', 'text/event-stream')
        self.set_header('Cache-Control', 'no-cache')
        self.set_header('Connection', 'keep-alive')

    def get(self):
        self.clients.add(self)
        self.write('data: Connected\n\n')
        self.flush()

    def on_connection_close(self):
        self.clients.remove(self)

    @classmethod
    def send_message(cls, message):
        for client in cls.clients:
            client.write(f'data: {message}\n\n')
            client.flush()

def make_app():
    app = tornado.web.Application([
        (r'/sse', LogHandler),
        ('/(.*)$', tornado.web.StaticFileHandler,
         {"path": os.path.join(os.path.dirname(__file__), 'static'), "default_filename": "index.html"})
    ])
    return app

async def simulate_logs():
    while True:
        log_message = "This is a log message"
        LogHandler.send_message(log_message)
        await asyncio.sleep(1)

async def main():
    app = make_app()
    app.listen(port=8888, address='0.0.0.0')
    print('Listening at 0.0.0.0:8888')

    # 启动模拟日志生成的任务
    task = asyncio.create_task(simulate_logs())
    await task

if __name__ == '__main__':
    asyncio.run(main())
