# emoji64

It is a tool that translates any text to emojis and vice-versa.

Emoji64 is a variant of [Base64](https://en.wikipedia.org/wiki/Base64) encoding that uses emojis instead of the usual
set of characters.
Base64 is a popular encoding method used to represent binary data in ASCII characters, allowing it to be transmitted
over text-based channels such as email, SMS, or chat.
Emoji64 works in the same way as base64 and can be used to add a fun and playful twist to your data encoding.

## How do I use it?

### Use in your browser

Open [emoji64](http://AwesomeDog.github.io/emoji64/) and you are ready to go.

It looks like this:

![snap](./asset/snapshot.png)

The site can also be hosted by yourself, simply drop `index.html` to any hosting service you like.
You can even download `index.html` to your own PC or Mac and open with your browser!

### Use in command line

Check out `emoji64.py` to any machine with python3 installed and run.

Emoji64 has two modes, encode and decode. It's default mode is encoding the input to Emojis. Simply pass
the `--decode` (or `-d` for short) argument to it, and it will switch to decoding the input. All input is read from
stdin, so it plays nicely with pipes.

Here's an example of encoding and decoding the message "Hello World":

```console
$ chmod u+x emoji64.py

$ ./emoji64.py "Hello World"

😨😜😫🙈😷😜😍😼😫😇😎🙎😷😜😦😒

$ ./emoji64.py -d "😨😜😫🙈😷😜😍😼😫😇😎🙎😷😜😦😒"

Hello World

$ echo "Hello World" | ./emoji64.py | ./emoji64.py -d

Hello World
```

## What is the algorithm?

It is a Base64 scheme whose encoding characters (`ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/`) are
mapped to unicode emojis.
The magic number `128512 - 43` is used for mapping, since emojis start at the `128512` range in unicode and
subtracting `43` ensures that the first possible character('+') in base64 is also the very first emoji in unicode.

This project is inspired by [jasonbarry](https://github.com/jasonbarry/face64) with encoding robustness and multiple
ways of usage.
