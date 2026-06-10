---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
type: "entry"
tags: [] # choose from data/allowed-tags.yaml
summary: ""
---
Write the entry. Put images/files as normal Markdown in the body.
