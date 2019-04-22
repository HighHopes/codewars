"""Description:
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :]
"""


def count_smileys(arr):
	counter = 0
	valid_eyes = [":", ";"]
	valid_nose = ["-", "~"]
	valid_mouth = [")", "D"]
	for i in arr:
		if len(i) == 2:
			if i[0] in valid_eyes and i[1] in valid_mouth:
				counter += 1
		elif len(i) == 3:
			if i[0] in valid_eyes and i[1] in valid_nose and i[2] in valid_mouth:
				counter += 1
	return counter


print(count_smileys([':)', ';(', ';}', ':-D']))
