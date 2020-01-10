"""Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in "I\n I\n I", or printed:

I
 I
  I"""

def draw_stairs(n):
    result = ""
    spaces = 1
    for i in range(n):
        result += "I\n" + " " * spaces
        spaces += 1

    return result.strip()

print(draw_stairs(3))
