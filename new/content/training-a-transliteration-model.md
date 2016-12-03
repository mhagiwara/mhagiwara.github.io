Title: Training a Transliteration Model using m2m-aligner
Date: 2016-05-21 12:00
Category: NLProc Cookbook
Tags: Machine Translation, Transliteration
status: draft

## Problem

## Solution

Clone it from its Github repository https://github.com/letter-to-phoneme/m2m-aligner

## Discussion

on OSX, you may need to modify the line below in the makefile from

```
INLIBS=-lgcc_s -lpthread -lc -lm
```
to

```
INLIBS=-lpthread -lc -lm
```

to compile.
