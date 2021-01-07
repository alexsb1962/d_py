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
    # запуск прослушки запросов
    with broadcast_socket() as s:
        s.settimeout(0.5)
        # очистка
        while True:
            try:
                (data, addr) = s.recvfrom(128)
                print('Принято.....')
                print(data.__str__)
                print(addr)
                if sdata == 'doors_on':
                    # подтверждение приема команды
                    s.sendto('doors_on', addr)
                    print('Включил кнопку')
                    time.sleep(0.3)
                    print('выключил кнопку')
                    # подтверхдение выполнения команды
                    s.sendto('doors-ok', addr)
            except socket.timeout as msg:
                print('timeout')
                pass
        # передача пустой
        n = 0
        while True:
            for i in range(100):
                n = s.sendto('door_empty'.encode('utf-8'), ('192.168.1.255', port))
                #time.sleep(0.002)
            print('Очередных 100 пакетов.....')
            time.sleep(0.5)

        return True


def button_press(event):
    press_button_command(PORT)


if __name__ == '__main__':
    button_press(1)




