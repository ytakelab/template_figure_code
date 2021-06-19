# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,md
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.6.0
#   kernelspec:
#     display_name: jlab38
#     language: python
#     name: jlab38
# ---

# %%
# -*- coding: utf-8 -*-

# %% [markdown]
# # main ipython notebook
# - brief description goes here
#
# Copyright (c) 2021 Yuichi Takeuchi


# %% [markdown]
# ## import modules

# %%
# standard library
import sys

# %% [markdown]
# ## append path and import in-house library

# %%
sys.path.append("../code/helper")
sys.path.append("../code/lib")
sys.path.append("../code/lib/python_utils")

# in-house library
import template_mainFunc

# %% [markdown]
# ## auto-reload

# %%
# %load_ext autoreload
# %autoreload 2

# %% [markdown]
# ## main


# %%
# execute main function as module
a, b = template_mainFunc.main()

# excecute main procecure via the main function
# #%run lib/template_mainFunc

# %%
del a, b

# %%
