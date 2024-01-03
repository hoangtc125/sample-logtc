# Logging with FastAPI (Python)

## Features

- File timer rotation handler (Always)

- Socket handler (On/Off)

## Architecture

FastAPI server implement both socket server and socket client to transfer log from client to self server. Use socket server can serve any monitor outside.

With micro-services, use socket server can work smoothly: who want to get log, just create socket client and connect to particular service, rather than use socket client which logs directly to dashboard: have to control socket connection

Monitor outside can use their socket client to connect to this socket server with source "dashboard" to get log realtime

Singleton pattern for socket and logger in whole project