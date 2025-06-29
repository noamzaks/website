---
layout: "../../layouts/Layout.astro"
title: TyX
icon: "fa-solid fa-file-edit"
description: "A LyX-like experience rewritten for Typst and the modern era."
---

# TyX

While working on my undergraduate studies, for the longest time I found myself mostly working in LyX.
It is incredible for many reasons, but the one that stood out to me was the quality of the output, and
how easy it was to work in multiple languages without having to switch the keyboard layout whenever editing math.

However, in my last year, I saw a fancy exercise instructions PDF posted by the instructor. I sent an email asking
how it was generated, since it looked like LaTeX but it contained English, Hebrew and Arabic, and the setup for Hebrew
is hard enough that I was confident the instructor didn't bother setting up all three languages. Turns out it was [Typst](https://github.com/typst/typst)!

For the rest of my degree I worked in Typst, using the amazing web app they offer, and sometimes also locally with [Tinymist](https://github.com/Myriad-Dreamin/Tinymist).
Then I knew what my next project would be - reimplementing the most important features of LyX in a new Typst-based editor!

This would surely be awesome, since I had long standing issues with LyX:

-   It is difficult to install (and keep updated) with Hebrew support.
-   Errors and backslashes are hard to work with and sometimes Hebrew doesn't "just work".
-   Using packages is a lot tougher than in Typst.
-   It lacks modern application features such as having a web/mobile version.

If this sounds interesting to you, feel free to check it out on [GitHub](https://github.com/tyx-editor/TyX)!
