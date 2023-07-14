import asyncio
import os

import tornado.web
import tornado.ioloop
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, message_queue):
        self.message_queue = message_queue

    async def get(self):
        self.set_header('Content-Type', 'text/event-stream')
        self.set_header('Cache-Control', 'no-cache')
        self.set_header('Connection', 'keep-alive')

        try:
            while True:
                message = await self.message_queue.get()
                self.write(f'data: {message}\n\n')
                await self.flush()
        finally:
            await asyncio.sleep(10)
            self.finish()

def make_app():
    message_queue = asyncio.Queue()
    app = tornado.web.Application([
        ('/sse', MainHandler, {'message_queue': message_queue}),
        ('/(.*)$', tornado.web.StaticFileHandler, {"path": os.path.join(os.path.dirname(__file__), 'static'), "default_filename": "index.html"})
    ])
    return app, message_queue


async def read_file_content():
    file_path = '../puppyify/logs/output.log'
    with open(file_path, 'r') as f:
        content = f.read()
    return content


async def check_file_changes(message_queue):
    last_content = await read_file_content()

    while True:
        current_content = await read_file_content()
        if current_content != last_content:
            changed_content = current_content[len(last_content):]
            await message_queue.put(changed_content)
            last_content = current_content

        await asyncio.sleep(1)

async def main():
    app, message_queue = make_app()
    app.listen(port=8888, address='0.0.0.0')
    print('Listening at 0.0.0.0:8888')

    task = asyncio.create_task(check_file_changes(message_queue))

    try:
        await asyncio.sleep(10)
    finally:
        task.cancel()
        await task

if __name__ == '__main__':
    asyncio.run(main())
