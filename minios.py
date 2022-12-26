import cmd
import ctypes

# Função para criar um novo arquivo
def create_file(filename):
  open(filename, "w").close()

# Função para ler o conteúdo de um arquivo
def read_file(filename):
  with open(filename, "r") as f:
    data = f.read()
  return data

# Função para escrever em um arquivo
def write_file(filename, data):
  with open(filename, "w") as f:
    f.write(data)

# Função para executar a tarefa 1
def task1():
  print("Executing task 1")

# Função para executar a tarefa 2
def task2():
  print("Executing task 2")

# Função para executar uma tarefa qualquer
def execute_task(task):
  if task == "task1":
    task1()
  elif task == "task2":
    task2()

# Função para criar um socket
def create_socket():
  sock = ctypes.CDLL("libc.so.6").socket(AF_INET, SOCK_STREAM, 0)
  return sock

# Função para ligar um socket a um endereço na rede
def bind_socket(sock, address, port):
  ctypes.CDLL("libc.so.6").bind(sock, address, port)

# Função para escutar conexões entrantes
def listen_socket(sock, backlog):
  ctypes.CDLL("libc.so.6").listen(sock, backlog)

# Função para aceitar uma conexão
def accept_socket(sock):
  conn, address = ctypes.CDLL("libc.so.6").accept(sock)
  return conn, address

class MiniOSCommandLine(cmd.Cmd):
  intro = "Welcome to the MiniOS command line interface. Type help or ? to list commands.\n"
  prompt = "minios> "

  def do_create_file(self, filename):
    "Create a new file"
    create_file(filename)

  def do_read_file(self, filename):
    "Read the contents of a file"
    data = read_file(filename)
    print(data)

  def do_write_file(self, line):
    "Write to a file"
    args = line.split()
    filename = args[0]
    data = " ".join(args[1:])
    write_file(filename, data)

  def do_execute_task(self, task):
    "Execute a task"
    execute_task(task)

  def do_create_socket(self):
    "Create a new socket"
    sock = create_socket()
    print(f"Socket created with file descriptor {sock}")

  def do_bind_socket(self, line):
    "Bind a socket to an address and port"
    args = line.split()
    sock = int(args[0])
    address = args[1]
    port = int(args[2])
    bind_socket(sock, address, port)

  def do_listen_socket(self, line):
    "Listen for incoming connections"
    sock = int(line)
    listen_socket(sock, 5)

  def do_accept_socket(self, line):
    "Accept an incoming connection"
    sock = int(line)
    conn, address = accept_socket(sock)
    print(f"Connection accepted from {address}")

if __name__ == "__main__":
  MiniOSCommandLine().cmdloop()
