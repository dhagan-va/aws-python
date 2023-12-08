import sys
import signal
import json
import business


def signal_handler(sig, frame):
    print('Exiting.')
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    with open("event-sample.json", "r") as f:
        event = json.loads(f.read())

    print(business.run(event))
