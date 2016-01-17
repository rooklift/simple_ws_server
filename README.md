# Simple Websocket Server Example

I was trying to implement a simple websocket server using [SimpleWebSocketServer](https://github.com/dpallot/simple-websocket-server) but was having trouble. I finally found a blocking select() call in the library, and saw that I could specify a timeout for it in the initial call to the library. So this simple program is now a working example.

SimpleWebSocketServer is by Dave P. (dpallot) and licensed under the MIT license.

This example (test_server.py) is public domain.
