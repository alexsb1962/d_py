import socket

PORT = 49001


def broadcast_socket() -> socket.socket:
    udp_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_sock.settimeout(2)
    return udp_sock


def send_broadcast(command: string = 'doors_empty', port: int = 1234):
    with broadcast_socket() as s:
        s.sendto(command.encode('utf-8'), ('255.255.255.255', port))


def get_response():
    with broadcast_socket() as s:
        mes = s.recvfrom(128)
    return None if len(mes) == 0 else mes


class NetIO:
    #  UDP broadcast связь

    def __init__(self, port: int = 1234):
        self._port_ = port


def press_button_command():
    # запуск прослушки ответов с очисткой
    # передача пустой команды
    # ожидание подтверждения
    # передача команды
    # ожидание подтверждения
    pass
