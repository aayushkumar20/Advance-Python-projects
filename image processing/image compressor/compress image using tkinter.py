from tkinter import font
from PIL import ImageTk
from PIL import Image as PilImage
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

class ImageCompressor(Tk):
    def __init__(self,winTitle,xSize,ySize,*args):
        super(ImageCompressor,self).__init__()
        if args:
            self.configure(bg=args)
        self.geometry(f'{xSize}x{ySize}')
        self.title(winTitle)
        self.resizable(False,False)
        self.compressFile=Button(text="select image",command=self.GetImage)
        self.compressFile.place(x=25,y=25)
        self.chooseQuality=Label(self,text="choose quality",font=("Helvetica",10))
        self.chooseQuality.place(x=60,y=70)
        self.scaleValue=Scale(self,from_=100,to=0)
        self.scaleValue.place(x=0,y=70)
        self.saveFolder=Button(text="select folder to save image",command=self.SavedFolder)
        self.saveFolder.place(x=62.5,y=100)
        self.imageNameLabel=Label(text="image name",font=("Helvetica",10))
        self.imageNameLabel.place(x=62.5,y=135)
        self.imageName=Entry(self,bd=2)
        self.imageName.place(x=62.5,y=150)
        self.compressImageBtn=Button(text="compress image",command=self.CompressImage,bd=5)
        self.compressImageBtn.place(x=290,y=90)
        self.mainloop()
    def GetimageFile(self):
        self.compressLocation=filedialog.askopenfilename()
        if self.compressLocation:
            messagebox.showinfo("File",self.compressLocation)
        else:
            messagebox.showinfo("Error","No file selected")
    def SavedFolder(self):
        self.saveLocation=filedialog.askdirectory()
        if self.saveLocation:
            messagebox.showinfo("Folder",self.saveLocation)
        else:
            messagebox.showinfo("Error","No folder selected")
    def CompressImage(self):
        self.scaleNum=self.scaleValue.get()
        try:
            self.imageToCompress=PilImage.open(self.compressLocation)
            self.getImageExtension=self.CompressLocation.rsplit(".",1)
            self.imageExtension=self.getImageExtension[1]
            self.imageEntryName=self.imageName.get()
            self.imageToCompress.save(f'{self.saveLocation}/{self.imageEntryName}.{self.imageExtension}',quality=self.scaleNum)
            messagebox.showinfo("Success","Image compressed successfully")
            messagebox.showinfo({self.saveTo})
        except:
            messagebox.showinfo("Error","No image selected")
            messagebox.showinfo("Error","something went wrong")
MyNewGUI=ImageCompressor("Image Compressor",500,500)