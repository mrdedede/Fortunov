# Cookov!

A fortune cookie message generator. It reads a corpus of real fortune cookie messages, learns which words tend to follow which, and produces new, plausible-sounding fortunes that have never been printed in a cookie.

The app has two parts: a **Python/Flask server** that builds a Markov chain from the message corpus and generates phrases, and a **Vue 2 client** that asks the server for a fortune and displays it.

## Table of Contents

- [How it works](#how-it-works)
- [Project structure](#project-structure)
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [API](#api)
- [Adding a language](#adding-a-language)
- [Known limitations](#known-limitations)
- [Sources for fortune cookie messages](#sources-for-fortune-cookie-messages)

## How it works

1. **Training.** `server/produce.py` reads `Messages_<LOCALE>.txt` (one message per line). Each word becomes a state in a *first-order Markov chain*, and every pair of consecutive words adds a weighted link. Punctuation is stripped and words are lowercased, and the start of each message is modelled as the empty state `""`.
2. **Generation.** Starting from the empty state, the chain picks the next word at random, weighted by how often that word followed the current one in the corpus. Generation stops at the end of a sentence, with a word cap of about 10 that stretches when a phrase ends on a weak word such as *a*, *the* or *and*.
3. **Display.** The client calls the server, capitalizes the result and shows it as a "Last Result".

The chain is rebuilt from the text file on every request. That is simple and fast enough for a ~1,100-line corpus, but see [Known limitations](#known-limitations).

## Project structure

```
.
├── client/          Vue 2 + TypeScript single-page app (Bootstrap-Vue UI)
│   └── README.md    Client setup and commands
├── server/          Flask API and Markov chain generator
│   ├── server.py        Flask app and routes
│   ├── produce.py       Builds the chain from a corpus and produces phrases
│   ├── markov_chain.py  The MarkovGraph class (weighted transitions)
│   ├── Messages_EN.txt  English fortune corpus (one message per line)
│   └── README.md        Server setup and API details
└── README.md
```

## Requirements

- **Python 3** with `Flask` and `Flask-Cors` (developed with Python 3.12; any recent Python 3 should work)
- **Node.js and npm** (tested with Node 24)

## Getting started

You need two terminals: one for the server and one for the client. The server must be running before you click *Generate!*.

**1. Start the server** (from the `server/` folder, because the corpus is loaded by a relative path):

```bash
cd server
pip install Flask Flask-Cors
python server.py
```

The API listens on `http://127.0.0.1:5001`.

**2. Start the client** (from the `client/` folder, in another terminal):

```bash
cd client
npm install
npm run serve
```

Open the URL printed by the dev server (usually `http://localhost:8080`), pick a language, and press **Generate!**.

To build a production bundle instead, run `npm run build` in `client/`.

## API

| Method | Route                       | Description                                  |
|--------|-----------------------------|----------------------------------------------|
| GET    | `/`                         | Health check. Returns `Hello, World!`.       |
| GET    | `/language/<language>`      | Returns one generated fortune as plain text. `<language>` is a locale code such as `EN`. |

Example:

```bash
curl http://127.0.0.1:5001/language/EN
```

## Adding a language

1. Create `server/Messages_<CODE>.txt` with one message per line, UTF-8 encoded.
2. Make the client offer that code: in `client/src/components/BasicForm.vue`, add an `<option value="<CODE>">` to the language select.

The server picks up the corpus by file name, so no server code change is needed. Note that the generator's punctuation and bad-ending lists in `server/produce.py` are English-oriented.

## Known limitations

- **Portuguese is disabled.** The option is shown in the UI but cannot be selected, and the corpus `Messages_PT.txt` does not exist yet. A comment in `BasicForm.vue` notes that English and Portuguese phrases were getting mixed.
- **The corpus is reloaded on every request.** Caching the chain once at startup would be a cheap win.
- **The server URL is hard-coded** to `http://localhost:5001` in the client.
- **Output quality is limited by a first-order chain.** Phrases are locally plausible but often drift in meaning, which is part of the charm.

## Sources for fortune cookie messages

- [Reggi Fortune Cookies](https://github.com/reggi/fortune-cookie/blob/master/fortune-cookies.txt)
- [Click the Cookie](https://www.ifortunecookies.co.uk/traditional-fortune-cookie-messages)
- [Josh Madison](https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/)
- [Reddit r/d100 thread](https://www.reddit.com/r/d100/comments/hnw4u7/d100_fortune_cookietype_phrases_of_which_the_dm/)
- [David C. Forman](https://www.linkedin.com/pulse/fortune-cookies-50-memorable-sayings-quotes-david-c-forman-iymgc/)
- [Rockoly](https://rockoly.com/fortune-cookies/)
