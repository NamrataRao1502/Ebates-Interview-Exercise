# Ebates-Interview-Exercise

Problem Statement :
-----------------

====================== Start problem description ==================

Exercise: Using any language of your choice write a script that does the following:

Call http://api.viki.io/v4/videos.json?app=100250a&per_page=10&page=1

To go to next page of response you have to increment the page number in the above url. As long as the "more" field returns 

true, you have more data available.

The response is a JSON object which has a response key which is an array of more JSON objects. Each of them has a key 

called flags and within flags there is a key called hd.

Print out how many response objects have flags:hd set to true and how many have hd set to false.

Finally, please check in your code onto GitHub and share the link.

====================== End problem description ======================

Interpreted QA Scenario :
-----------------------

A Python script accesses the viki API, browses through the pages (that has data) in order to compute the total number of HD videos present

Pre-requisites:
--------------

-> Python Interpreter (3.5.1) => To successfully run the program

-> Pycharm (5.0.4) => UI based Python tool used for scripting and compiling the program

Sample Output :
-------------

Total no. of pages parsed are
500

Total no. of response objects that have the flag:hd value set to True is
4026

Total no. of response objects that have the flag:hd value set to False is
0

Process finished with exit code 0

Assumptions :
-----------

-> The 'page' value in the URL starts from 1

-> The '&per_page' value in the URL is maintained at a constant value of 10

Recommendations for further enhancement :
---------------------------------------

-> It checks only for the 'more' value as 'true assuming that only then data is present, although there are cases when the 'more' value is false and there is still data present. It can be enhanced to checked for both values.

-> It computes the 'hd' values with the assumption that &per_page=10'. This value can be manipulated for better accuracy

-> It is not the most optimized implementation and could be refined further, for example, by using internal libraries such as itertools
