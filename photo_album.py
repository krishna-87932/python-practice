import tkinter
import PIL.Image , PIL.ImageTk
import os
import cv2
from functools import partial
SET_HEIGHT = 650
SET_WIDTH = 800
Image_list = os.listdir("images/")
current_imge = 0
windows = tkinter.Tk()
windows.title("Photo_Album")
canvas = tkinter.Canvas(windows,height=SET_HEIGHT,width=SET_WIDTH)
canvas.pack()
def Next(index):
    global photo, current_imge
    print(f"images/{Image_list[index]}")
    image = PIL.Image.open(f"images/{Image_list[index]}")
    photo = PIL.ImageTk.PhotoImage(image)
    canvas.create_image(0,0,anchor="nw",image=photo)
    current_imge +=1
    print(current_imge)
    # if current_imge ==0 or current_imge<0:
    #     current_imge +=1
    # else:
    #     return
print(current_imge)
         
btn = tkinter.Button(windows,text="Next >>", width=50,command=partial(Next, current_imge))
btn.pack()
windows.mainloop()



