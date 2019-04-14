"""
This module describes two console scripts for sending and receiving osc messages.
"""

import argparse

from color import magenta
import pythonosc.udp_client
import pythonosc.dispatcher
import pythonosc.osc_server

DEFAULT_IP = 'localhost'
DEFAULT_PORT = 4242

parser = argparse.ArgumentParser()
parser.add_argument('--ip-address', '-a', type=str, help='IP address of the OSC server.')
parser.add_argument('--port', '-p', type=int, help='UDP port of the OSC server.')

# This function is used to get a pretty input with default value.
minput = lambda s, d: input(magenta('{} [{}] >'.format(s, d))) or d

# This function is used to display the tool's name.
print_title = lambda s: print('\n{}\n{}\n'.format(s,len(s)*'-'))

def _get_server_address():
    """
    Return the server address and port in a tuple.
    Check if they was passed as arguments, or prompt for them.
    """
    args = parser.parse_args()
    return (
        args.ip_address or minput('server adress', DEFAULT_IP),
        args.port or int(minput('ssrver port', DEFAULT_PORT))
    )

def client():
    """
    osc-client is a really simple interactive UDP client to send OSC messages.
    """ 
    print_title('osc-client')


    client = pythonosc.udp_client.SimpleUDPClient(*_get_server_address())

    print('Let\'s send messages !')

    path = ''
    value = []

    while 1:
        print('Enter the path and the value of the requests.')
        path = minput('path', path)
        while 1:
            v = input(magenta('value [leave blank to send] >'))
            if v:
                value.append(v)
            else:
                break
        print('Sending: {} {} to {}:{}'.format(path, value, address, port))
        client.send_message(path, value)


def server():
    """
    osc-server is a really simple interactive UDP server to receive OSC messages.
    """
    print_title('osc-server')

    def fun(*args):
        print('Receiving:', *args)

    class OSCDispatcher(pythonosc.dispatcher.Dispatcher):
        def __init__(self):
            super().__init__()
        def handlers_for_address(self, address_pattern):
            """yields Handler namedtuples matching the given OSC pattern."""
            yield pythonosc.dispatcher.Handler(fun, [])
    
    server_address = _get_server_address()
    osc_server = pythonosc.osc_server.OSCUDPServer(
        server_address,
        OSCDispatcher()
    )
    print('Serving at osc://{}:{}'.format(*server_address))
    osc_server.serve_forever()


