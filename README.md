# pyload

Very basic and entirely impractical payload for remote code execution in the same vein as meterpreter.

For the payload to work, the attacking PC must set up the listener for the reverse shell by running server.py, whilst the target must run client.py. 
The client will attempt to connect to the attacker's server every 20 seconds until it is successful or the client process is ended (e.g. via task manager or restarting the computer).

Once connected, the attacker will have access to a terminal which runs commands natively on the target's PC.

Besides all the basic commands available on the target PC (`cd`, `ls`, `dir`, `ip addr show`, `netstat` etc.), the remote shell also supports commands to download and upload files bidirectionally. Type `quit` to exit the shell and shut down the process on the target PC.

The payload should work regardless of attacker or host operating system, so long as each one has python installed.

You may wish to package `client.py` into an executable file format with a tool such as pyinstaller (for windows) to reduce the number of clicks a target needs to run the payload.

Ideas for future expansion:
* More meterpreter-style commands, like `screenshot` or `getsystem`
* Enter attacker IP address during runtime
* Help menu
* General robustness
