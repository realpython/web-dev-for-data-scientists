# Lesson 5: Information Retrieval (continued)

In this session, you will learn how to obtain data from web APIs as well as parse and normalize the data to use in a chart.

## Objectives

By the end of this lesson, you should be able to:

1. Make an AJAX request from the server to grab data from an external API
1. Use a scheduler to continuously pull data from external sources

## Welcome

Slides: `npm run day5`

## Challenge

The focus over the next two sessions will be to build the following app...

### Flask Bitcoin

Build an app that will find the best exchange rates for Bitcoin (USD -> Bitcoin)  from the following cryptocurrency exchanges:

1. [Bitstamp](https://www.bitstamp.net/)
1. [Kraken](https://www.kraken.com/)
1. [Bittrex](https://bittrex.com/)

It should have the following pages:

1. The first page should display the rates and highlight the best one
1. The second page should display the rates over time

### Instructions

We'll work through the pseudocode together. You'll code the app either alone (or with the awesome, good-looking people at your table). We'll come together after each step to review.

### Part 2 - Client

Code Along!

1. Add a Template
1. Set up simple route for a sanity check
1. Refactor route to add a chart:
    - Create a Bokeh Chart
    - Get data from DB
    - Create a Bokeh line, passing in x and y values from the DB data
    - Create the Bokeh static files
    - Render the template
    - Update the *index.html* file
