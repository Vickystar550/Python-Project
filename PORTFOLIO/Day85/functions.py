from tkinter import filedialog, messagebox, Text
from PIL import Image, ImageTk, ImageDraw, ImageFont

class ButtonFunctions:
    def __init__(self):
        self.filetypes = (
            ('All files', '*.*'),
            ('Screenshot', '*.png'),
            ('JPEG', '*.jpg'),
            ('SVG', '*.svg'),
            ('text files', '*.txt'))
        self.watermark_text: Text = None

    def get_location(self, **kwargs):
        """get the location of a file in the computer's file system"""
        type_ = kwargs.get('type')

        if type_:
            file_path = filedialog.askopenfilename(
                title=f'Open the {type_} File',
                filetypes=self.filetypes)
        else:
            file_path = filedialog.askopenfilename(
                title=f'Open the File',
                filetypes=self.filetypes)
        return file_path

    def enter(self, **kwargs):
        """write the watermark to the image"""
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
        try:
            # get the image draw object
            draw = ImageDraw.Draw(IMAGE)
        except NameError:
            load_image()
            enter()
        else:
            self.write_watermark(draw_object=draw)

    def write_watermark(self, draw_object):
        # get text
        txt = self.get_text()

        # using the text function of the draw object to write to the image
        times_ = int(IMAGE.size[1] // 10 * 10)
        for t in range(10, times_, 10):
            draw_object.text((10, t), text=txt, fill='white', direction=180, align='center')

        # write to canvas or saving in a file:
        IMAGE.show()
        # print(canvas_image)
        canvas.itemconfig(canvas_image, image=IMAGE)

    def get_text(self):
        txt = self.watermark_text.get("1.0", END).strip()

        # check if an entered text is not the initialized one
        if txt == "Enter your watermark here":
            if messagebox.askyesno(title='Edit Message',
                                   message='Continue with this as watermark?'):
                return txt

    def pil_image(self, fp: str, **kwargs):
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

    def load_image(self):
        """load an image from the given location in the computer file system"""
        file_path = self.get_location(type='Image')
        if file_path:
            im = self.pil_image(fp=file_path)
            global IMAGE
            IMAGE = im
            # preparing PIL image for tkinter canvas widget
            photo = ImageTk.PhotoImage(im.resize(CANVAS_SIZE))
            im.show()
            global canvas_image
            canvas_image = canvas.create_image((200, 200), image=photo, anchor=CENTER)

    def picture_watermark(self):
        # get the main image
        image_path = self.get_location(type_='Image')
        background_image = self.pil_image(fp=image_path)

        # get the watermark logo
        logo_path = self.get_location(type_='Logo')
        logo_image = self.pil_image(fp=logo_path, convert='RGBA')

        max_logo_size = (200, 200)
        logo_image.thumbnail(max_logo_size)

        logo_image.show()
