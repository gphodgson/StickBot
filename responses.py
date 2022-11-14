from domain.router import Router

async def handle_response(content, msg, client) -> str:
    router = Router(content, msg, client)
    await router.Route()
    return router.getOutput()