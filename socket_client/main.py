import socket
import time
import tkinter as tk

PORT = 54545


def broadcast_socket() -> socket.socket:
    udp_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_sock.settimeout(0.1)
    return udp_sock


def press_button_command(port:int):
    # запуск прослушки ответов с очисткой
    with broadcast_socket() as s:
        s.settimeout(0.5)
        # очистка
        while True:
            try:
                data = s.recv(128)
            except socket.timeout as msg:
                break
                main_win

        n = 0
        while True:
            try:
                for i in range(2):
                    n = s.sendto('door_empty'.encode('utf-8'), ('192.168.1.255', port))
                print('Очередных 2 пакета.....')
            except socket.???
                # TODO restart
                pass
            # принять все ответы
            while True:
                try:
                    data = s.recv(128)
                    print("Принято ", data)
                except socket.timeout as msg:
                    break

            time.sleep(1)

        return True


def button_press(event):
    press_button_command(PORT)


if __name__ == '__main__':
    button_press(1)


