---
jupyter:
  jupytext:
    formats: ipynb,py:percent,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernelspec:
    display_name: jlab38
    language: python
    name: jlab38
---

```python
# -*- coding: utf-8 -*-
```

# main ipython notebook
- brief description goes here

Copyright (c) 2021 Yuichi Takeuchi



## import modules

```python
# standard library
import sys
```

## append path and import in-house library

```python
sys.path.append("../code/helper")
sys.path.append("../code/lib")
sys.path.append("../code/lib/python_utils")

# in-house library
import template_mainFunc
```

## auto-reload

```python
%load_ext autoreload
%autoreload 2
```

## main


```python
# execute main function as module
a, b = template_mainFunc.main()

# excecute main procecure via the main function
#%run lib/template_mainFunc
```

```python
del a, b
```

```python

```
