---
layout: "../../layouts/Layout.astro"
title: VSCode Setup
icon: "fa-solid fa-file-code"
description: "My VSCode setup."
---

# VSCode Setup

-   Install the following extensions:
    -   Python (`ms-python.python`)
    -   clangd (`llvm-vs-code-extensions.vscode-clangd`)
    -   Prettier (`esbenp.prettier-vscode`)
    -   Ruff (`charliermarsh.ruff`)
    -   Tinymist (`myriad-dreamin.tinymist`)
    -   Mypy Type Checker (`ms-python.mypy-type-checker`)
    -   WSL (`ms-vscode-remote.remote-wsl`)
    -   Better Comments (`aaron-bond.better-comments`)
    -   Error Lens (`usernamehw.errorlens`)
-   Change the following settings:
    -   In `editor.codeActionsOnSave`, set `source.organizeImports` to true.
    -   Change `python.languageServer` to Pylance.
    -   Change `editor.formatOnSave` to true.
