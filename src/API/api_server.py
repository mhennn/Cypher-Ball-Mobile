import uvicorn

class APIServer:
    @staticmethod

    def run():
        uvicorn.run(
            "API.api_get_endpoint:app",
            host="127.0.0.1",
            port=8000
        )