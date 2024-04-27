from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont

CANVAS_SIZE = (500, 600)
CANVAS_MID = int(CANVAS_SIZE[0]/2), int(CANVAS_SIZE[1]/2)
print(CANVAS_MID)
IMAGE = None

############### PART 2: FUNCTIONS ###############

def get_location(**kwargs):
    """get the location of a file in the computer's file system"""
    type_ = kwargs.get('type')

    filetypes = (
        ('All files', '*.*'),
        ('Screenshot', '*.png'),
        ('JPEG', '*.jpg'),
        ('SVG', '*.svg'),
        ('text files', '*.txt'),
    )
    if type_:
        file_path = filedialog.askopenfilename(
            title=f'Open the {type_} File',
            filetypes=filetypes)
    else:
        file_path = filedialog.askopenfilename(
            title=f'Open the File',
            filetypes=filetypes)
    return file_path


def enter(**kwargs):
    """perform the watermarking operation"""
    x = kwargs.get('x')
    y = kwargs.get('y')
    fill_ = kwargs.get('fill')
    font_ = kwargs.get('font')
    anchor_ = kwargs.get('anchor')
    spacing_ = kwargs.get('spacing')
    align_ = kwargs.get('align')
    direction_ = kwargs.get('direction')
    stroke_width = kwargs.get('stroke_width')
    stroke_fill = kwargs.get('stroke_fill')

    # checking if IMAGE object exists:
    if IMAGE:
        # create an ImageDraw Object
        draw = ImageDraw.Draw(IMAGE)
        write_watermark(draw_object=draw)
    else:
        load_image()


def write_watermark(draw_object: ImageDraw):
    """write the watermark on the image"""
    # get text
    txt_input = get_text()

    if txt_input is not None:
        # get a font:
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 10)

        # writing watermark at the mid-way along the image height
        mid_h = (IMAGE.size[1]) // 10 * 10
        mid = int(mid_h / 2) - 10

        draw_object.multiline_text((10, mid),
                                   font=fnt,
                                   text=txt_input,
                                   fill=(255, 255, 255, 50),
                                   direction='ltr', )

        # write to canvas or saving in a file:
        IMAGE.show()
        # canvas.itemconfig(canvas_image, image=IMAGE)
        canvas_text = canvas.create_text(CANVAS_MID, text=f"{txt_input}", fill='white', anchor='s')


def get_text():
    """Return the text input from tkinter Text widget"""
    txt = entry.get().strip()

    # shorten text length
    if len(txt) > 20:  # using 20 as default number of characters in a line
        txt = txt[:21] + '\n' + txt[21:]

    # check if an entered text is not the initialized one
    if txt == "Enter watermark here":
        # confirm if a text should be retained
        if messagebox.askyesno(title='Edit Message',
                               message='Continue with this as watermark?'):
            return txt
    else:
        return txt


def pil_image(fp: str, **kwargs):
    """Return a PIL image object if the given fp holds an image"""
    convert = kwargs.get('convert')
    try:
        if convert:
            im = Image.open(fp).convert(convert)
        else:
            im = Image.open(fp)
    except OSError:
        messagebox.showerror(title='OSError!!!',
                             message="This file is not an Image File.\nPlease make another selection")
    else:
        return im


def load_image():
    """load an image from the given location in the computer file system"""
    file_path = get_location(type='Image')
    if file_path:
        im = pil_image(fp=file_path)
        if im is None:
            load_image()
        else:
            global IMAGE
            IMAGE = im
            # preparing PIL image for tkinter canvas widget
            photo = ImageTk.PhotoImage(im.resize(CANVAS_SIZE))
            im.show()
            global canvas_image
            canvas_image = canvas.create_image((200, 200), image=photo, anchor=CENTER)


def picture_watermark():
    # get the main image if not existing
    if IMAGE is None:
        load_image()

    # get the watermark logo
    logo_path = get_location(type_='Logo')
    logo_image = pil_image(fp=logo_path, convert='RGBA')
    l, h = IMAGE.size

    logo_l = l // 10 * 2
    logo_h = h // 10 * 2

    logo_image.thumbnail((logo_l, logo_h))

    result_image = Image.new('RGBA', IMAGE.size)
    result_image.paste(IMAGE, (0, 0))

    logo_x = int(result_image.width / 2) - 5  # Adjust the position as needed
    logo_y = int(result_image.height / 2) - 5  # Adjust the position as needed

    # paste watermark logo to the main image:
    result_image.paste(logo_image, (logo_x, logo_y), mask=logo_image.split()[3])

    result_image.show()


############## PART 1: UI SETUP ##################
# -------- create the window ---------
window = Tk()
window.title("Victor Nice's Watermark Software")
window.minsize(width=800, height=1200)
window.config(padx=50, pady=50)

# ------------- styling ------------
window.option_add('*foreground', 'black')  # set all tk widgets' foreground to black
window.option_add('*activeForeground', 'black')  # set all tk widgets' foreground to green

style = ttk.Style(window)
style.configure('TLabel', foreground='black')
style.configure('TEntry', foreground='black')
style.configure('TMenubutton', foreground='black')
style.configure('TButton', foreground='black')
# -----------------------

# -------------- LABELS ---------------
welcome_label = Label(text='Welcome to your Super Watermark Software', font=('Serif', 30, 'bold'))
welcome_label.grid(row=0, column=0, columnspan=3)
welcome_label.config(padx=50, pady=50, fg='white')

water_mark_label = Label(text='Text Watermark:', font=('Courier', 20, 'normal'))
water_mark_label.grid(row=3, column=0)
water_mark_label.config(padx=20, pady=20, fg='white')

# ------------------- BUTTON ----------------
load_image_button = Button(text='Load Image', command=load_image)
load_image_button.config(padx=30, pady=10, font=('Courier', 20, 'normal'), fg='white')
load_image_button.grid(row=1, column=0)

picture_watermark_button = Button(text='Picture as Watermark', command=picture_watermark)
picture_watermark_button.config(padx=30, pady=10, font=('Courier', 20, 'normal'), fg='white')
picture_watermark_button.grid(row=1, column=1, columnspan=2)

enter_water_mark_button = Button(text='enter', command=enter)
enter_water_mark_button.config(font=('Courier', 20, 'normal'), fg='white')
enter_water_mark_button.grid(row=3, column=2)

# --------------------- ENTRY ------------------
entry = Entry(borderwidth=10)
entry.configure(font=('Courier', 20, 'normal'), fg='white', width=25)
entry.insert(END, "Enter watermark here")
entry.grid(row=3, column=1, padx=20, pady=10)

# ------------------ CANVAS --------------------
canvas = Canvas(width=500, height=600, bg='black', highlightthickness=0)
canvas.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

#########################################

# ACTIVATE TKINTER
window.mainloop()
