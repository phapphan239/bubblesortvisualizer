import turtle, random, time

def update():
	window.ontimer(update, 20)

def create_array(n):
	arr = []
	elmn = []
	while len(arr) < n:
		x = random.randint(1, n)
		if x not in elmn:
			arr.append(x)
			elmn.append(x)
	return arr

def drawcols(array, highlight, highlight_color):
	global pen
	pen.goto(-230, -250)
	pen.pensize(15)
	for i in array:
		pen.color("white" if i not in highlight else highlight_color)
		pen.pendown()
		pen.left(90)
		pen.pendown()
		pen.forward(50 * i)
		pen.penup()
		pen.right(180)
		pen.forward(50 * i)
		pen.left(90)
		pen.forward(50)

array = create_array(10)

window = turtle.Screen()
window.title("just a turtle")
window.bgcolor("black")

window.tracer(0, 0)

pen = turtle.Turtle()
pen.hideturtle()
n = len(array)
    
for i in range(n):
	swapped = False
	for j in range(0, n - i - 1):
		if array[j] > array[j + 1]:
			array[j], array[j + 1] = array[j + 1], array[j]
			swapped = True
		pen.clear()
		drawcols(array, [array[j + 1]], "red")
		window.update()
		time.sleep(0.3)
	if not swapped:
		break

for i in range(n + 1):
	drawcols(array, array[min(i, n):min(i + 3, n)], "lightgreen")
	window.update()
	time.sleep(0.2)

window.update()

update()
window.mainloop()