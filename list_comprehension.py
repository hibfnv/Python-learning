#!/usr/bin/env python
girls=['alice','bernice','clarice']
boys=['chris','anorld','bob']
lettergirls={}
for girl in girls:
	lettergirls.setdefault(girl[0], []).append(girl)
print [b+'+'+g for b in boys for g in lettergirls[b[0]]]
