# Q2_SidiaSam
#Python Coding
#Question 2
Ellen is a new Assembly Line Manager in a shoe factory. So far, everything has been going very smoothly for her an N shoes of the same model and size have been produced. Exactly half of them are left shoes and the other half are right shoes.
The freshly sewn shoes are standing in a line, in no particular order (i.e with no regard to being left or right shoes). They now need to be matched into pairs and packed into boxes.
Ellen would like to assign this task to her subordinate workers. Each worker should get a distinct interval of adjacent shoes, such that the number of left shoes is equal to the number of right shoes. Each shoe must be assigned to exactly one worker.
What is the maximum number of workers that Ellen can assign to this task?
Write a function:
	def solution(S)
that, given s string S of letters “L” and “R”, denoting the types of shoes in line (left or right), returns the maximum number of intervals such that each interval contains an equal number of left or right shoes.
Given S = “RLLLRRRLLR”, the function should return 4, because S can be split into intervals: “RL”, “LLRR”, “RL” and “LR”.
Given S = “LLRLRLRLRLRLRR”, the function should return 1. Write an efficient algorithm for the following assumptions:
a.	N is an integer within the range [2…100,000];
b.	String S consists only of the characters “R” and/or “L”;
c.	The number of letters “L” and “R” in string S is the same. 


