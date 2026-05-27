from js import Response as resp

async def on_fetch(request, env):
    return resp.new("testing")
  
