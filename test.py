data = [1,2,3,4,5]
canvas_height = 450
canvas_width = 870
x_width = canvas_width / (len(data)+1)
offset = 10
spacing_bet_rect = 10
normalised_data = [i / max(data) for i in data]
print(normalised_data)
for i ,height in enumerate(normalised_data):
    print(i,height)
    x0 = i*x_width + offset + spacing_bet_rect
    y0 = canvas_height - height *400  #we have multiplied 400 because we will normalised our values with one
                                       # formila so that our data won't exceed our canvas
    x1 = (i+1) * x_width
    y1 = canvas_height
    print(f"({x0},{y0})\t({x1},{y1})")



    # canvas.create_rectangle(x0,y0,x1,y1,fill = "#A90042")
    # canvas.create_text((x0+2),y0,anchor=  SW,text = str(data[i]),font = ("new roman",15,"italic bold"),fill = "orange")

# color = ['red' for x in range(3)]
# print(color)