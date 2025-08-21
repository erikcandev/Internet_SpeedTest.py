import tkinter as tk
from tkinter import Frame, Label
import speedtest
import threading

#pillow
from PIL import Image, ImageTk
#cores
co0 = "#000000"
co1 = "#ffffff"
co2 = "#24c739"
co3 = "#db3125"
co4 = "#403d3d"
co5 = "#4a88e8"

#janela
janela = tk.Tk()
janela.title("Internet Speedtest")
janela.geometry("350x250")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

#dividindo em frames
frame_logo = Frame(janela, width=350, height=60, bg=co1, relief="flat")
frame_logo.grid(row=0, column=0, padx=0, pady=1, sticky="nsew")

frame_corpo = Frame(janela, width=350, height=190, bg=co1, relief="flat")
frame_corpo.grid(row=1, column=0, padx=0, pady=1, sticky="nsew")



def testar_velocidade():
    # Reseta os labels e desabilita o botão
    l_velocidade_download.config(text="---")
    l_velocidade_upload.config(text="---")
    b_testar.config(text="Testando...", state="disabled")

    try:
        s = speedtest.Speedtest()

        # Atualiza o status para o usuário ver o progresso
        b_testar.config(text="Testando Download...")
        download_speed = s.download() / 1_000_000
        l_velocidade_download.config(text=f"{download_speed:.2f}")

        # Atualiza o status novamente para o teste de upload
        b_testar.config(text="Testando Upload...")
        upload_speed = s.upload() / 1_000_000
        l_velocidade_upload.config(text=f"{upload_speed:.2f}")

        # Teste finalizado, reabilita o botão
        b_testar.config(text="Iniciar Teste", state="normal")
    except speedtest.SpeedtestException as e:
        print(f"Erro no teste de velocidade: {e}")
        l_velocidade_download.config(text="Erro")
        l_velocidade_upload.config(text="Erro")
        b_testar.config(text="Tentar Novamente", state="normal")

def iniciar_teste_thread():
    
    t = threading.Thread(target=testar_velocidade)
    t.start()


logo = Image.open("speed.png")
logo = logo.resize((50, 50))
logo = ImageTk.PhotoImage(logo)

l_logo = Label(frame_logo, image=logo, height=60, compound="left", padx=10, anchor="nw", font=("IvyFont", 16, "bold"), bg=co1, fg=co3)
l_logo.place(x=20, y=0)

l_logo_name = Label(frame_logo, text="Velocidade Internet", compound="left", padx=10, anchor="ne", font=("sans-serif", 18, "bold"), bg=co1, fg=co4)
l_logo_name.place(x=75, y=10)

l_linha = Label(frame_logo, width=350, anchor="nw", font=("IvyFont", 1), bg=co2)
l_linha.place(x=0, y=57)




# Download
l_velocidade_download = Label(frame_corpo, text="---", anchor="nw", font=("sans-serif", 28), bg=co1, fg=co4)
l_velocidade_download.place(x=30, y=20)

l_unidade_download = Label(frame_corpo, text="Mbps Download", anchor="nw", font=("ivyFont", 10), bg=co1, fg=co4)
l_unidade_download.place(x=30, y=70)

down_img = Image.open("baixo.png")
down_img = down_img.resize((45, 45))
down_img = ImageTk.PhotoImage(down_img)
l_down_img = Label(frame_corpo, image=down_img, bg=co1)
l_down_img.place(x=130, y=25)

# Upload
l_velocidade_upload = Label(frame_corpo, text="---", anchor="nw", font=("sans-serif", 28), bg=co1, fg=co4)
l_velocidade_upload.place(x=185, y=20)

l_unidade_upload = Label(frame_corpo, text="Mbps Upload", anchor="nw", font=("ivyFont", 10), bg=co1, fg=co4)
l_unidade_upload.place(x=185, y=70)

up_img = Image.open("cima.png")
up_img = up_img.resize((45, 45))
up_img = ImageTk.PhotoImage(up_img)
l_up_img = Label(frame_corpo, image=up_img, bg=co1)
l_up_img.place(x=285, y=25)

# Botão para iniciar o teste
b_testar = tk.Button(frame_corpo, text="Iniciar Teste", font=("IvyFont", 12, "bold"), bg=co5, fg=co1, relief="raised", overrelief="ridge", command=iniciar_teste_thread)
b_testar.place(x=110, y=120)

janela.mainloop()