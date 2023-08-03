import time
import pyautogui
from django.shortcuts import render
from django.http import HttpResponse

def send_whatsapp_message(group_ids, message):
    time.sleep(5)
    for group_id in group_ids:
        open_group_chat(group_id)
        time.sleep(20)
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(2)

def open_group_chat(group_id):
    group_url = f'https://web.whatsapp.com/accept?code={group_id}'
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite(group_url + '\n')

def index(request):
    if request.method == 'POST':
        group_ids = request.POST['group_id'].split(',')
        message = request.POST['message']

        try:
            send_whatsapp_message(group_ids, message)
            return HttpResponse("WhatsApp messages sent successfully.")
        except Exception as e:
            return HttpResponse(f"An exception occurred while sending the WhatsApp messages: {str(e)}")

    return render(request, 'web/index.html')
