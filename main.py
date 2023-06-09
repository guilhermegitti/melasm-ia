#importing required modules
import tkinter
import customtkinter
from PIL import ImageTk,Image
from tkinter import NW, filedialog
import os
import ia
import webbrowser

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("1920x1080+0+0")
# app.attributes('-fullscreen', True)
app.title('Login')
app.iconbitmap('test_images/artificial-intelligence.ico')


class Inicial(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.path_file = []
        self.title("MelasmIA")
        self.geometry("1920x1080+0+0")
        self.iconbitmap('test_images/artificial-intelligence.ico')
        # self.attributes('-fullscreen', True)
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "artificial-intelligence.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.search_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "search-2-256 (1).png")),
                                                 dark_image=Image.open(os.path.join(image_path, "search-2-256.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.chart_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chart-256 (1).png")),
                                                     dark_image=Image.open(os.path.join(image_path, "chart-256.png")), size=(20, 20))
        self.resultImg = customtkinter.CTkImage(Image.open("test_images/melas.jpg"), size=(300, 300))
        self.produto1 = customtkinter.CTkImage(Image.open("test_images/SERUM CLAREADOR TECH PEEL PREMIUM.png"), size=(150, 150))
        self.produto2 = customtkinter.CTkImage(Image.open("test_images/PEELING DE LARANJA CLEANSER.png"), size=(150, 150))
        self.produto3 = customtkinter.CTkImage(Image.open("test_images/MÁSCARA DE OURO VITA MASK 40G.png"), size=(150, 150))
        self.produto4 = customtkinter.CTkImage(Image.open("test_images/KIT CLAREADOR TECH PEEL PREMIUM.png"), size=(150, 150))
        self.produto5 = customtkinter.CTkImage(Image.open("test_images/ESPUMA CREMOSA DE LIMPEZA CLEANSER.png"), size=(150, 150))
        self.produto6 = customtkinter.CTkImage(Image.open("test_images/EMULSÃO FACIAL NEW ACTIVE FPS35 – 200gr.png"), size=(150, 150))
        self.produto7 = customtkinter.CTkImage(Image.open("test_images/serum.jpg"), size=(150, 150))
        self.produto8 = customtkinter.CTkImage(Image.open("test_images/serum2.jpg"), size=(150, 150))


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  MelasmIA", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Meu Resultado",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chart_image, anchor="w", command=lambda: self.frame_2_button_event("frame_2"))
        self.frame_2_button.grid(row=4, column=0, sticky="ew")
        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Medir Progresso",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.search_image, anchor="w", command= self.frame_6_button_event)
        self.frame_6_button.grid(row=3, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Nova Detecção",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command= self.frame_3_button_event)
        self.frame_3_button.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
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
        self.second_label = customtkinter.CTkLabel(self.second_frame, text="Meu Resultado", font=("Arial",32))
        self.second_label.grid(row=0, column=0, padx=20, pady=10)
        self.second_large_image_label = customtkinter.CTkLabel(self.second_frame,text="", image=self.resultImg)
        self.second_large_image_label.grid(row=1, column=0, padx=20, pady=10)
        self.second_label_result = customtkinter.CTkLabel(self.second_frame,text="-")
        self.second_label_result.grid(row=2, column=0, padx=20, pady=10)
        self.second_label_Re = customtkinter.CTkLabel(self.second_frame, text="Recomendações", font=("Arial",32))
        self.second_label_Re.place(x=760,y=440)
        self.second_image_label1 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto1)
        self.second_image_label1.place(x=130, y=500)
        self.second_label_description = customtkinter.CTkLabel(self.second_frame, text="\n\nSERUM CLAREADOR TECH PEEL PREMIUM", font=("Arial",13))
        self.second_label_description.place(x=330, y=500)
        self.second_frame_button_1 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280, command=lambda: webbrowser.open_new("https://www.vitaderm.com/serum-clareador-tech-peel-premium/p"))
        self.second_frame_button_1.place(x=330, y=600)
        self.second_image_label2 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto2)
        self.second_image_label2.place(x=650, y=500)
        self.second_label_description2 = customtkinter.CTkLabel(self.second_frame, text="\n\nPEELING DE LARANJA CLEANSER" , font=("Arial",13))
        self.second_label_description2.place(x=830, y=500)
        self.second_frame_button_2 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280 , command=lambda: webbrowser.open_new("https://www.vitaderm.com/peeling-de-laranja-cleanser/p"))
        self.second_frame_button_2.place(x=830, y=600)
        self.second_image_label3= customtkinter.CTkLabel(self.second_frame, text="", image=self.produto3)
        self.second_image_label3.place(x=1130, y=500)
        self.second_label_description3 = customtkinter.CTkLabel(self.second_frame, text="\n\nMÁSCARA DE OURO VITA MASK" , font=("Arial",13))
        self.second_label_description3.place(x=1330, y=500)
        self.second_frame_button_3 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280 , command=lambda: webbrowser.open_new("https://www.vitaderm.com/mascara-de-ouro-vita-mask-40g/p"))
        self.second_frame_button_3.place(x=1330, y=600)

        self.second_image_label4 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto4)
        self.second_image_label4.place(x=130, y=750)
        self.second_label_description4 = customtkinter.CTkLabel(self.second_frame, text="\n\nKIT CLAREADOR TECH PEEL PREMIUM" , font=("Arial",13))
        self.second_label_description4.place(x=330, y=750)
        self.second_frame_button_4 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280 , command=lambda: webbrowser.open_new("https://www.vitaderm.com/kit-clareador-tech-peel-premium/p"))
        self.second_frame_button_4.place(x=330, y=850)
        self.second_image_label5 = customtkinter.CTkLabel(self.second_frame, text="", image=self.produto5)
        self.second_image_label5.place(x=650, y=750)
        self.second_label_description5 = customtkinter.CTkLabel(self.second_frame, text="\n\nESPUMA CREMOSA DE LIMPEZA CLEANSER" , font=("Arial",13))
        self.second_label_description5.place(x=830, y=750)
        self.second_frame_button_5 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280, command=lambda: webbrowser.open_new("https://www.vitaderm.com/espuma-cremosa-de-limpeza-cleanser/p"))
        self.second_frame_button_5.place(x=830, y=850)
        self.second_image_label6= customtkinter.CTkLabel(self.second_frame, text="", image=self.produto6)
        self.second_image_label6.place(x=1130, y=750)
        self.second_label_description6 = customtkinter.CTkLabel(self.second_frame, text="\n\nEMULSÃO FACIAL NEW ACTIVE FPS35" , font=("Arial",13))
        self.second_label_description6.place(x=1330, y=750)
        self.second_frame_button_6 = customtkinter.CTkButton(self.second_frame, text="Clique Aqui!", width=280, command=lambda: webbrowser.open_new("https://vitaderm-es.com.br/produto/emulsao-facial-new-active-fps35-200gr/"))
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


        # create fifth frame
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifth_frame.grid_columnconfigure(0, weight=1)
        self.fifth_label = customtkinter.CTkLabel(self.fifth_frame, text="Meu Resultado", font=("Arial",32))
        self.fifth_label.grid(row=0, column=0, padx=20, pady=10)
        self.fifth_large_image_label = customtkinter.CTkLabel(self.fifth_frame,text="", image=self.resultImg)
        self.fifth_large_image_label.grid(row=1, column=0, padx=20, pady=10)
        self.fifth_label_Re = customtkinter.CTkLabel(self.fifth_frame, text="Recomendações", font=("Arial",32))
        self.fifth_label_Re.place(x=760,y=500)
        self.fifth_image_label1 = customtkinter.CTkLabel(self.fifth_frame, text="", image=self.produto7)
        self.fifth_image_label1.place(x=150, y=650)
        self.fifth_label_description = customtkinter.CTkLabel(self.fifth_frame, text="\n\nSERUM REVITALIZANTE FACIAL" , font=("Arial",13))
        self.fifth_label_description.place(x=330, y=650)
        self.fifth_frame_button_1 = customtkinter.CTkButton(self.fifth_frame, text="Clique Aqui!", width=280, command=lambda: webbrowser.open_new("https://www.vitaderm.com/serum-revitalizante-facial-ionderm-vita-tempo/p"))
        self.fifth_frame_button_1.place(x=330, y=750)
        self.fifth_image_label2 = customtkinter.CTkLabel(self.fifth_frame, text="", image=self.produto8)
        self.fifth_image_label2.place(x=650, y=650)
        self.fifth_label_description2 = customtkinter.CTkLabel(self.fifth_frame, text="\n\nSERUM HIDRATANTE FACIAL ANTI-IDADE" , font=("Arial",13))
        self.fifth_label_description2.place(x=830, y=650)
        self.fifth_frame_button_2 = customtkinter.CTkButton(self.fifth_frame, text="Clique Aqui!", width=280, command=lambda: webbrowser.open_new("https://www.vitaderm.com/serum-hidratante-facial-anti-idade-dermacrono-defense-fps30-uva10/p"))
        self.fifth_frame_button_2.place(x=830, y=750)
        self.fifth_image_label3= customtkinter.CTkLabel(self.fifth_frame, text="", image=self.produto5)
        self.fifth_image_label3.place(x=1150, y=650)
        self.fifth_label_description3 = customtkinter.CTkLabel(self.fifth_frame, text="\n\nEMULSÃO FACIAL NEW ACTIVE FPS35", font=("Arial",13))
        self.fifth_label_description3.place(x=1330, y=650)
        self.fifth_frame_button_3 = customtkinter.CTkButton(self.fifth_frame, text="Clique Aqui!", width=280, command=lambda: webbrowser.open_new("https://www.vitaderm.com/espuma-cremosa-de-limpeza-cleanser/p"))
        self.fifth_frame_button_3.place(x=1330, y=750)


        # create fifth frame
        self.sixth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixth_frame.grid_columnconfigure(0, weight=1)
        self.sixth_label = customtkinter.CTkLabel(self.sixth_frame, text="Comparação", font=("Arial",32))
        self.sixth_label.grid(row=0, column=0, padx=20, pady=10)
        self.sixth_frame_1 = customtkinter.CTkButton(self.sixth_frame, text="Upload da foto antiga", width=200, height=70, font = my_font_text, command=lambda: self.upload("left"))
        self.sixth_frame_1.place(x=600, y=120)
        self.sixth_frame_1 = customtkinter.CTkButton(self.sixth_frame, text="Upload da foto atual", width=200, height=70, font = my_font_text, command=lambda: self.upload("right"))
        self.sixth_frame_1.place(x=900, y=120)

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

    def upload(self,direction):
        # Abre o gerenciador de arquivos para selecionar uma imagem
            file_path = filedialog.askopenfilename(
                filetypes=[("Imagens PNG", "*.png")],
                title="Selecione uma imagem",
                initialdir="/",
            )
            if file_path:
                if direction == "left":
                    self.img = customtkinter.CTkImage(Image.open(file_path), size=(300,400))
                    self.img_1 = customtkinter.CTkLabel(self.sixth_frame, text="", image=self.img)
                    self.img_1.place(x=500, y=300)
                    self.path_file.insert(0, file_path)
                else:
                    self.img = customtkinter.CTkImage(Image.open(file_path), size=(300,400))
                    self.img_2 = customtkinter.CTkLabel(self.sixth_frame, text="", image=self.img)
                    self.img_2.place(x=900, y=300)
                    self.button = customtkinter.CTkButton(self.sixth_frame,text="Comparar Imagens", width=200, height=70, font = ("Arial",12), command= self.compararImagens)
                    self.button.place(x=750, y=750)
                    self.path_file.insert(1, file_path)


    def compararImagens(self):
        prediction_img1 = ia.getPredictions(self.path_file[0])
        prediction_img2 = ia.getPredictions(self.path_file[1])

        area_img1 = self.get_area(prediction_img1)
        area_img2 = self.get_area(prediction_img2)

        self.second_large_image_label.destroy()
        self.second_label_result.destroy()
        if(area_img1 > area_img2):
            self.second_label_result = customtkinter.CTkLabel(self.second_frame,text="Detectamos um aumento na área do melasma",font=("Arial",27),fg_color="red")
            self.second_label_result.grid(row=3, column=0, padx=20, pady=150)
            self.select_frame_by_name("frame_2")
        elif(area_img1 < area_img2):
            self.second_label_result = customtkinter.CTkLabel(self.second_frame,text="Detectamos uma diminuição na área do melasma",font=("Arial",27),fg_color="green")
            self.second_label_result.grid(row=3, column=0, padx=20, pady=150)
            self.select_frame_by_name("frame_2")

    def get_area(self,json_data):
        predictions = json_data['predictions']
        total_area = 0

        for prediction in predictions:
            prediction_width = prediction['width']
            prediction_height = prediction['height']
            area = prediction_width * prediction_height
            total_area += area

        return total_area
    
    def analizar(self, path):
        self.config(cursor="watch")
        predictions = ia.indentificarMelasma(path)
        self.config(cursor="")
        if not predictions:
            self.fifth_large_image_label.destroy()
            self.resultImg = customtkinter.CTkImage(Image.open("prediction.jpg"), size=(300, 300))
            self.fifth_large_image_label = customtkinter.CTkLabel(self.fifth_frame,text="", image=self.resultImg)
            self.fifth_large_image_label.grid(row=1, column=0, padx=20, pady=10)
            self.select_frame_by_name("frame_5")
            self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="My Results",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=lambda: self.frame_2_button_event("frame_5"))
            self.frame_2_button.grid(row=4, column=0, sticky="ew")
        else:
            self.second_label_result.destroy()
            self.second_large_image_label.destroy()
            self.resultImg = customtkinter.CTkImage(Image.open("prediction.jpg"), size=(300, 300))
            self.second_large_image_label = customtkinter.CTkLabel(self.second_frame,text="", image=self.resultImg)
            self.second_large_image_label.grid(row=1, column=0, padx=20, pady=10)
            self.select_frame_by_name("frame_2")
            self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="My Results",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=lambda: self.frame_2_button_event("frame_2"))
            self.frame_2_button.grid(row=4, column=0, sticky="ew")

    def capturarImagem(self):
        ia.abrirCamera()
        self.select_frame_by_name("frame_3")
        self.img = customtkinter.CTkImage(Image.open("recorte.jpg"), size=(300,400))
        self.img_1 = customtkinter.CTkLabel(self.third_frame, text="", image=self.img)
        self.img_1.place(x=700, y=300)
        self.button = customtkinter.CTkButton(self.third_frame,text="Analizar Imagem", width=200, height=70, font = ("Arial",12), command=lambda: self.analizar("recorte.jpg"))
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
        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget() 
        if name == "frame_6":
            self.sixth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sixth_frame.grid_forget() 


    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self, version):
        self.select_frame_by_name(version)

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_6_button_event(self):
        self.select_frame_by_name("frame_6")


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
