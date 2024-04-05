#Write a program that computes and displays the perimeter of a letter-size (8.5 × 11 inch) sheet of paper and the length of its diagonal.
import math
l=8.5
w=11.0
p=2*(l+w)
d=math.sqrt(w**2+l**2)
print(p)
print(d)
