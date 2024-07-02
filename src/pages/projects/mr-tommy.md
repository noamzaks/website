---
layout: "../../layouts/Layout.astro"
title: Mr. Tommy
icon: "fa-brands fa-python"
description: "Rapid development of Motion Planning algorithms."
---

# Code Battles

For the final project in the Algorithmic Robotics and Motion Planning course given in Tel Aviv University by Prof. Dan Halperin, I wanted to implement some motion planning algorithms, such as PRM, RRT, RRT*, dRRT, dRRT* and some techniques such as hybridization.

During the course itself, I used the [discopygal](https://www.cs.tau.ac.il/~cgl/discopygal/docs/index.html) package, which certainly does raise the floor and ease the creation of such algorithms, and provides nice applications to design _Scenes_, i.e. environments with obstacles and robots which need to get from start to end, and a nice application to view _Solvers_, which are the algorithms that find a good route for the robots.

However, the package did have some caveats. For one, it is a nuisance to install, since it uses Conan and a the CGAL C++ project underneath the hood, and that requires some additional hacking for it to work. Another caveat of this approach is that the Python bindings of the C++ code are okay-ish, but not as friendly to work with as well-written Python code. The last caveat of the package that bothered me was that the tools were written in Qt, which is overall a fine choice, but I believe when developing such algorithms I want to be using Python and have everything very close to the code itself (and not in a separate app).

For this, I created the [Tommy](https://github.com/noamzaks/mrtommy) package. The package provides some interfaces written in Python with typing, which makes developing such algorithms easier. It should be noted that this comes with a performance cost of course, which I tried to cover by using [Numba](https://numba.pydata.org/), but that didn't turn out so well.

After creating that package, and completing my project, I wanted to think about the other issues I had with the package, and how I would go about solving them. For the scene editor, I created the [Tommy VSCode Extension](https://github.com/noamzaks/vscode-mrtommy), which lets you work on the Scene's JSON file, in a straightforward fashion, and see the scene in real time in a separate panel.

The current status of Tommy is alpha, with many lacking features and necessary performance improvements, but it does seem like a better approach to me nonetheless.
