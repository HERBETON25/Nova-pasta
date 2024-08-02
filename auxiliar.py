import pyautogui
import time
# pegar posições do mouse e da tela
time.sleep(5)
print(pyautogui.position())



#----------funções do mouse--------
#pyautogui.click(x=1151, y=157) # clica em algum lugar
# pyautogui.moveTo(x=351, y=152, duration=1) move o mouse ate o destino e o tempo de duração
# pyautogui.click(x=1230, y=328)
# pyautogui.scroll(-200) # numero negativo = scroll para baixo

#------funções do teclado-------
# pyautogui.write("escrever") # escrever um texto
# pyautogui.hotkey("ctrl", "c") # ele aperta varias teclas ao mesmo tempo
# pyautogui.press("enter") # pressionar um teclado teclado