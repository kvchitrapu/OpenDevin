# OpenHands Server

This is a WebSocket server that executes tasks using an agent.

## Recommended Prerequisites

- [Initialize the frontend code](../../frontend/README.md)
- Install Python 3.12 (`brew install python` for those using homebrew)
- Install pipx: (`brew install pipx` followed by `pipx ensurepath`)
- Install poetry: (`pipx install poetry`)

## Install

First build a distribution of the frontend code (From the project root directory):
```
cd frontend
npm install
npm run build
cd ..
```
Next run `poetry shell` (So you don't have to repeat `poetry run`)

## Start the Server

```sh
uvicorn openhands.server.listen:app --reload --port 3000
```

## Test the Server

You can use [`websocat`](https://github.com/vi/websocat) to test the server.

```sh
websocat ws://127.0.0.1:3000/ws
{"action": "start", "args": {"task": "write a bash script that prints hello"}}
```

## Supported Environment Variables

```sh
LLM_API_KEY=sk-... # Your OpenAI API Key
LLM_MODEL=gpt-4o   # Default model for the agent to use
WORKSPACE_BASE=/path/to/your/workspace # Default absolute path to workspace
```

## API Schema

There are two types of messages that can be sent to, or received from, the server:

* Actions
* Observations

### Actions

An action has three parts:

* `action`: The action to be taken
* `args`: The arguments for the action
* `message`: A friendly message that can be put in the chat log

There are several kinds of actions. Their arguments are listed below.
This list may grow over time.

* `initialize` - initializes the agent. Only sent by client.
  * `model` - the name of the model to use
  * `directory` - the path to the workspace
  * `agent_cls` - the class of the agent to use
* `start` - starts a new development task. Only sent by the client.
  * `task` - the task to start
* `read` - reads the content of a file.
  * `path` - the path of the file to read
* `write` - writes the content to a file.
  * `path` - the path of the file to write
  * `content` - the content to write to the file
* `run` - runs a command.
  * `command` - the command to run
* `browse` - opens a web page.
  * `url` - the URL to open
* `think` - Allows the agent to make a plan, set a goal, or record thoughts
  * `thought` - the thought to record
* `finish` - agent signals that the task is completed

### Observations

An observation has four parts:

* `observation`: The observation type
* `content`: A string representing the observed data
* `extras`: additional structured data
* `message`: A friendly message that can be put in the chat log

There are several kinds of observations. Their extras are listed below.
This list may grow over time.

* `read` - the content of a file
  * `path` - the path of the file read
* `browse` - the HTML content of a url
  * `url` - the URL opened
* `run` - the output of a command
  * `command` - the command run
  * `exit_code` - the exit code of the command
* `chat` - a message from the user
