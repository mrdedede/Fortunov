# Cookov client

The front end of Cookov: a single-page app built with Vue 2, TypeScript, Bootstrap-Vue and vue-resource. It lets the user pick a language, asks the API for a fortune, and shows the result.

## Structure

- `src/main.ts`: Creates the Vue app and registers the HTTP and Bootstrap plugins.
- `src/App.vue`: Page layout and title.
- `src/components/BasicForm.vue`: Language select and the *Generate!* button. Calls `GET http://localhost:5001/language/<code>`.
- `src/components/Phrase.vue`: Shows a spinner while loading, otherwise the last result.
- `src/plugins/bootstrap-vue.js`: Bootstrap-Vue setup.

## Requirements

- Node.js and npm. Tested with Node 24.
- The Cookov [server](../server/README.md) running on port 5001. Without it, the button shows a connection error.

## Setup

```bash
npm install
```

## Commands

```bash
npm run serve   # dev server with hot reload (usually http://localhost:8080)
npm run build   # production build into dist/
```

## Configuration

The API address is hard-coded in `BasicForm.vue`. Change it there if the server runs elsewhere. See the [Vue CLI configuration reference](https://cli.vuejs.org/config/) for build options.
