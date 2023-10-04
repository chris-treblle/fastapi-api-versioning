class QueryParameterVersioning:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        async def asgi(receive, send):
            api_version = scope.get('query_string').decode('utf-8')
            api_version = api_version.split("=")[1] if "api_version=" in api_version else None

            original_path = scope["path"]
            new_path = scope["path"]

            if api_version == "1":
                new_path = f"/v1{original_path}"
            elif api_version == "2":
                new_path = f"/v2{original_path}"

            scope["path"] = new_path

            await self.app(scope, receive, send)

        return await asgi(receive, send)
