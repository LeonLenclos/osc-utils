# osc-utils

Simple command line tools written in Python usefull for debuging OSC ([Open Sound Control](http://opensoundcontrol.org)) applications.

Two interactive console scripts for sending and receiving OSC messages : `osc-client` for sending and `osc-server` for receiving.

## Usage

Install osc-utils :

    pip install git+https://github.com/LeonLenclos/osc-utils.git@master

Run the interactive osc-server :

    osc-server

Run the interactive osc-client :

    osc-client

Uninstall :

    pip uninstall osc-utils


### osc-server

`osc-server` will let you choose an IP address and a port where to listen for OSC messages. You can leave blank to choose default values.

Once you choosed the adress and port, it will print every OSC messages sent to it.

### osc-client

`osc-client` will let you choose an IP address and a port where to send OSC messages. You can leave blank to choose default values.

Then you will be prompted for the path and the values of the message. If you don't want to add a value to the message, leave blank. If you want to add one ore more values, hit enter after entering each value and leave blank when finished.

The message will be sent to the server address and you will be prompted for a new message. Default value for the path will be the last path you entered.

### address as arguments

You can also call osc-client and osc-server with a `--ip-address` and/or a `--port` argument. In this way, you won't be asked for them later.