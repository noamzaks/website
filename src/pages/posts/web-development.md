---
layout: "../../layouts/Layout.astro"
title: Web Development
date: "October 18, 2024"
icon: "fa-solid fa-globe"
description: "A web development guide for those who don't want to do web development."
---

# Web Development

The web possesses many powers:

-   Making stuff accessible to everyone (without having to pay 100$ for Apple's Developer plan).
-   Storing user data and even having real-time updates across devices.
-   Creating fancy stuff.
-   Running Rust/Go/C++ code which even has access to its APIs (and even Python).

However, about 90% of the people I know _really_ don't want to get into JavaScript, understandably.
In this post, I want to go over the "easy" and free way that I know to gain access to these powers.

You've been warned tho - you cannot develop web without doing some JavaScript.

## Bun + Vite + React

The first thing you'll want to do is get some way to write TypeScript (and HTML/CSS if need be) and be able to see the results in real time
using a method called [Hot Reload](https://vite.dev/guide/api-hmr) (or "Hot Module Replacement").

The easiest way I know to do this involves installing [Bun](https://bun.sh/) and then creating a new [Vite](https://vite.dev/) project
by running `bun create vite`.

If you want to have some sort of "state" which should make your HTML change accordingly, I recommend selecting the [React](https://react.dev/) framework (and I recommend the `TypeScript + SWC` variant).

After creating the project, follow the instructions, for example by opening the new folder in Visual Studio Code and then installing the JS libraries with `bun install` and running a local server with `bun run dev` (with hot reload!).

## Firebase Hosting

Now that you've created your cool website, you probably want to put it on some domain in the internet.
Even if you have your domain, you'll need some way to host it.

My recommended free and "easy" way is Firebase Hosting (a Google platform which provides a ton of power). To deploy the app you created above you'll need to follow these steps:

-   Create a new project in the [Firebase Console](https://console.firebase.google.com/). If your project name is `example`, you will be able to deploy to the domain `example.web.app`.
-   Install the `firebase-tools` package locally, as a development dependency for your app, by running `bun add -D firebase-tools`.
-   Sign in to your Google account for the Firebase CLI by running `bun run firebase login`.
-   Link your app to the firebase project by running `bun run firebase init`. If you're using the above setup, you'll want the public directory to be `dist` (which is where `vite` puts the compiled HTML+CSS+JS into).

Now, whenever you're satisfied with the changes you've made locally, you can deploy them by simply running `bun run firebase deploy`.

## Firestore

Next, you probably want to have some shared data for your website, for example if you're building a website to play a game with your girlfriend you may want to store the current game state.

My recommended free and "easy" way is Firestore, which is also available as part of Firebase!

This is a tad more convoluted, and you'll definitely need to follow some [documentation](https://firebase.google.com/docs/firestore/quickstart) for working with it, but the main changes should include clicking "Add app" in your firebase project for the Web, copying the configuration JSON, installing the `firebase` library with `bun add firebase` and having something similar to the following code somewhere in your code:

```typescript
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";

const app = initializeApp({
    // Your config here...
});

export const firestore = getFirestore(app);
```

Then you may use functions such as `getDoc` and `setDoc` which use a hierarchical layout for _basically_ storing JSONs (you have a lot more power than just storing JSONs, but that's a lot of power as is!).

## Mantine

Unless you really enjoy writing CSS, in which case you're probably not reading this, you'll probably want to get yourself some "UI library" to make your website look good without working _too hard_. My recommendation is [Mantine](https://mantine.dev/getting-started/), which I use for almost all of my web projects.

Its documentation is great.

## Writing Python

Working with WebAssembly is not super trivial, so I wouldn't recommend doing it unless you're fairly acquainted with web development.

However, one cool project which gives you a lot of power you probably seek if you hate web development is [PyScript](https://pyscript.net/).

You can use the getting started guide [here](https://docs.pyscript.net/latest/beginning-pyscript/).

**Note:** Sadly, I don't think it can save you the hassle of web development. If you really hate web, you can have a look at my [code battles](../projects/code-battles/) library which lets you create a cool event without writing JavaScript, but it's definitely not "general purpose".
