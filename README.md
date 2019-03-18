# yealink-remote-manager
This is a script that uses the Remote Management interface in Yealink phones to make, answer, hold, mute and hang up calls.
Furthermore it supports other neat tricks such as sending arbitrary "keypresses" to your phone and remotely rebooting it. 

Please refer to the [Usage](#Usage) section below for a full list of features.


## Motivation

This script was written because I didn't want to type phone numbers in the phone keyboard like people used to a decade ago.

Moreover this gives one the ability to copy and paste numbers, which saves a ton of time and frustration. Answering calls is probably faster through the actual phone itself, though.


## Dependencies

*This program was written for python3. You are welcome to rewrite it for python2 and make a PR.*

The only dependency is `requests`. You can install it using pip:
```bash
python3 -m pip install requests
```

In addition to that, your phone must support Remote Management. Refer to [this article](http://support.yealink.com/faq/faqInfo?id=565) to find out how to configure it.

Also be aware that this has only been tested on a Yealink T28P, but it ought to work on a wide range of Yealink devices, particularily because the [documentation](http://support.yealink.com/faq/faqInfo?id=173) of the keys didn't even list my device as "supported", but everything seems to work alright.


## Usage
```
usage: manager.py [-h] --host HOST --user USER --password PWD [--dial DIAL]
                  [--answer] [--mute] [--hangup] [--hold] [--speaker]
                  [--reboot] [--key KEY]

Make and answer calls using the Remote Management feature on Yealink phones.

optional arguments:
  -h, --help            show this help message and exit
  --host HOST, -H HOST  The IP adress or hostname of your Yealink phone.
  --user USER, -U USER  An administrative user.
  --password PWD, -P PWD
                        Password of the admin user.
  --dial DIAL, -d DIAL  Phone number to dial.
  --answer, -a          Answer an incoming call.
  --mute, -m            Mute/unmute ongoing call.
  --hangup, -hp         Hang up ongoing call.
  --hold, -hd           Hold ongoing call.
  --speaker, -sp        Toggle loudspeaker.
  --reboot, -rb         Reboot phone.
  --key KEY, -K KEY     Send arbitrary key.
```

## Examples

### Dial 1234 and put phone on speaker
```bash
python3 manager.py -H '10.0.0.4' -U admin -P hunter2 --dial 1234 --speaker
```

### Accept call
```bash
python3 manager.py -H '10.0.0.4' -U admin -P hunter2 --answer
```

### Reboot phone
```bash
python3 manager.py -H '10.0.0.4' -U admin -P hunter2 --reboot
```

## Contribution

If you manage to extend the feature set of this script, I'd really appreciate a PR.


## Licensing

This program is licensed under the GPL 2.0 license. For more information, please refer to `LICENSE`.
