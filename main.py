from fastapi import FastAPI, Request,HTTPException
import base64
import os, asyncio

app = FastAPI()

secret = os.getenv('pcopy')  #Secret for auth (key)

key = os.getenv('keylook')  #Secret for server validation (secret)


async def clearlog():
    
    await asyncio.sleep(30) #To clear the console, not too secure after 30 sec
 
    os.system('clear')



"""This endpoint is to be sure that we are connected to the correct server, 
 we receive back a key and our shortcuts will validate with our key.
"""
@app.get("/look")
async def process_json(request: Request):
    #print(secret)
    #print(key)
    client_token = request.headers.get("secret")
    if client_token != secret: #We sent the secret with GET in the shortcuts
        raise HTTPException(status_code=403, detail="Unauthorized: Invalid secret")
    
    """
    Sending the key to IOS to compare it, if the secret match then the shortcut will reach the clip endpoint
    """

    return  key   




"""This endpoint handle the clipboard , we have to send a secret
in the header in our shortcut, it will only be reached by our shortcut when it validates that the key is correct (/look endpoint), 
to be sure that we send it to our own server.    
"""

@app.post("/clip")  
async def process_json(request: Request):

    client_token = request.headers.get("secret")
    if client_token != secret: #We sent the secret with the post in the shortcuts
        raise HTTPException(status_code=403, detail="Unauthorized: Invalid secret")



    json_data = await request.json()
    

    text = json_data.get("text",None)
    decode = base64.b64decode(text).decode("utf-8") #Decode from base64
    

    print(f"From IOS: {decode}")



    
    asyncio.create_task(clearlog())
  
    
    return {
        #"message": f"Received text: {text}"
    }