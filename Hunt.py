import vk_api
import time
import json

vk = vk_api.VkApi(token="Твой токен")
vk._auth_token()
api = vk.get_api()
id = -182725650
ido = "А сюда свой айди"
WFR = 0
vrema = 3
Fantasys = 0

while True:
    dial = api.messages.getHistory(count=1, peer_id=api.users.get()[0]["id"])['items'][0]['text']
    a = api.users.get()[0]["id"]
    print(a)
    dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
    if dial == "Запуск":
        if "☢ Stalker Project ☢" in dials:
            api.messages.edit(peer_id=api.users.get()[0]["id"], message_id=api.messages.getHistory(count=1, peer_id=ido)['items'][0]['id'], message=f"Скрипт успешно запустился, сначала он пойдёт на охоту, а затем бить Random Player", random_id=0)
            while True:
                dial = api.messages.getHistory(count=1, peer_id=api.users.get()[0]["id"])['items'][0]['text']
                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                if "🐗 Danger Zone 🐗" in dials:
                    api.messages.send(peer_id=id, message=f"Окрестности зоны", random_id=0, payload=json.dumps({"button":"1"}))
                    time.sleep(vrema)
                if "Лиманск" in dials:
                    api.messages.send(peer_id=id, message=f"Лиманск", random_id=0, payload=json.dumps({"button":"2"}))
                    Fantasys = 2400
                    if WFR <= 0:
                        time.sleep(vrema)
                        while True:
                            dial = api.messages.getHistory(count=1, peer_id=api.users.get()[0]["id"])['items'][0]['text']
                            dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                            if "🌟 Подарочные коды/Ключи" in dials:
                                api.messages.send(peer_id=id, message=f"🤼‍♂ Группировки", random_id=0, payload=json.dumps({"button":"3"}))
                                time.sleep(vrema)
                                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                            if "👥 Информация о группировке" in dials:
                                api.messages.send(peer_id=id, message=f"Война за ресурсы", random_id=0, payload=json.dumps({"button":"3"}))
                                time.sleep(vrema)
                                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                            if "1⃣ Напасть на случайного игрока" in dials:
                                api.messages.send(peer_id=id, message=f"Напасть на случайного игрока", random_id=0, payload=json.dumps({"button":"1"}))
                                time.sleep(vrema)
                                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                            if "🔫 Нападение на игрока 🔫" in dials:
                                api.messages.send(peer_id=id, message=f"👊 Напасть на игрока", random_id=0, payload=json.dumps({"button":"1"}))
                                WFR = 6
                                time.sleep(Fantasys)
                                break
                            else:
                                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                                api.messages.edit(peer_id=api.users.get()[0]["id"], message_id=api.messages.getHistory(count=1, peer_id=ido)['items'][0]['id'], message=f"Скрипт не понял где он, поэтому он зайдёт в главное меню '☢ Stalker Project ☢' и начнёт выполнять действия, которые создатель скрипта решил приготовить для Никитоса :)", random_id=0)
                                api.messages.send(peer_id=id, message=f"❎ Вернуться в главное меню", random_id=0, payload=json.dumps({"button":"0"}))
                    else:
                        WFR -= 1
                        print(WFR)
                        time.sleep(Fantasys)
                if "❌ Вам необходимо подождать" in dials:
                    Fantasys = int(dials.split('❌ Вам необходимо подождать еще ')[-1].split(' секунд до входа в Окрестности зоны!')[0])
                    if WFR <= 0:
                        time.sleep(vrema)
                        while True:
                            dial = api.messages.getHistory(count=1, peer_id=api.users.get()[0]["id"])['items'][0]['text']
                            dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                            if "🌟 Подарочные коды/Ключи" in dials:
                                api.messages.send(peer_id=id, message=f"🤼‍♂ Группировки", random_id=0, payload=json.dumps({"button":"3"}))
                                time.sleep(vrema)
                                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                            if "👥 Информация о группировке" in dials:
                                api.messages.send(peer_id=id, message=f"Война за ресурсы", random_id=0, payload=json.dumps({"button":"3"}))
                                time.sleep(vrema)
                                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                            if "1⃣ Напасть на случайного игрока" in dials:
                                api.messages.send(peer_id=id, message=f"Напасть на случайного игрока", random_id=0, payload=json.dumps({"button":"1"}))
                                time.sleep(vrema)
                                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                            if "🔫 Нападение на игрока 🔫" in dials:
                                api.messages.send(peer_id=id, message=f"👊 Напасть на игрока", random_id=0, payload=json.dumps({"button":"1"}))
                                WFR = 6
                                time.sleep(Fantasys)
                                break
                            else:
                                dials = api.messages.getHistory(count=1, peer_id=id)['items'][0]['text']
                                api.messages.edit(peer_id=api.users.get()[0]["id"], message_id=api.messages.getHistory(count=1, peer_id=ido)['items'][0]['id'], message=f"Скрипт не понял где он, поэтому он зайдёт в главное меню '☢ Stalker Project ☢' и начнёт выполнять действия, которые создатель скрипта решил приготовить для Никитоса :)", random_id=0)
                                api.messages.send(peer_id=id, message=f"❎ Вернуться в главное меню", random_id=0, payload=json.dumps({"button":"0"}))
                    else:
                        WFR -= 1
                        print(WFR)
                        time.sleep(Fantasys)
                if "🎰 Игровой бар" in dials:
                    api.messages.send(peer_id=id, message=f"☣ Вылазки", random_id=0, payload=json.dumps({"button":"4"}))
                    time.sleep(vrema)
        else:
            api.messages.edit(peer_id=api.users.get()[0]["id"], message_id=api.messages.getHistory(count=1, peer_id=ido)['items'][0]['id'], message=f"Скрипт не понял где он, поэтому он зайдёт в главное меню '☢ Stalker Project ☢' и начнёт выполнять действия, которые создатель скрипта решил приготовить для Никитоса :)", random_id=0)
            api.messages.send(peer_id=id, message=f"❎ Вернуться в главное меню", random_id=0, payload=json.dumps({"button":"0"}))
            api.messages.edit(peer_id=api.users.get()[0]["id"], message_id=api.messages.getHistory(count=1, peer_id=ido)['items'][0]['id'], message=f"Запуск", random_id=0)