import tkinter
from tkinter import *
from PIL import ImageTk, Image

# Set-up for main game
buttonClicked = False

window = tkinter.Tk()
window.title("Hormone Adventure Game")
window.attributes('-fullscreen', True)
window.columnconfigure(2,weight=1)
window.rowconfigure(1,weight=1)

class screen(Frame):
    """A screen is area for content in a program"""
    def __init__(self,master,name):
        Frame.__init__(self,master)
        #Attributes
        self.master=master
        self.name=name
        #Initalise with master
        self.master.addScreen(self)
    def show(self):
        """Method will show screen"""
        self.master.showScreen(self.name)

class screenController(Frame):
    """Screen Controller will manage screens in the program"""
    def __init__(self,parent):
        Frame.__init__(self,parent)
        #Configure
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #Attributes
        self.allScreens={}
        self.currentScreen=None

    def addScreen(self,screenObject):
        """Adds a Screen object to the screenController"""
        #Place the screen
        screenObject.grid(row=0, column=0, sticky="nsew")
        #Add to dictionary
        self.allScreens[screenObject.name]=screenObject

    def showScreen(self,screenName):
        if screenName in self.allScreens:
            #Display
            self.allScreens[screenName].tkraise()
            #Update variable
            self.currentScreen=screenName

# Run homescreen
screenMaster = screenController(window)
screenMaster.grid(row=1,column=0,sticky="NSEW")
homescreen = screen(screenMaster, "1")
Label(homescreen,text="Welcome to the Hormone Adventure Game. This is the list of possible starting Hormones:").grid(row=0,column=0) 
Label(homescreen,text="[GHRH] [CRH] [TRH] [Parathyroid Hormone] [Inactive Vitamin D]").grid(row=1,column=0)
Label(homescreen,text="Please choose a Hormone: ").grid(row=2,column=0) 

# Set-up for all Pathways
subtitles = ["Adrenal Hormone Pathway"]
adrenal1 = screen(screenMaster, "2a")
errorScreen = screen(screenMaster, "error")
Button(homescreen,text="GHRH",command=lambda: errorScreen.show()).grid(row=3,column=0)
Button(homescreen,text="CRH",command=lambda:[adrenal1.show(),adrenal_pathway(True)]).grid(row=4,column=0)
Button(homescreen,text="TRH",command=lambda: errorScreen.show()).grid(row=5,column=0)
Button(homescreen,text="Parathyroid Hormone",command=lambda: errorScreen.show()).grid(row=3,column=1)
Button(homescreen,text="Inactive Vitamin D",command=lambda: errorScreen.show()).grid(row=4,column=1)

def adrenal_pathway(buttonClicked):
    if buttonClicked == True:
        buttonClicked = False  #reset variable
        adrenal2 = screen(screenMaster, "2b.1")
        
        Label(adrenal1,text=subtitles[0]).grid(row=0,column=0) 
        textString = "\nYou awaken in the Hypothalamus carrying Cortisol Releasing Hormone (CRH). Motivated by circadian rhythm and stress,"\
            " you know\nthat you must move forward. The path before you leads to the Anterior Pituitary Gland (APG) door."\
            " Would you like to inspect\nthe door?"
        Label(adrenal1,text=textString).grid(row=1,column=0)
        Button(adrenal1,text="yes",command=lambda:[adrenal2.show(),adrenal_2c(True)]).grid(row=2,column=1)
        adrenal1.show()

        def adrenal_2c(buttonClicked):
            buttonClicked = False  #reset variable
            adrenal3 = screen(screenMaster, "2c.1")
            
            Label(adrenal2,text=subtitles[0]).grid(row=0,column=0)
            textString = "\nThe door to the Anterior Pituitary Gland has a hole labled CRH. You insert the CRH and the door opens."
            Label(adrenal2,text=textString).grid(row=1,column=0)
            Button(adrenal2,text="next",command=lambda:[adrenal3.show(),adrenal_2d(True)]).grid(row=2,column=1)
            adrenal2.show()
            altar = 'no'  #set variable

            def adrenal_2d(buttonClicked):
                buttonClicked = False  #reset variable
                adrenal4 = screen(screenMaster, "2d.1")

                Label(adrenal3,text=subtitles[0]).grid(row=0,column=0)
                textString = "You recover the CRH and walk through the APG door and you see a small room. In the center of the room, there is a small altar"\
                    "\nand another door on the far end of the room. What would you like to inspect?"
                Label(adrenal3,text=textString).grid(row=1,column=0)
                Button(adrenal3,text="altar",command=lambda:[adrenal4.show(),adrenal_2e(True)]).grid(row=2,column=1)
                adrenal3.show()

                def adrenal_2e(buttonClicked):
                    buttonClicked = False  #reset variable
                    adrenal5 = screen(screenMaster, "2e.1")

                    Label(adrenal4,text=subtitles[0]).grid(row=0,column=0)
                    textString = "\nYou inspect the altar and see a slot just big enough for CRH. Would you like to insert the CRH?"
                    Label(adrenal4,text=textString).grid(row=1,column=0)
                    Button(adrenal4,text="yes",command=lambda:[adrenal5.show(),adrenal_2f(True)]).grid(row=2,column=1)
                    adrenal4.show()

                    def adrenal_2f(buttonClicked):
                        buttonClicked = False  #reset variable
                        adrenal6 = screen(screenMaster, "2f.1")

                        Label(adrenal5,text=subtitles[0]).grid(row=0,column=0)
                        textString = "\nThe CRH perfectly slides into the slot and ejects an ACTH molecule, just like a Gacha pod."\
                            "\nNow you can inspect the door."
                        Label(adrenal5,text=textString).grid(row=1,column=0)
                        Button(adrenal5,text="next",command=lambda:[adrenal6.show(),adrenal_2g(True)]).grid(row=2,column=1)
                        adrenal5.show()

                        def adrenal_2g(buttonClicked):
                            buttonClicked = False  #reset variable
                            adrenal7 = screen(screenMaster, "2g.1")

                            Label(adrenal6,text=subtitles[0]).grid(row=0,column=0)
                            textString = "The door is labeled ACTH. Would you like to place the ACTH in the key slot?"
                            Label(adrenal6,text=textString).grid(row=1,column=0)
                            Button(adrenal6,text="yes",command=lambda:[adrenal7.show(),adrenal_2h(True)]).grid(row=2,column=1)
                            adrenal6.show()

                            def adrenal_2h(buttonClicked):
                                buttonClicked = False  #reset variable
                                adrenal8 = screen(screenMaster, "2h.1")

                                Label(adrenal7,text=subtitles[0]).grid(row=0,column=0)
                                textString = "\nThe ACTH opens the door, and you are led to the Adrenal Cortex."
                                Label(adrenal7,text=textString).grid(row=1,column=0)
                                Button(adrenal7,text="next",command=lambda:[adrenal8.show(),adrenal_2i(True)]).grid(row=2,column=1)
                                adrenal7.show()
                                tim = 'no'  #set variable

                                def adrenal_2i(buttonClicked):
                                    buttonClicked = False  #reset variable
                                    adrenal9 = screen(screenMaster, "2i.1")

                                    Label(adrenal8,text=subtitles[0]).grid(row=0,column=0)
                                    textString = "\nYou recover the ACTH and walk to the Adrenal Cortex. Inside the Adrenal Cortex lurks a mysterious skeleton."\
                                        " Behind the skeleton\nlies another door... You can sneak around or approach the skeleton, what will you do?"
                                    Label(adrenal8,text=textString).grid(row=1,column=0)
                                    Button(adrenal8,text="approach",command=lambda:[adrenal9.show(),adrenal_2j(True)]).grid(row=2,column=1)
                                    adrenal8.show()

                                    def adrenal_2j(buttonClicked):
                                        buttonClicked = False  #reset variable
                                        adrenal10 = screen(screenMaster, "2j.1")

                                        Label(adrenal9,text=subtitles[0]).grid(row=0,column=0)
                                        textString = "\nYou slink towards the cobwebbed skeleton and realize its hand is outstretched."\
                                            " Do you give the skeleton your ACTH?"
                                        Label(adrenal9,text=textString).grid(row=1,column=0)
                                        Button(adrenal9,text="yes",command=lambda:[adrenal10.show(),adrenal_2k(True)]).grid(row=2,column=1)
                                        adrenal9.show()

                                        def adrenal_2k(buttonClicked):
                                            buttonClicked = False  #reset variable
                                            adrenal11 = screen(screenMaster, "2l.1")

                                            Label(adrenal10,text=subtitles[0]).grid(row=0,column=0)
                                            textString = "\nYou hand over ACTH, which slowly disappears as the skeleton rattles and hands you Cortisol."
                                            Label(adrenal10,text=textString).grid(row=1,column=0)
                                            Button(adrenal10,text="next",command=lambda:[adrenal11.show(),adrenal_2l(True)]).grid(row=2,column=1)
                                            adrenal10.show()

                                            def adrenal_2l(buttonClicked):
                                                Label(adrenal11,text=subtitles[0]).grid(row=0,column=0)
                                                closing = "You hear the doors behind you close in succession upon obtaining Cortisol."\
                                                "\nNo more adventurers will be able to follow the path you tred, because you have obtained Cortisol and no more is needed."\
                                                "\nThus, all previous steps are closed off. This is known as a negative feedback loop."\
                                                "\n..."\
                                                "\nCarrying Cortisol, you now exit through the door and travel throughout the body."\
                                                "\nCortisol proves to be powerful and have a variety of effects."\
                                                "\nThe Immune systyem becomes suppressed, gluconeogenesis occurs in the liver,"\
                                                "\nprotein catabolism occurs in the muscle, and lipolysis occurs in the adipose tissue."\
                                                "\nThe End!"
                                                Label(adrenal11,text=closing).grid(row=1,column=0)
                                                Button(adrenal11,text="Homescreen",command=lambda:homescreen.show()).grid(row=2,column=0)
                                                image = Image.open("StressFlow.jpeg")
                                                resize_img = image.resize((400,400))
                                                img = ImageTk.PhotoImage(resize_img)
                                                panel = Label(adrenal11, image = img)
                                                panel.photo = img
                                                panel.grid(row=1,column=1)
                                                adrenal11.show()
homescreen.show()
Label(errorScreen,text="Sike. You can only start with CRH. It is the only one.").grid(row=0,column=0,padx=150,sticky="wens")
Button(errorScreen,text="Homescreen",command=lambda:homescreen.show()).grid(row=1,column=0)
window.mainloop()