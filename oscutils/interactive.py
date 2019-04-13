"""
This module describes two console scripts for sending and receiving osc messages.
"""

from color import magenta
import pythonosc.udp_client
import pythonosc.dispatcher
import pythonosc.osc_server

DEFAULT_IP = 'localhost'
DEFAULT_PORT = 4242

# This function is used to get a pretty input with default value.
minput = lambda s, d: input(magenta('{} [{}] >'.format(s, d))) or d

# This function is used to display the tool's name.
print_title = lambda s: print('\n{}\n{}\n'.format(s,len(s)*'-'))

def client():
    """
    osc-client is a really simple interactive UDP client to send OSC messages.
    """
    print_title('osc-client')
    print('Please set the ip adress and the port of the server :')
    address = minput('adress', DEFAULT_IP)
    port = int(minput('port', DEFAULT_PORT))

    client = pythonosc.udp_client.SimpleUDPClient(address, port)

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
    print('Please set the ip adress and the port of the server :')
    address = minput('adress', DEFAULT_IP)
    port = int(minput('port', DEFAULT_PORT))

    def fun(*args):
        print('Receiving:', *args)

    class OSCDispatcher(pythonosc.dispatcher.Dispatcher):
        def __init__(self):
            super().__init__()
        def handlers_for_address(self, address_pattern):
            """yields Handler namedtuples matching the given OSC pattern."""
            yield pythonosc.dispatcher.Handler(fun, [])
            
    osc_server = pythonosc.osc_server.OSCUDPServer((address, port), OSCDispatcher())
    osc_server.serve_forever()
