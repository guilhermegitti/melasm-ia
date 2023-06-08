#importing required modules
import tkinter
import customtkinter
from PIL import ImageTk,Image
from tkinter import NW, filedialog
import os
import ia

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("1920x1080+0+0")
app.title('Login')


class Inicial(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("MelasmIA")
        self.geometry("1920x1080+0+0")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.resultImg = customtkinter.CTkImage(Image.open("test_images/prediction.jpg"), size=(300, 300))
        self.produto = customtkinter.CTkImage(Image.open(os.path.join(image_path, "produto.png")), size=(150, 150))


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  MelasmIA", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="My Results",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=3, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="New Detection",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        # Home Frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        #Def font 
        my_font_text = customtkinter.CTkFont(family="Arial", size=12)
        my_font_title = customtkinter.CTkFont(family="Arial", size=32)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="Bem vindo ao MelasmIA.", font = my_font_title)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_large_image_label_text = customtkinter.CTkLabel(self.home_frame, text="Utilizamos de uma IA treinada para te ajudar com o tratamento de um Melasma.", font = my_font_text)
        self.home_frame_large_image_label_text.grid(row=2, column=0, padx=20, pady=10)


        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Faça já uma detecção", font = my_font_text, image=self.image_icon_image, compound="right", width=1000, height=50, command=lambda: self.select_frame_by_name("frame_3"))
        self.home_frame_button_2.grid(row=3, column=0, padx=20, pady=10)

        self.home_frame_large_image_label_text2 = customtkinter.CTkLabel(self.home_frame, text="Caso já tenha feito sua primeira detecção, veja clicando no botão abaixo.", font = my_font_text)
        self.home_frame_large_image_label_text2.grid(row=4, column=0, padx=20, pady=10)

        self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="Vejá seus resultados", font = my_font_text, image=self.image_icon_image, compound="right", width=1000, height=50, command=lambda: self.select_frame_by_name("frame_2"))
        self.home_frame_button_3.grid(row=5, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_label = customtkinter.CTkLabel(self.second_frame, text="Meu Resultados", font=("Arial",32))
        self.second_label.grid(row=0, column=0, padx=20, pady=10)
        self.second_large_image_label = customtkinter.CTkLabel(self.second_frame,text="", image=self.resultImg)
        self.second_large_image_label.grid(row=1, column=0, padx=20, pady=10)
        self.second_label_Re = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento", font=("Arial",32))
        self.second_label_Re.grid(row=2, column=0, padx=20, pady=10)
        self.second_image_label1 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label1.place(x=150, y=500)
        self.second_label_description = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description.place(x=330, y=500)
        self.second_frame_button_1 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_1.place(x=330, y=600)
        self.second_image_label2 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label2.place(x=650, y=500)
        self.second_label_description2 = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description2.place(x=830, y=500)
        self.second_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_2.place(x=830, y=600)
        self.second_image_label3= customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label3.place(x=1150, y=500)
        self.second_label_description3 = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description3.place(x=1330, y=500)
        self.second_frame_button_3 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_3.place(x=1330, y=600)

        self.second_image_label4 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label4.place(x=150, y=750)
        self.second_label_description4 = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description4.place(x=330, y=750)
        self.second_frame_button_4 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_4.place(x=330, y=850)
        self.second_image_label5 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label5.place(x=650, y=750)
        self.second_label_description5 = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description5.place(x=830, y=750)
        self.second_frame_button_5 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_5.place(x=830, y=850)
        self.second_image_label6= customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label6.place(x=1150, y=750)
        self.second_label_description6 = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description6.place(x=1330, y=750)
        self.second_frame_button_6 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_3.place(x=1330, y=600)

        self.second_image_label4 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label4.place(x=150, y=750)
        self.second_label_description4 = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description4.place(x=330, y=750)
        self.second_frame_button_4 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_4.place(x=330, y=850)
        self.second_image_label5 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label5.place(x=650, y=750)
        self.second_label_description5 = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description5.place(x=830, y=750)
        self.second_frame_button_5 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_5.place(x=830, y=850)
        self.second_image_label6= customtkinter.CTkLabel(self.second_frame, text="", image=self.produto)
        self.second_image_label6.place(x=1150, y=750)
        self.second_label_description6 = customtkinter.CTkLabel(self.second_frame, text="Recomendações de Tratamento dhududs \n" *5, font=("Arial",15))
        self.second_label_description6.place(x=1330, y=750)
        self.second_frame_button_6 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280)
        self.second_frame_button_6.place(x=1330, y=850)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")        
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)
        
        self.third_frame_1 = customtkinter.CTkLabel(self.third_frame, text="Seja bem vindo a aba de Detecções! \n Para começar uma nova detecção escolha a forma que deseja subir uma imagem: ", font = my_font_title)
        self.third_frame_1.place(x=300, y=30)
        
        self.third_frame_1 = customtkinter.CTkButton(self.third_frame, text="Upload do Computador", width=200, height=70, font = my_font_text)
        self.third_frame_1.configure(command=self.upload_foto)
        self.third_frame_1.place(x=600, y=120)
        
        self.third_frame_1 = customtkinter.CTkButton(self.third_frame, text="Abrir Camera", width=200, height=70, font = my_font_text, command=lambda: self.select_frame_by_name('frame_4'))
        self.third_frame_1.place(x=900, y=120)
        # self.toplevel_window = None

        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_columnconfigure(0, weight=1)
        self.label = customtkinter.CTkLabel(self.fourth_frame, text="Posicione a câmera como no exemplo abaixo", font=("Arial",20))
        self.label.grid(row=1, column=0, padx=20, pady=10)
        self.face_image = customtkinter.CTkImage(Image.open("test_images/face.png"), size=(200, 270))
        self.label_img = customtkinter.CTkLabel(self.fourth_frame, text="", image=self.face_image)
        self.label_img.grid(row=2, column=0, padx=20, pady=10)
        self.button_1 = customtkinter.CTkButton(self.fourth_frame, text="Capturar imagem", width=280, command=self.capturarImagem)
        self.button_1.grid(row=3, column=0, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name("home")

    def upload_foto(self):
            # Abre o gerenciador de arquivos para selecionar uma imagem
            file_path = filedialog.askopenfilename(
                filetypes=[("Imagens PNG", "*.png")],
                title="Selecione uma imagem",
                initialdir="/",
            )

            # Verifica se um arquivo foi selecionado
            if file_path:
                print("Arquivo selecionado:", file_path)
                self.img = customtkinter.CTkImage(Image.open(file_path), size=(300,400))
                self.img_1 = customtkinter.CTkLabel(self.third_frame, text="", image=self.img)
                self.img_1.place(x=700, y=300)
                self.button = customtkinter.CTkButton(self.third_frame,text="Analizar Imagem", width=200, height=70, font = ("Arial",12), command=lambda: self.analizar(file_path))
                self.button.place(x=750, y=750)

    def analizar(self, path):
        self.config(cursor="watch")
        ia.indentificarMelasma(path)
        self.config(cursor="")
        self.second_large_image_label.destroy()
        self.resultImg = customtkinter.CTkImage(Image.open("prediction.jpg"), size=(300, 300))
        self.second_large_image_label = customtkinter.CTkLabel(self.second_frame,text="", image=self.resultImg)
        self.second_large_image_label.grid(row=1, column=0, padx=20, pady=10)
        self.select_frame_by_name("frame_2")

    def capturarImagem(self):
        ia.abrirCamera()
        self.select_frame_by_name("frame_3")
        self.img = customtkinter.CTkImage(Image.open("recorte.jpg"), size=(300,400))
        self.img_1 = customtkinter.CTkLabel(self.third_frame, text="", image=self.img)
        self.img_1.place(x=700, y=300)
        self.button = customtkinter.CTkButton(self.third_frame,text="Analizar Imagem", width=200, height=70, font = ("Arial",12), command=self.analizar)
        self.button.place(x=750, y=750)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")  
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget() 

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


def button_function():
    app.destroy()            # destroy current window and creating new one 
    w = Inicial() 
    w.mainloop()

img1=ImageTk.PhotoImage(Image.open("pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

l3=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
l3.place(x=155,y=195)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)


img2=customtkinter.CTkImage(Image.open("google_logo.webp").resize((20,20), Image.ANTIALIAS))
img3=customtkinter.CTkImage(Image.open("facebook_logo.png").resize((20,20), Image.ANTIALIAS))
button2= customtkinter.CTkButton(master=frame, image=img2, text="VitaDerm", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290)

button3= customtkinter.CTkButton(master=frame, image=img3, text="Marcelinho", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button3.place(x=170, y=290)

# You can easily integrate authentication system 

app.mainloop()
