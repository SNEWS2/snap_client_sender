# snews_snap_client_sender
A setup for application sending observations to SNEWS

## Installation
Checkout this package:
```shell
git clone 
```

Install the requirements:
```shell
pip install -r requirements.txt
``` 

## Running the examples

In `config.yml` file two nodes are defined (each of them is a separate application).

### Client sender application

Run the default node (named `node`):
```shell
snap_run config.yml 
```
to start the application that

1. Sends `SNEWSHeartbeatMessage` every 10 seconds
2. Reads alerts from the file "alerts.txt" and sends the `SNEWSCoincidenceTierMessage` whenever a new line with timestamp appears

You should see the output of each message being sent.

### Fake alarms generation

Run the `generate_alerts` node:

```shell
snap_run config.yml generate_alerts
```

to start the process which adds a line to `alerts.txt` file every 120 seconds.
You should see the counter of generated alerts
