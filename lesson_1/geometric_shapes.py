def draw_rectangle(height, width):
    for i in range(height):
        print("*"*width)

def draw_upsidedown_triangle(width):
    width+=1
    for i in range(width):
        print("*"*(width := width - 1))

def draw_triangle(width):
    n = 0
    for i in range(width):
        print("*"*(n := n + 1))

def draw_empty_rectangle(height, width):

    if height > 2 and width > 2:
        print("*"*width)
        for i in range(height-2):
            print(f"*{" "*(width-2)}*")
        print("*"*width)
    else:
        print("cannot be printed")

draw_rectangle(3,5)
print()
draw_upsidedown_triangle(5)
draw_triangle(5)
print()
draw_empty_rectangle(3,3)

