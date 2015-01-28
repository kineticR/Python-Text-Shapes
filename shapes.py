
Square 1

Given an integer n draw a square of n x n asterisks. Like the ones below.


 n = 3
 *  *  * 
 *  *  *  
 *  *  * 
 
 
 n = 7
 *  *  *  *  *  *  * 
 *  *  *  *  *  *  * 
 *  *  *  *  *  *  * 
 *  *  *  *  *  *  *  
 *  *  *  *  *  *  * 
 *  *  *  *  *  *  * 
 *  *  *  *  *  *  *
 

def square(n):
    i = 0
    while i < n:
        print(" * " * n)
        i += 1
 
 
 -------------------------------------------------------------------------
 
 
Square 2

Draw an empty square. Like the ones below.


n = 2
** 
**


n = 6
******
*    *
*    *
*    *
*    *
******


def empty_square(n):
    i = 0
    while i < n:
        if i == 0 or i == (n - 1):  # if it is the first or last line.
            print("*" * n)
            i += 1
        else:                       # if it is the middle lines.
            print("*" + " " * (n - 2) + "*")
            i += 1


 -------------------------------------------------------------------------
 
 
 Square 3
 
 Draw an empty square, but instead of asterisks, use + for corners, - for
 the top and bottom sides and | for the left and right ones.
 Like the ones below.
 
 
n = 2 
++
++


n = 9
+-------+
|       |
|       |
|       |
|       |
|       |
|       |
|       |
+-------+


def square_corners(n):
    i = 0
    while i < n:
        if i == 0 or i == (n - 1):  # if it is the first or last line
            print("+" + ("-" * (n - 2)) + "+")
            i += 1
        else:                       # if it is the middle lines
            print("|" + " " * (n - 2) + "|")
            i += 1


-------------------------------------------------------------------------


Rectangle 1

Given two integers n and m draw a rectangle of n x m asterisks. Like the ones below.


n = 1, m = 5
*****


n = 5, m = 20
********************
********************
********************
********************
********************


def rectangle(n, m):
    i = 0
    while i < n:
        print("*" * m)
        i += 1


-------------------------------------------------------------------------


Rectangle 2

Draw an empty rectangle. Like below.


n = 3, m = 4
****
*  *
****


n = 10, m = 50
**************************************************
*                                                *
*                                                *
*                                                *
*                                                *
*                                                *
*                                                *
*                                                *
*                                                *
**************************************************


def empty_rectangle(n, m):
    i = 0
    while i < n:
        if i == 0 or i == (n -1):   # if first or last line
            print("*" * m)
            i += 1
        else:
            print("*" + (" " * (m - 2) + "*"))
            i += 1
 
 
-------------------------------------------------------------------------


Rectangle 3

Draw an empty rectangle, but instead of asterisks, use + for corners,
- for the top and bottom sides and | for the left and right ones.
Like the ones below.


n = 2, m = 3
+-+
+-+


n = 6, m = 45
+-------------------------------------------+
|                                           |
|                                           |
|                                           |
|                                           |
+-------------------------------------------+


def rectangle_corners(n, m):
    i = 0
    while i < n:
        if i == 0 or i == (n - 1):   # if first or last line
            print("+" + ("-" * (m - 2) + "+"))
            i += 1
        else:
            print("|" + (" " * (m - 2) + "|"))
            i += 1


-------------------------------------------------------------------------


Triangle 1

Given an integer N draw a triangle of asterisks. The triangle should
have n lines, the i-th line should have i asterisks on it.
Like the ones below.


n = 1
*


n = 12
*
**
***
****
*****
******
*******
********
*********
**********
***********
************


def triangle(n):
    i = 1
    while i <= n:
        print("*" * i)
        i += 1


-------------------------------------------------------------------------


Triangle 2

Draw an empty triangle. Like the ones below.


n = 3
*
**
***


n = 4
*
**
* *
****


n = 10
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
**********


def empty_triangle(n):
    i = 1
    while i <= n:
        if i == 1 or i == 2 or i == n:  # these 3 places will never be empty.
            print("*" * i)
            i += 1

        else:
            print("*" + (" " * (i - 2)) + "*")
            i += 1


-------------------------------------------------------------------------


Triangle 3

Draw an empty triangle, but instead of asterisks, use + for corners,
- for the bottom side, | for the left side and \ for the right side.
Like the ones below.


n = 2
+
++


n = 14
+
|\
| \
|  \
|   \
|    \
|     \
|      \
|       \
|        \
|         \
|          \
|           \
+------------+


def triangle_corners(n):
    i = 1
    while i <= n:
        if i == 1:      # if first line.
            print("+")
            i += 1

        if i == n:      # if last line.
            print("+" + ("-" * (i - 2)) + "+")
            i += 1

        else:           # if in between first and last line.
            print("|" + (" " * (i - 2)) + "\\")
            i += 1





 _______  _______  _______  _______  _______    
(  ____ )(  ____ \(  ___  )(  ____ \(  ____ \   
| (    )|| (    \/| (   ) || (    \/| (    \/   
| (____)|| (__    | (___) || |      | (__       
|  _____)|  __)   |  ___  || |      |  __)      
| (      | (      | (   ) || |      | (         
| )      | (____/\| )   ( || (____/\| (____/\ _ 
|/       (_______/|/     \|(_______/(_______/(_)
- By Rhys Dunn 2015.
- Question from https://www.weheartswift.com/drawing-with-text

