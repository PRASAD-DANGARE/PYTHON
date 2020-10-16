'''
Function Name    :  Creation Of Various Shapes In Canvas
Function Date    :  16 Oct 2020
Function Author  :  Prasad Dangare
Input            :  Shapes
Output           :  It Display OVAL, POLYGON,RECTANGLE SHAPES IN CANVAS

'''

# Python Program That Demonstrates The Creation Of Various Shapes In Canvas

from tkinter import*

root = Tk()  # Create Root Window

# Create Canvas As A Child To Root Windows

c = Canvas(root, bg="blue", height=700, width=1200, cursor='pencil')

# Create A Line In The Canvas

id = c.create_line(50, 50, 200, 50, 200, 150, width=4, fill="white")

# Create An Oval In The Canvas

id = c.create_oval(100, 100, 400, 300, width=5, fill="yellow",
                   outline="red", activefill="green")

# Create A Polygon In The Canvas

id = c.create_polygon(10, 10, 200, 200, 300, 200, width=3,
                      fill="green", outline="red", smooth=1, activefill="lightblue")

# Create A Rectangle In The Canvas

id = c.create_rectangle(500, 200, 700, 600,  width=2,
                        fill="gray", outline="black", activefill="yellow")

# Create Some Text In The Canvas

fnt = ('Times', 40, 'bold italic underline')
id = c.create_text(500, 100, text="My Canvas", font=fnt,
                   fill="yellow", activefill="green")

# Add Canvas To The Root Window

c.pack()

# Wait For Any Events

root.mainloop()
