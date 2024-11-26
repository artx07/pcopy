# pcopy


**A lightweight Python server made with FastApi designed to seamlessly receive clipboard data from an iOS device using the native Shortcuts functionality.** 

## Copy or Share Text:

Copy any text you want to send to the server on your iPhone.
Alternatively, you can share the text directly to the Shortcut without opening it.

## Run the Shortcut:

Open the installed Shortcut and run it. The Shortcut retrieves the copied text from your clipboard.

##  Validation:

The Shortcut connects to your server and verifies it by comparing a server-provided key with a pre-configured key in the Shortcut.

##  Send the Clipboard:

After successful validation, the Shortcut securely sends the clipboard data to the server.

## Server Processing:

The server receives the clipboard data and displays it in the console for a few seconds.


## Features

Native iOS Shortcuts Integration: Utilizes iOS Shortcuts to send clipboard data without requiring third-party apps.

"Secure" communication: Includes a mechanism to validate the server before sending confidential data and auto-deletion of the received text.

Cross-Platform Compatibility: Works on macOS, Linux, and Windows systems.


## Installation
python3 -m venv venv  # Using a virtual environment  
source venv/bin/activate  
pip install fastapi uvicorn


## Set the secrets
#secret for pcopy  
export pcopy="123"  
export keylook="777"

## Run the server
uvicorn main:app --host 0.0.0.0 --port 8081

## On IOS

Download and install the shortcut, set the same secrets, and the server IP

## Notes 

Never expose the server to the internet. Ensure the server runs only on your local Wi-Fi network for security.
