![logo](https://user-images.githubusercontent.com/91157484/147389754-00c8e58f-f0e5-4b59-bf41-eac93a678282.png)
### version 1.0.0
# Discord Message Splitter (<img src="https://user-images.githubusercontent.com/91157484/147390100-f71e95f9-11f8-4497-82b2-725995de00b7.png" data-canonical-src="https://user-images.githubusercontent.com/91157484/147390100-f71e95f9-11f8-4497-82b2-725995de00b7.png" width="27" height="27" /> library)
One algorithm Python library, free for anyone to grab and use without any credit or permission.
Used by Python Discord bots to smartly split long messages into smaller ones in order to cope with the 2000 character per message limit.
Longer messages can also be sent by bots with Discord Nitro subscribed, thus please remember to help Discord grow when writting a bigger project.

![sending](https://user-images.githubusercontent.com/91157484/147390060-1b9eeaaf-93f4-4c18-ab10-7a5f385ed23d.png)

### Functions
```py
def splitText(
        text : str,
        char_limit : int = default_char_limit,
        split_by : list = ['\n', ' ', '.', ','],
        erase_leadings : list = ['\n', ' ']
    ) -> list:
```
`splitText(text, ...)` tries to split the message when the `char_limit` is about to get hit and a `split_by` character is found. It also erases the leading characters in the created messages. `char_limit` is defaultly set to `2000` and `split_by` characters are ordered by starting with the most likable one to split with.


