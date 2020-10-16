'''
Function Name    :  Create Arcs In Different Shapes
Function Date    :  16 Oct 2020
Function Author  :  Prasad Dangare
Input            :  Shapes
Output           :  It Display All Different Arcs Shapes

'''

# Python Program To Create Arcs In Different Shapes

from tkinter import*

# Create Root Window

root = Tk()

# Create Canvas As A Child To Root Window

c = Canvas(root, bg="white", height=700, width=1200)

# Create Arcs In The Canvas

id = c.create_arc(100, 100, 400, 300, Width=3, start=270, extent=180,
                  outline="red", style="arc")

id = c.create_arc(500, 100, 800, 300, Width=3, start=90, extent=180,
                  outline="red", style="arc")

id = c.create_arc(100, 400, 400, 600, Width=3, start=0, extent=180,
                  outline="blue", style="arc")

id = c.create_arc(500, 400, 800, 600, Width=3, start=180, extent=180,
                  outline="blue", style="arc")

id = c.create_arc(900, 400, 1200, 600, Width=3, start=90, extent=90,
                  outline="black", style="arc")

# Add Canvas To The Root

c.pack()

# Wait For Any Events

root.mainloop()
