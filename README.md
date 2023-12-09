# AirBnB Clone - The Console

![Optional Text](hbnb.png)

## Project Description

Welcome to the AirBnB clone project! This project is a group effort by Wanyoike Edwards and Whitney Oduor, mentored by Guillaume. The goal is to build a command-line interpreter to manage AirBnB objects, laying the foundation for a complete web application.

## Table of Contents

- [Background Context](#background-context)
- [Concepts](#concepts)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Examples](#examples)
- [Authors](#authors)

## Background Context

Before delving into the project, it's crucial to familiarize yourself with the AirBnB concept page. The primary objectives of this project are as follows:

1. **Parent Class (BaseModel):** Create a parent class named `BaseModel` responsible for object initialization, serialization, and deserialization.

2. **Serialization/Deserialization Flow:** Implement a simple flow for serialization/deserialization, connecting instances to dictionaries, JSON strings, and files.

3. **AirBnB-related Classes:** Develop various classes related to AirBnB functionality (e.g., User, State, City, Place) that inherit from the `BaseModel`.

4. **File Storage Engine:** Build the first abstracted storage engine for the project, focusing on file storage.

5. **Unit Testing:** Emphasize the importance of unit testing for all classes and the storage engine to ensure the reliability and functionality of the code.

6. **Python Packages:** Understand and implement Python packages to organize and structure the project effectively.

7. **Datetime, UUID, and Command-line Arguments:** Handle essential concepts such as datetime for time-related operations, UUID for unique identifiers, and command-line arguments for interaction with the command interpreter.

This project serves as a foundational step towards creating a comprehensive AirBnB clone. It not only establishes the core functionalities but also sets the groundwork for subsequent projects involving HTML/CSS templating, database storage, API integration, and front-end development.

It is crucial to adhere to the outlined requirements, including proper documentation, adherence to coding standards, and thorough unit testing. By the end of this project, you'll gain a deep understanding of Python packages, command-line interpreters, unit testing, serialization/deserialization, and other essential concepts that form the backbone of a robust software development process.

## Concepts

- Python packages
- AirBnB clone
- Command-line interpreter
- Serialization and deserialization
- Unit testing
- File storage engine
- Datetime, UUID, and command-line arguments

## Requirements

Make sure to check the [Requirements](#requirements) section for details on script execution, allowed editors, file organization, and unit tests.

## How to Use

## Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
```

## Non-Interactive Mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

```
## Examples

Create a new User:
```bash
(hbnb) create User
```
Retrieve an object from a file:
```bash
(hbnb) show User 1234-5678
```
Update attributes of an object:
```bash
(hbnb) update User 1234-5678 name "John Doe"
```
Destroy an object:
```bash
(hbnb) destroy User 1234-5678
```
## Authors

`Wanyoike Edwards`
`Whitney Oduor`

For a full list of contributors, check the [AUTHORS](#AUTHORS) file.
