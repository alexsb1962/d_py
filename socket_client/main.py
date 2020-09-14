import socket
import tkinter as tk

PORT = 49001


def broadcast_socket() -> socket.socket:
    udp_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_sock.settimeout(0.1)
    return udp_sock


def press_button_command(main_win, port:int):
    # запуск прослушки ответов с очисткой
    with broadcast_socket() as s:
        s.settimeout(0.1)
        # очистка
        while True:
            try:
                data = s.recv(128)
            except socket.timeout as msg:
                break
                main_win
        # передача пустой
        while True:
            s.sendto('door_empty'.encode('utf-8'), ('255.255.255.255', port))
            sleep(0.5)
        return True


def button_press(event):
    press_button_command(main_win, PORT)



if __name__ == '__main__':
    main()


