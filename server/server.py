from fastapi import FastAPI, WebSocket

app = FastAPI()

rooms = {}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    room = await websocket.receive_text()

    if room not in rooms:
        rooms[room] = []

    rooms[room].append(websocket)

    print("Client connecté au salon:", room)

    try:
        while True:
            data = await websocket.receive_text()

            for client in rooms[room]:
                await client.send_text(data)

    except:
        rooms[room].remove(websocket)
        print("Client déconnecté")