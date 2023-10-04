class MediaTypeVersioning:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        async def asgi(receive, send):
            accept_header = scope.get('headers', {}).get(b'accept', b'').decode('utf-8')
            version = None

            if 'application/vnd.api.' in accept_header:
                version = accept_header.split('application/vnd.api.')[1].split('+json')[0]

            original_path = scope["path"]
            new_path = scope["path"]

            if version == "1":
                new_path = f"/v1{original_path}"
            elif version == "2":
                new_path = f"/v2{original_path}"

            scope["path"] = new_path

            await self.app(scope, receive, send)

        return await asgi(receive, send)
