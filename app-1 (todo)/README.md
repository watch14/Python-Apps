# App-1 (Todo List)

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## Description

This is a small application that allows you to manage your tasks. It is a simple command line interface (CLI) that allows you to add, display, edit, and mark tasks as completed.

## Features

- Add a new task
- Display all tasks
- Edit a task
- Mark a task as completed
- Display completed tasks

## Installation

You can either download the repository and run the application in your local environment or use Docker to run the application in a containerized environment.

### Local Environment

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages by running `pip install -r requirements.txt`.
4. Run the application by executing `python cli_todo.py`.

### Docker

1. Make sure Docker is installed on your machine.
2. Build the Docker image by running `docker build -t todo-app .` in the root directory of the repository.
3. Run the Docker container by executing `docker run -it todo-app`.

## Usage

1. Run the application.
2. Use the following commands to interact with the application:
   - `add`: Add a new task.
   - `show`: Display all tasks.
   - `edit`: Edit a task.
   - `complete`: Mark a task as completed.
   - `exit`: Exit the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to [Streamlit](https://streamlit.io/) for providing a great framework for building web applications.
- Thanks to [pandas](https://pandas.pydata.org/) for providing a powerful data manipulation library.
- Thanks to [PySimpleGUI](https://pysimplegui.readthedocs.io/) for providing a user-friendly GUI library.
- Thanks to [tkinter](https://docs.python.org/3/library/tkinter.html) for providing a simple and powerful GUI library.

## Web App (Streamlit)

This is a web application using Streamlit.

### Usage

1. Run the application by executing `streamlit run web_app_todo.py`.
2. Add a new task by typing in the text box and pressing Enter.
3. Edit a task by clicking on it.
4. Mark a task as completed by clicking on the checkbox next to it.
5. View archived tasks by clicking on the "View Archived Tasks" button.
