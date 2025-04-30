import argparse
import socket
import sys
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            sys.stdout.write(f"\r{message}\n")
            sys.stdout.write(f"<{username}> ")
            sys.stdout.flush()
        except ConnectionResetError:
            break

def start_client(ip, port, name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    client_socket.send(name.encode('utf-8'))
    
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    
    while True:
        message = input()
        if message.startswith('/'):
            if message == '/quit':
                client_socket.send(message.encode('utf-8'))
                client_socket.close()
                break
            elif message == '/list':
                client_socket.send(message.encode('utf-8'))
            elif message == '/help':
                print("Commands:")
                print("/quit - Exit the chat")
                print("/list - List all online users")
                print("/help - Show this help message")
            else:
                print("Unknown command. Type /help for a list of commands.")
        else:
            client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat Client")
    parser.add_argument("--ip", type=str, required=True, help="Server IP address")
    parser.add_argument("--port", type=int, required=True, help="Server port")
    parser.add_argument("--name", type=str, required=True, help="Your username")
    args = parser.parse_args()
    
    ip = args.ip
    port = args.port
    username = args.name
    
    start_client(ip, port, username)
