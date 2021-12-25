![logo](https://user-images.githubusercontent.com/91157484/147389754-00c8e58f-f0e5-4b59-bf41-eac93a678282.png)
### version 1.0.0
# Discord Message Splitter (<img src="https://user-images.githubusercontent.com/91157484/147390100-f71e95f9-11f8-4497-82b2-725995de00b7.png" data-canonical-src="https://user-images.githubusercontent.com/91157484/147390100-f71e95f9-11f8-4497-82b2-725995de00b7.png" width="27" height="27" /> library)
One algorithm Python library, free for anyone to grab and use without any credit or permission.
Used by Python Discord bots to smartly split long messages into smaller ones in order to cope with the 2000 character per message limit.
Longer messages can also be sent by bots with Discord Nitro subscribed, thus please remember to help Discord grow when writting a bigger project.

![sending](https://user-images.githubusercontent.com/91157484/147390060-1b9eeaaf-93f4-4c18-ab10-7a5f385ed23d.png)

### Splitting Messages
```py
default_char_limit = 2000

def splitText(
	text : str,
	char_limit : int = default_char_limit,
	split_by : list = ['\n', ' ', '.', ','],
	erase_leadings : list = ['\n', ' ']
) -> list:
```
`splitText(text, ...)` tries to split the message when the `char_limit` is about to get hit and a `split_by` character is found. It also erases the leading characters in the created messages. `char_limit` is defaultly set to `2000` and `split_by` characters are ordered by starting with the most likable one to split with.
#### Example
```py
splitText(text, 14, [], []) # split by 14 characters
-> ['I see a red do', 'or\nAnd I want ', 'it painted bla', 'ck\nNo colors a', 'nymore\nI want ', 'them to turn b', 'lack']

splitText(text, 7, [], []) # split by 7 characters
-> ['I see a', ' red do', 'or\nAnd ', 'I want ', 'it pain', 'ted bla', 'ck\nNo c', 'olors a', 'nymore\n', 'I want ', 'them to', ' turn b', 'lack']

splitText(text, 7, ['\n'], []) # split by 7 characters, most likely ending a split with '\n'
-> ['I see a', ' red do', 'or\n', 'And I w', 'ant it ', 'painted', ' black\n', 'No colo', 'rs anym', 'ore\n', 'I want ', 'them to', ' turn b', 'lack']

splitText(text, 7, ['\n', ' '], []) # split by 7 characters, most likely ending a split with '\n', if it is not found, then maybe ' '?
-> ['I see ', 'a red ', 'door\n', 'And I ', 'want ', 'it ', 'painted', ' black\n', 'No ', 'colors ', 'anymore', '\n', 'I want ', 'them ', 'to ', 'turn ', 'black']

splitText(text, 7, ['\n', ' '], [' ']) # additionally erase the leading ' 's (basically "<text>".strip(' '))
-> ['I see', 'a red', 'door\n', 'And I', 'want', 'it', 'painted', 'black\n', 'No', 'colors', 'anymore', '\n', 'I want', 'them', 'to', 'turn', 'black']

splitText(text, 7, ['\n', ' '], ['\n', ' ']) # erase both the leading '\n's and ' 's 
-> ['I see', 'a red', 'door', 'And I', 'want', 'it', 'painted', 'black', 'No', 'colors', 'anymore', 'I want', 'them', 'to', 'turn', 'black']
```

### Splitting Code
```py
def splitCode(
	code : str,
	language_filename : str = "",
	char_limit : int = default_char_limit
) -> list:
```
`splitCode(code, language_filename, ...)` takes source code and language's filename and creates several messages / blocks of code.
#### Example
```py
splitCode("for i in range(20):\n    print(i)", "py", 30) # without Discord's formatting!
-> ['´´´py\nfor i in range(20):\n´´´', '´´´py\n    print(i)´´´']
```
![obraz](https://user-images.githubusercontent.com/91157484/147390920-84a2b438-77fa-4452-a10a-a1eb26319f17.png)

#### Exceptions
This function also raises two exceptions:
- one when Discord's code formatting (`´´´<language_filename>\n` and `´´´`) is already enough to exceed the `char_limit`,
- one when the parsed code already has Discord's code formatting.
```py
# both can be easily caught using the try block
try:
    splitCode("\nfor i in range(20):\n    print(i)", "py", 9)
    splitCode("´´´\nfor i in range(20):\n    print(i)´´´", "py", 30)
except Exception as e:
    print(e)
```
