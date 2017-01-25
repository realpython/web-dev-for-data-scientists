# Lesson 1: Intro

## Welcome

Slides (`npm run day1`):

1. Hi!
1. `whoami`
1. Who are you?
1. About this workshop

## Why should data scientists learn web dev?

- Visualization - show off that data!
- Gather - scraping, accessing (and parsing) web apis
- Interaction - get people to interact with and add more data
- Learn - always be learning (ABCs!)

## Web Development 101

### Modern Web Development

What technologies (languages, frameworks, concepts) do you need to know a to be a full-stack web developer?

1. Client-side
1. Server-side
1. Database

Review *Interlude: Modern Web Development* in **Real Python Course 2**.

### Web Frameworks

Developers got tired of writing the same boilerplate code over and over again, so they lumped together the code common to all web apps into a framework.

What are some tasks common to the majority of web apps?

1. foo
1. bar

For the most part, you can split web frameworks between high and low-level. Turn the *Interlude: Web Frameworks, Compared* chapter in **Real Python Course 2** for more information.

Besides preventing repetition, web frameworks help with organizing your file and folder structure...

### MVC Structure

Model-View-Controller (MVC) is a design pattern used to separate your application's concerns in order to make it easier to scale:

- Model: the data itself
- View: visual representation of the data
- Controller: link between the model and the view

The controller updates the model based on user actions in the view and also updates the view when the model changes.

The majority of modern web frameworks utilize this design pattern. Again, high-level frameworks like Django and Rails force you to use this design pattern. Flask, on the other hand, Flask does not enforce any specific design patterns; you can structure your app how you see fit. It's recommended that you use some form of MVC since the majority of web applications use this pattern.

> **NOTE:** Check out [Model-View-Controller (MVC) Explained -- With Legos](https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/) for more info on the MVC design pattern.

## Environment Setup

> **NOTE:** All commands are unix environment

1. Install Python v[3.6](https://docs.python.org/3.6/whatsnew/3.6.html) - [download](https://www.python.org/downloads/)
1. Create a project directory:

  ```sh
  $ mkdir web-dev-for-data-scientists
  $ cd web-dev-for-data-scientists
  $ python3.6 -m venv env
  $ source/env/bin/activate
  ```

  > **NOTE:** If you're on a Python 3 version > 3.6, use `pyvenv-3.x env`

1. Install Flask v[0.12](https://pypi.python.org/pypi/Flask/0.12):

  ```sh
  (env)$ pip install Flask==0.12
  (env)$ pip freeze > requirements.txt
  ```

1. Deactivate and reactivate virtualenv:

  ```sh
  (env)$ deactivate
  $ source/env/bin/activate
  ```

## Review

Answer the following questions...

1. Why should data scientists learn web development?
1. What do you need to know to be a full-stack web developer?
1. What is a web framework?
1. Why should you use a web framework?
1. What's the MVC design pattern?

## Homework

1. Complete the [Flask Quick Start](http://flask.pocoo.org/docs/0.12/quickstart/)
1. Complete the [Flask Tutorial](http://flask.pocoo.org/docs/0.12/tutorial/)
