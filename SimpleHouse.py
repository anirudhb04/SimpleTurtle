import turtle

counter = 2
len = 100
width = 150
angle = 90

# Body of the House
for i in range(0, counter):
	turtle.forward(len)
	turtle.right(angle)
	turtle.forward(width)
	turtle.right(angle)

# Roof of the House
turtle.right(180)
turtle.forward(20)
turtle.right(120)
turtle.forward(140)
turtle.right(120)
turtle.forward(140)
turtle.right(120)
turtle.forward(20)




