#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#"""
#QUESTION 2
#"""
def solution(S):
	if len(S) == 2:
		return 1
	workers = 0
	lCount, rCount = 0,0

	for i in S:
		if i == "L": lCount = lCount + 1
		else: rCount = rCount + 1

		if lCount == rCount: workers = workers + 1

	return workers

