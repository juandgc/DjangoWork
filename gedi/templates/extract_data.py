#!/usr/bin/env python
# change this line to meet your system configuration


# Version 0.2 by Antti Karvonen, 26.08.2006
# Please feel free to copy, modify and distribute.
# BTW This is the first program I ever made with Python
# and I did it in a hurry, so the code is ugly and not thorougly tested.
# Use it on your own risk.


import sys
import os
import string
import re
from urllib import urlopen,urlencode

debug=0		# debug messages
separate=0	# in results put a new line with "*******" after each register
deli="**"	# delimiter used in extract program file
deli2=";"	# delimiter used in result file

# comments
# line number is actually index of array starting from 0
# therefore for the user always display line_number+1, and internally use line_number

def help():
	print """

USAGE:
extract_data.py [data file | url] [extract program file]

   First parameter can be an url (starting with http://) or any text file including downloaded HTML-file.
   Second parameter is a name of a file containing the extract program. 

   Extract program file includes the instructions how to extract the strings from data file. The results
   are given in CSV-format:
   field;field;field;field <newline>
   field;field;field;field <newline>
   ....

   The syntax of the program file is the following (case sensitive):
      search STRING              Goto next STRING in the data file - if not found then error. STRING can include whitespaces.
      try STRING1 ** STRING2     Try to search next STRING1 before STRING 2 - if not found do nothing. STRING1 and STRING2
                                 may have whitespaces, and they are separated by "**".
                                 UNIMPLEMENTED!!!
      insert STRING              Insert STRING into the results.
      get STRING ** STRING       Insert string between STRING1 and STRING2 into the results.
      next                       All fields are separated by a delimiter and are in the same line.
                                 This command separates a register from another, i.e. adds a new line in the results.
      loop                       Start of the loop. Can be nested.
      until STRING               When STRING is encountered, the loop is ended.
	
   Comment lines start with #.
   Tabs and white spaces are allowed.
	"""


def clean(str):
	str=string.strip(str)
	#str=re.sub('\033','',str)
	str=re.sub('\015','',str)
	str=string.replace(str,"  ","")
	str=str.replace('\n',' ')
	return str


def checkFile(filename):
	a = filename and os.path.isfile(filename)
	if not a:
		sys.stderr.write("File " +filename+ " does not exist or is not accessible!")
		sys.exit()

def getStartPointer(data,str1,pointer):
	# returns the end point of the searched string in string data (file)
	s=string.find(data,str1,pointer)
	if (s<0):
		return 0
	return s+len(str1)

def getSubStr(data,str1,str2,pointer):
	# returns the the next string between str1 and str2 in data-file after pointer 
	global debug
	subStr=""
	s=getStartPointer(data,str1,pointer)
	if (s<0):
		return 0
	e=string.find(data,str2,s+1)
	if (e<0):
		return 0
	subStr=clean(data[s:e])

	if (debug): print "getSubStr(): from "+str(s)+" to "+str(e)
	insert(subStr)
	return e

def isUrl(str):
	if str.startswith("http://"):
		return 1
	return 0
	
def syntaxError(line_num, reason=""):	
	sys.stderr.write("\nError in extract program file. Unexpected syntax on line "+str(l_num+1)+"\n")
	if len(reason)>0:
		sys.stderr.write("reason: "+reason+"\n\n")
	sys.exit()

def getLastLoopStart():
	global loopStartLines
	global debug
	count=len(loopStartLines)-1
	if (debug): print("((((((( getLastLoopStart() s="+str(loopStartLines[count])+" with count="+str(count))
	return loopStartLines[count],count

def removeLastResult():
	global results
	results=results[:-1]

def deleteLastLoopStart():
	global loopStartLines
	global debug
	loop_s_line,count=getLastLoopStart()
	if (debug): print("((((( removing "+str(loop_s_line)+" from the loop list ("+str(count)+")")
	loopStartLines=loopStartLines[:-1]		# remove the last item from the list
	return loop_s_line

def loop_f(loop_s_line,loop_e_line,loop_end_string,loop):
	# to permit recursive loops this has to be a function
	# not checked if file end is reached during the loop
	global d_lines
	global pointer
	global h_data
	global filesize
	global debug
	if (debug): print("(((((((((    LOOP_F() called - from "+str(loop_s_line+1)+" to "+str(loop_e_line)+"   )))))))))")
	i=0
	while (loop):
		if (debug): print("\n\nLOOP STARTS\n\n")
		for looped_line in (range(loop_s_line,loop_e_line)):
			if (debug): print "--> (in loop): execute line "+str(looped_line+1)+": "+string.strip(d_lines[looped_line][:-1])
			prev_pointer=pointer
			numArgs,command,s_str,e_str=parseLine(d_lines[looped_line],looped_line)
			executeCommand(command,s_str,e_str)
			if (debug): print("prevPointer="+str(prev_pointer)+" and pointer="+str(pointer))
			if pointer<prev_pointer:
				if (debug): 
					print ("--> ERROR (in loop) last command was unsuccessfull")
					sys.stderr.write("\nERROR: Command on line "+str(looped_line+1)+" (in loop) was not successfull\n")
				# last command was not successfull
				pointer=prev_pointer
				loop=0
				# sys.exit()
				break
			else:
				if (debug): print ("--> (in loop) going on normal")
				passed_data=h_data[prev_pointer:pointer]
				f=string.find(passed_data,loop_end_str)
				if (f>0) or (pointer>=filesize):
					loop=0
					# bug found: if the last command was getSubStr and it was successfull,
					# then the last insertion should be removed. 
					if (command==4): removeLastResult()
					if (debug): print("--> END STRING ("+loop_end_str+") FOUND at "+str(f))
					if (debug): print("--> setting pointer back to "+str(prev_pointer+f))
					pointer=prev_pointer+f		# pointer is now where then loop end string was found
					break

def executeCommand(command,s_str,e_str):
	global pointer
	global h_data
	global loop
	global loopStartLines
	global loop_e_line
	global loop_end_str
	global debug
	if (debug) and (command!=0):
		print("========================================================================================")
		print("executeCommand(): pointer is "+str(pointer)+" command="+str(command))
	# 1 search STRING
	# 2 try STRING1 ][ STRING2
	# 3 insert STRING
	# 4 get STRING ][ STRING
	# 5 next
	# 0 loop
	# 6 until STRING
	if (command==1):
		pointer=getStartPointer(h_data,s_str,pointer)+1
	elif (command==2):		
		pointer=tryStr(h_data,s_str,e_str,pointer)+1
	elif (command==3):
		insert(s_str)
	elif (command==4):
		pointer=getSubStr(h_data,s_str,e_str,pointer)+1
	elif (command==5):
		insert("nl")
	elif (command==6):
		# recursive loop system
		loop_s_line=deleteLastLoopStart()
		loop_f(loop_s_line,loop_e_line,loop_end_str,loop)

def insert(str):
	global results
	global debug
	if (debug): print("\t\t\t\t\t\t\t\tinsert(): append "+str)
	results.append(str)
	
def tryTo(data,s_str,e_str,pointer):
	global prev_pointer
	sys.strerr.write("called unfinished function tryTo()")
	# test if s_str can be found before e_ste
	# if true -> return end of s_str
	# if not -> return pointer
	return pointer

def splitCommand(line,lineNum):
	global deli
	com_str=""
	s_str=""
	e_str=""
	numArgs=0
	
	list1=line.split(" ",1)
	if (len(list1) < 1):
		# actually never should get here as empty string has been checked before calling this function
		return numArgs
	com_str=string.strip(list1[0]);
	numArgs=numArgs+1
	if (len(list1)<2):
		s_str=""
		e_str=""
	else:
		list2=list1[1].split(deli,1)
		s_str=string.strip(list2[0])
		if len(s_str)<1:
			syntaxError(lineNum,"first parameter is an empty string")
		numArgs=numArgs+1
		if (len(list2) > 1):
			e_str=string.strip(list2[1])
			if len(e_str)<1:
				syntaxError(lineNum,"second parameter is an empty string")
			numArgs=numArgs+1
	return numArgs,com_str,s_str,e_str

def parseLine(line,lineNum):
	global loop
	global loopStartLines
	global loop_e_line
	global loop_end_str
	global debug
	global deli
	# 1 search STRING
	# 2 try STRING1 ][ STRING2
	# 3 insert STRING
	# 4 get STRING ][ STRING
	# 5 next
	# 0 loop
	# 6 until STRING
	
	s_str=""
	e_str=""
	
	# strip of the new line
	line=string.strip(line[:-1])
	if line[:1] == "#" or len(line)<1:
		# omit comments and empty lines
		command=0
		numArgs=0
	else:
		numArgs,com_str,s_str,e_str=splitCommand(line,lineNum)
		if com_str=="loop":
			loop=1
			loop_end_str="" 	# loop should be ended when this string is found
			loop_s_line=lineNum+1
			loopStartLines.append(loop_s_line)
			if (debug): print("(((((( appended "+str(loop_s_line)+" to loopStartLines")
			command=0
		elif com_str=="until":
			if numArgs<2:
				syntaxError(lineNum,"first parameter not found")
			else:
				loop_end_str=s_str
				loop_e_line=lineNum
				command=6
				loop_s_line,count=getLastLoopStart()
				if (debug): print "Looping from "+str(loop_s_line+1)+" to "+str(loop_e_line)+" until '"+loop_end_str+"' is found"
		elif com_str=="search":
			# get the rest of the line
			if numArgs<2:
				syntaxError(lineNum,"first parameter not found")
			else:
				command=1
		elif com_str=="try":
			if numArgs<3:
				syntaxError(lineNum,"incorrect number of parameters")
			else:
				command=2
		elif com_str=="insert":
			if numArgs<2:
				syntaxError(lineNum,"first parameter not found")
			else:
				command=3
		elif com_str=="get":
			if numArgs<3:
				syntaxError(lineNum,"incorrect number of parameters")
			else:
				command=4
		elif com_str=="next":
			command=5
		else:
			command=-1
			syntaxError(lineNum,"unrecognized command")
	return numArgs,command,s_str,e_str

def outputResults(results):
	global deli2
	global separate
	res=""
	for c in results:
		if c=="nl":
			res=res+"\n"
			if (separate): res=res+"**********************\n"
		else:
			res=res+c+deli2
	print res


############################################################################################
#      GLOBAL VARIABLES                                                                    #
############################################################################################


loop=0			# if searching in loop mode
loopStartLines=[]	# a list containing all loop start lines (as there might be nested loops)
loop_e_line=0		# line number where the loop ends
loop_end_str=""		# ending string - when found, jump out of the loop
pointer=0		# file position pointer
prev_pointer=0		# previous file pos pointer (needed to search loop_end_str)
filesize=0 		# the limit for pointer
l_num=0			# line number counter
results=[]		# all strings extracted are stored to this list


############################################################################################
#      MAIN                                                                                #
############################################################################################


# checking the arguments and files
if len(sys.argv) < 3:
	sys.stderr.write("Missing arguments")
	help()
	sys.exit()
else:
	html_src  = sys.argv[1]
	data_file = sys.argv[2]
 
# process extract program file
checkFile(data_file)
df=file(data_file,'r')
d_lines=df.readlines()
df.close()
if (debug): print("datafile has "+str(len(d_lines))+" lines")

# process html data
if isUrl(html_src):
	if (debug):  print("is Url: "+html_src)
	try:
		h_data=urlopen(html_src).read()
	except:
		sys.stderr.write("Error downloading from "+html_src)
		sys.stderr.write("Check if the url is correct")
		sys.exit()
else:
	checkFile(html_src)
	hf=file(html_src,'r')
	h_data=hf.read()
	hf.close()
filesize=len(h_data)
if (debug): print "filesize is "+str(filesize)


# excecute the commands upon data file content
for line in d_lines:
	numArgs,command,s_str,e_str=parseLine(line,l_num)
	# now checking what to do
	if (command<7):
		prev_pointer=pointer
		executeCommand(command,s_str,e_str)
		if (pointer<prev_pointer):
			# last command was not successfull
			sys.stderr.write("\nERROR: Command on line "+str(l_num+1)+" was not successfull\n")
			pointer=prev_pointer
	else:
		sys.stderr.write("unrecognized command "+str(command))
		sys.exit()
	l_num=l_num+1


outputResults(results)
sys.exit()