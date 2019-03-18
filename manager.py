#!/bin/env python3
import requests
from enum import Enum
from argparse import ArgumentParser

# Keys documented here: http://support.yealink.com/faq/faqInfo?id=173
# Not all keys are implemented and not all implementations can be given as arguments.

class Keys(Enum):
    OK = "OK"
    Speaker = "SPEAKER"
    Mute = "MUTE"
    Hold = "F_HOLD"
    Cancel = "X"
    DNDOn = "DNDOn"
    DNDOff = "DNDOff"
    Up = "UP"
    Down = "DOWN"
    Left = "LEFT"
    Right = "RIGHT"
    Pound = "POUND"
    Reboot = "Reboot"

ARGS = None
BASE_URL = "http://{0}/cgi-bin/ConfigManApp.com"


def make_request(params):
    return requests.get(BASE_URL.format(ARGS.host), auth=(ARGS.user, ARGS.pwd), params=params)


def press_key(key):
    return make_request({"key": key.value})


def call(number):
    print("Dialing %s" % number)
    return make_request({
        "number": number,
        "outgoing_uri": 'URI'
    })


def main(parser):
    global ARGS
    ARGS = parser.parse_args()

    # user can put phone to speaker regardless of other options
    if ARGS.speaker:
        press_key(Keys.Speaker)

    if ARGS.dial:
        call(ARGS.dial)
    elif ARGS.answer:
        print("Answering call")
        press_key(Keys.OK)
    elif ARGS.hangup:
        print("Hanging up call")
        press_key(Keys.Cancel)
    elif ARGS.mute:
        print("Mute/unmute call")
        press_key(Keys.Mute)
    elif ARGS.hold:
        print("Hold/unhold call")
        press_key(Keys.Hold)
    elif ARGS.key:
        print("Sending key: %s" % ARGS.key)
        press_key(ARGS.key)
    elif ARGS.reboot:
        print("Rebooting phone...")
        press_key(Keys.Reboot)
    else:
        print("Please tell me what to do.")
        parser.print_usage()


if __name__ == "__main__":
    parser = ArgumentParser(
        description='Make and answer calls using the Remote Management feature on Yealink phones.')
    parser.add_argument('--host', '-H', dest='host', required=True,
                        help='The IP adress or hostname of your Yealink phone.')
    parser.add_argument('--user', '-U', dest='user',
                        required=True, help='An administrative user.')
    parser.add_argument('--password', '-P', dest='pwd',
                        required=True, help='Password of the admin user.')
    parser.add_argument('--dial', '-d', dest='dial',
                        help='Phone number to dial.')
    parser.add_argument('--answer', '-a', dest='answer',
                        action='store_true', help='Answer an incoming call.')
    parser.add_argument('--mute', '-m', dest='mute',
                        action='store_true', help='Mute/unmute ongoing call.')
    parser.add_argument('--hangup', '-hp', dest='hangup',
                        action='store_true', help='Hang up ongoing call.')
    parser.add_argument('--hold', '-hd', dest='hold',
                        action='store_true', help='Hold ongoing call.')
    parser.add_argument('--speaker', '-sp', dest='speaker',
                        action='store_true', help='Toggle loudspeaker.')
    parser.add_argument('--reboot', '-rb', dest='reboot',
                        action='store_true', help='Reboot phone.')
    parser.add_argument('--key', '-K', dest='key', help='Send arbitrary key.')
    main(parser)
