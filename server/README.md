# Cookov server

A small Flask API that builds a word-level Markov chain from a fortune corpus and returns generated fortunes.

## Files

- `server.py`: Flask app. Defines the routes and starts the server on `127.0.0.1:5001`.
- `produce.py`: Reads `Messages_<LOCALE>.txt`, builds the chain, and generates a phrase with `produce_phrases(locale)`.
- `markov_chain.py`: `MarkovGraph`, a weighted adjacency structure. `add_link` counts word pairs; `next_state` samples the next word in proportion to those counts.
- `Messages_EN.txt`: English corpus, one message per line.

## Setup

Requires Python 3 with Flask and Flask-Cors:

```bash
pip install Flask Flask-Cors
```

## Running

Run from this folder, because the corpus is opened with a relative path:

```bash
python server.py
```

## Routes

| Method | Route                  | Response                                              |
|--------|------------------------|-------------------------------------------------------|
| GET    | `/`                    | `Hello, World!` (health check)                        |
| GET    | `/language/<language>` | One generated phrase as plain text, with a trailing space |

`<language>` selects the corpus: `EN` loads `Messages_EN.txt`. An unknown code makes the server fail, because no corpus file exists for it.

The response has a trailing space, which the client does not need to trim because it only displays the text.

## Testing the generator without the API

```bash
python -c "import produce; print(produce.produce_phrases('EN'))"
```

## Notes

- CORS is enabled for all origins, so the client dev server can call the API directly. Restrict it before deploying publicly.
- The server runs Flask's development server (`app.run`). Use a WSGI server such as gunicorn for anything beyond local use.
- The chain is rebuilt on every request. Building it once at startup is the obvious next step if speed matters.
