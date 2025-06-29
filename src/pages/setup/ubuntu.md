---
layout: "../../layouts/Layout.astro"
title: Ubuntu Setup
icon: "fa-brands fa-ubuntu"
description: "My Ubuntu code development setup."
---

# Ubuntu Setup

-   Remove snap.
-   Install Chrome and Visual Studio Code from their `.deb`.
-   Run `sudo visudo` and add `Defaults pwfeedback` to show asterisks when typing a password.
-   Install the following apt packages: `` sudo apt install -y neovim git gh zsh zsh-autosuggestions zsh-syntax-highlighting default-jre default-jdk curl build-essential linux-headers-`uname -r` dkms virtualbox-dkms``.
-   Set up `.zshrc`:
    -   `export PS1="%~ $ "`
    -   `source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh`
    -   `source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh`
    -   `autoload -Uz compinit && compinit && zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'` (case-insensitive completion)
