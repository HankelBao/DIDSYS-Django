# SFLSDID
> The new official website of SFLS Discipline Inspection Department

## Purpose
Usually, people will waste hours to count the final scores of every classes and the final result sometimes will be changed by some naughty children since they are just written on the public blackboard.

The aim of this system is just to release these unnesssary jobs. The final score and ranking will be calculated and displayed automatially. Also, people can make sure that scores on it are definitely just and no one is capable to secretly alter the scores.

## 1.0.0
> Start Time: Augest 9th, 2017
### Philosophy
Put all the content in one page since there are not a lot of things to read for each single part or item. Use an extra page shown above(but still in the same webpage) will toggle the use of ajax so that more things will be required to load to realize more complicated actions and more content.
### Framework
Since I'm learning PYTHON in my school. Let's use django and I find it really awesome because the things used to be really complex in PHP are much easier here. As a result, I save a lot of time. Thanks to Django.

## 2.0.0
> Start Time: May 16, 2018

### Motivation  
It's really hard to tolerate the conditions in school because the server is always starting, making the server seems to be quite unstable.
Actually, Django is awesome and my code is good. Things should be working find.
The school doesn't allow me to upload the system to the Internet. Fine, let's not go against it directly but still....
I will put the database and backend on another server and just leave some html files in the school server.
Also, this means redesigning.

### API
+ /scorebaord/board/get
+ /scorebaord/board/get_by_date
+ /scorebaord/rank/get
+ /scorebaord/rank/get_3
+ /scoreboard/moments/get
+ /scoreboard/moments/get_3
+ /scorer/login

### Accidents
It has been three hours and I still cannot use jsonp in Django. It may simply not supported officially.
After the last attempt, I will switch to some other framework or language if I still fail.

#### Aftermath
I managed to solve it via Access-Control-Allow-Origin
Maybe It won't be quite safe.
Anyway, I solved the problem.

### TODO
Redesign better API and recode the views.py


