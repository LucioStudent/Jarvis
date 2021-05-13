import JarvisAI
import re
import pprint
import random

obj = JarvisAI.JarvisAssistant()


def t2s(text):
    obj.text2speech(text)


def start():
    while True:
                res = obj.mic_input()

                if re.search("Jarvis", res):
                    t2s("Salve, cosa posso fare per lei?")

                if re.search('parlami di', res):
                    topic = res[14:]
                    wiki_res = obj.tell_me(topic)
                    print(wiki_res)
                    t2s(wiki_res)
                    
                if re.search('tempo|temperatura', res):
                    city = res.split(' ')[-1]
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    t2s(weather_res)

                if re.search('notizie', res):
                    news_res = obj.news()
                    pprint.pprint(news_res)
                    t2s(f"Ho trovato queste notizie: {len(news_res)}. Le puoi leggere. Ti dirò solo le prime 2")
                    t2s(news_res[0])
                    t2s(news_res[1])

                if re.search('giorno', res):
                    date = obj.tell_me_date()
                    print(date)
                    print(t2s(date))

                if re.search('ora', res):
                    time = obj.tell_me_time()
                    print(time)
                    t2s(time)

                if re.search('apri', res):
                    domain = res.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    print(open_result)

                if re.search('ciao|hey', res):
                    print('ciao')
                    t2s('ciao')

                if re.search('come stai?', res):
                    li = ['bene', 'benissimo', 'alla grande']
                    response = random.choice(li)
                    print(f"sto {response}")
                    t2s(f"sto {response}, grazie")

                if re.search('il tuo nome|chi sei', res):
                    print("Io sono Jarvis, il tuo assistente vocale")
                    t2s("Io sono Jarvis, il tuo assistente vocale, ti darò una mano con le mie risorse")

                if re.search("chi sei realmente", res):
                    t2s("Ho da dirti una cosa molto importante... so Lillo")

                if re.search('cosa puoi fare?', res):
                    li_commands = {
                        "aprire siti": "esempio: 'apri youtube.com",
                        "ora": "esempio: 'che ora è?'",
                        "giorno": "esempio: 'che giorno è?'",
                        "parlami": "esempio: 'parlami dell'India'",
                        "tempo": "esempio: 'che tempo/temperatura fa ad Arezzo?'",
                        "notizie": "esempio: 'notizie di oggi' ",
                    }
                    ans = """Posso fare molte cose, per esempio mi puoi chiedere che ora è, giorno, il meteo della tua città,
                    posso aprirti dei siti web e molto altro. Guarda la lista dei comandi-"""
                    print(ans)
                    pprint.pprint(li_commands)
                    t2s(ans)

                if re.search("stop", res):
                    t2s("ok, allora ci risentiamo dopo, sai dove trovarmi signore!!")
                    main()
def main():
    start()

main()
