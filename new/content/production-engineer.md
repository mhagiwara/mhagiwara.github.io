Title: Things I Wish I Had Known When I Transitioned from an Academic Researcher to a Software Engineer
Date: 2016-01-17 12:00
Tags: Programming
status: draft

## Introduction

It's been almost a year since I started working as a software engineer, after transitioning from an academic researcher.
In the past I had written some production code for a system which had been used probably around a thousand users a day,
but never had I written production code used in such a scale (*millions* of users per day).

For an average Ph.D. student, probably the best code you would write at school may be some crappy 'demo' system of your research that goes
unmaintained for months until your professor finds out it throws an error every time he tries it before his important presentation and tells you to fix it.

It's been a real challenge for me to write production-ready code that will be used by millions of people. Here are some things I wish I had known before this challenge.

## Code quality

You are sometimes tempted to write hacky, crappy code to meet some deadline as a software engineer. Actually, code quality and speed of development is not trade-off -
in order to develop fast, you need to write clean code.

> The only way to make the deadline— the only way to go fast— is to keep the code as clean as possible at all times. (Clean Code, Chapter 1)

> Improving quality reduces development costs. ... You don't have to choose between quality, cost, and time -- they all go hand in hand. (Code Complete, Chapter 23)

Also, if you are working in any company, any team, your code will surely be read, and read A LOT. First by yourself, but then by team members,
and maybe someone you never thought would read your code.

> Write Programs for People First, Computers Second (Code Complete, Chapter 34)

> Favor read-time convenience to write-time convenience.   Code is read far more times than it's written, even during initial development.
(Code Complete, Chapter 6)

## How to write functions

Probably the best explanation you heard about what a function is, is it's something that takes some arguments and returns a result, and that's it.

Clean Code, Chapter 3

> Describe everything the routine does.   In the routine's name, describe all the outputs and side effects. If a routine computes report totals and opens an output file, ComputeReportTotals() is not an adequate name for the routine. ComputeReportTotalsAndOpen-OutputFile() is an adequate name but is too long and silly. If you have routines with side effects, you'll have many long, silly names. The cure is not to use less-descriptive routine names; the cure is to program so that you cause things to happen directly rather than with side effects. (Code Complete, Chapter 7)

> Pseudocode Programming Process (Code Complete, Chapter 9)

## Enjoy debugging!

'The single biggest activity on most projects' (Code Complete, Chapter 20)
'On some projects, debugging occupies as much as 50 percent of the total development time.' (Code Complete, Chapter 23)

Create a checklist of type of errors you have made on the project (Code Complete, Chapter 20)

'Even if an error at first appears not to be your fault, it's strongly in your interest to assume that it is.'
(Code Complete, Chapter 23)'

Scientific method for debugging - 1) make a hypothesis, 2) create data/environment that proves/disproves the hypothesis, 3) repeat.
create a 'debug memo' - related to 'confessional debugging' - explicitly write down your hypotheses

Limit the time spent on debugging - if no progress, work on something else and let your subconcious work on the problem.

## Error Handing

Write Your Try-Catch-Finally Statement First
(Clean Code, Chapter 7)

Everything breaks - not only DB access or some remote call

## Teach

Try Rubber duck debugging - (Pragmatic Programmer, Chapter 4)
https://en.wikipedia.org/wiki/Rubber_duck_debugging

try to
teammate
being able to verbalize how a piece of code works
and 'you think you kind of understand it'
