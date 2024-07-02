---
layout: "../../layouts/Layout.astro"
title: Code Battles
icon: "fa-solid fa-robot"
description: "A fun group coding experience of writing Python bots to compete in a game!"
---

# Code Battles

In 2023, I was implementing the Bloons TD Battles mobile game in Python with an API to be a "player", in order to host some kind of a Code Battles event. The event consists of around 30 friends, broken into 4-6 teams, where every team creates a Python script which can play the game against other such scripts. The idea came to me after playing in a similar Code Battles event of a custom game. Once every 2 hours or so, everyone comes together to watch the current latest-and-greatest scripts of all the teams compete and the winning teams of every match get some points.

In order to create such an event, I wanted each team to be able to simulate the game on their own, without using any servers (mainly because I don't want to pay for a server on some cloud service). However, I do want some means of "selecting" the current latest-and-greatest script for the upcoming round, and to have some sort of way for myself to pull the team's code and show the matches being played.

The solution I came up with uses Google's (free tier of) Firebase and [Firestore](https://firebase.google.com/docs/firestore) so that every team can collaborate using a single team user and then I can as an admin fetch all of the teams' code. For simulation of the game, since I wanted the game, the API and particularly the teams' scripts to be in Python, I use [PyScript](https://pyscript.net/) to run the Python script on the browser, which uses WASM under the hood. For drawing, the script simply renders elements onto an HTML canvas element.

This has many upsides, but it does come with some costs. The main one being that **if** a team wishes to look for "vulnerabilities" in the simulator code, it will be very easy, since they are running on the same Python "process" as the simulator. The workaround for this issue is currently to ask the teams nicely not to do this.

Shortly after the first event I hosted, I decided to generalize this workflow into the [Code Battles](https://github.com/noamzaks/code-battles) project you can use today to host your very own Code Battles event.

Since then I've been implementing some features in the library and also working on additional features from Bloons TD Battles to host more such events. The documentation for the Code Battles project is hosted [on Read The Docs](https://code-battles.readthedocs.org/).
