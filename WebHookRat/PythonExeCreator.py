import os
import fade
logo = """
                      .__                     
  _____ _____    ____ |__| _________    ______
 /     \\__  \  /    \|  |/ ___\__  \  /  ___/
|  Y Y  \/ __ \|   |  \  / /_/  > __ \_\___ \ 
|__|_|  (____  /___|  /__\___  (____  /____  >
      \/     \/     \/  /_____/     \/     \/
      Python Exe Creator
"""
logo_text = fade.pinkred(logo)
print(logo_text)

def create_exe():
    python_file = input("Python dosyasının adını (uzantısı ile birlikte) girin: ")
    if not os.path.exists(python_file):
        print("Belirtilen dosya bulunamadı.")
        return
    
    os.system(f"pyinstaller --onefile {python_file}")
    print("Exe dosyası oluşturuldu.")

if __name__ == "__main__":
    create_exe()
