
---
# Python Command-Line Shell

## Overview

This project is a command-line shell built in Python, inspired by the challenge from the Codecrafters website. It provides a simple interface for executing basic commands and interacting with the file system, offering a terminal-like experience.

## Features

- **Basic Commands**:
  - `goto`: Change the current directory.
  - `show`: List files and directories in the current directory.
  - `cdir`: Create new directories.
  - `help`: Display available commands.
  - `clear`: Clear the terminal screen.
  - `git`: Use git in the terminal.
  - **Execute Programs**: Run shell commands directly from the Python shell.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  - `colorama` (for colored output)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Xolo978/Shell.git
   cd shell
   ```

2. Install the required dependencies (if any):

   ```bash
   pip install colorama
   ```

### Usage

To run the shell, execute the following command in your terminal:

```bash
python index.py
```

You will see a prompt displaying the current working directory, followed by a `$` symbol. Type any of the available commands and press Enter.

### Example Commands

- `show` - Lists the files and directories in the current directory.
- `goto commands` - Changes the current directory to the specified path.
- `mdir new_directory` - Creates a new directory named `new_directory`.
- `help` - Lists all available commands.
- `clear` - Clears the terminal screen.
- You can also execute standard shell commands directly (e.g., `git status`, etc.).

## Learnings

During this project, I explored:

- Dynamic command execution and modular code organization.
- Type safety and clarity in Python using type hints.
- User interface enhancements with colored output using the `colorama` library.

## Challenges Faced

- **Command Handling**: Ensuring proper parsing and handling of user inputs to avoid command execution errors.
- **Error Feedback**: Providing meaningful error messages for failed command executions.

## Future Improvements

- Enhance command support by adding more built-in commands, including `git`.
- Improve error handling for clearer user feedback.
- Implement better styling for a more authentic terminal experience.
- Conduct thorough testing and optimization for performance.
