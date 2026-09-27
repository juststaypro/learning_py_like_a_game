name =''
health = 0.00
strength = 0.00
enemyHealth=50.00
enemyStrength = 10
inventory = []
player_won = None

def hello_player():
    name = input("Ты просыпаешься в темной пещере.\n"
                 "Навстречу, из темноты, приближается темный силуэт.\n"
                 "Фигура в плаще с капюшоном, закрывающим лицо, спрашивает:\n"
                 "Как тебя зовут, путник?\n")
    print(f"Приветствую тебя {name}\n путники тут оказываются не случайно\n Тебе предстоит совершить подвиг \nИ постараться выбраться живым \nУдачи тебе {name}")
    return name

name = hello_player()

def hello_stats ():
    health = int(input("Уже уходя, фигура в капюшоне говорит:\n"
                   " - Обрати внимание, у тебя здесь есть ограниченное здоровье.\n"
                   "Ты осматриваешь себя и видишь очки здоровья\n"
                   "Их у тебя ровно: "))
    if health <= 10 :
         (f"Твое здоровье всего {health}? Ты слишком хрупкий для этого пути. \nБудь предельно осторожен.")
    elif 10 < health <= 30:
        print (f"У тебя достаточно здоровья для этого пути.")
    else:
        print (f"Ты обладаешь крепким здоровьем. Это поможет тебе в пути.")
    strength = int(input("Фигура уже скрылась за поворотом\n"
                        "А ты все еще осматриваешь себя\n"
                        "и замечаешь что у тебя есть еще и характеристика\n"
                        "Похоже это уровень твоей силы: "))
    if strength < 10:
        print ("За стенами раздается громкий смех. Таких слабаков еще поискать")
    elif 10 <= strength <= 30:
        print ("Вокруг сохраняется зловещая тишина")
    else:
        print ("Со всех сторон доносится звук открывающихся дверей")
    if health > 30 and strength > 30:
        print ("Ты слышишь шевеления и скрежет вокруг. \nПохоже твои здоровье и сила привлекли дополнительных врагов.")
    print(f"Персонаж {name} создан! Здоровье: {health}. Сила: {strength}")
    return health, strength

health, strength = hello_stats()

def light_hit (enemyStrength, health):
    enemyHit = (enemyStrength * 2)
    health -= (enemyHit * 2)
    print(f"\n\nТы не ударил врага. Здоровье врага {enemyHealth}\n")
    print(f"Враг ударил тебя с силой {enemyHit * 2} Твое здоровье {health}\n")
    return health

def normal_hit (hit, enemyStrength, health, enemyHealth):
    enemyHealth -= hit
    enemyHit = enemyStrength
    enemyHit -= (hit / 10)
    health -= (enemyHit/2)
    print(f"\n\nТы ударил врага. Здоровье врага {enemyHealth}\n")
    print(f"Враг ударил тебя с силой {enemyHit} Твое здоровье {health}\n")
    return health, enemyHealth


def over_hit (enemyStrength, health, enemyHealth, strength):
    failHit = (strength // 10)
    enemyHealth -= failHit
    enemyHit = enemyStrength
    health -= enemyHit
    print(f"Ты так старался сильно ударить, что потерял равновесие и вывихнул плечо\n")
    print(f"Ты попал по врагу с силой {failHit}. Враг попал по тебе с силой {enemyHit}\n")
    print(f"Здоровье врага {enemyHealth}, твое здоровье {health}\n")
    return health, enemyHealth

def fight (health, strength, enemyHealth, enemyStrength, inventory):
    hit = int(input("Ты пытаешься ударить врага. С какой силой ты хочешь удариь?"))
    if strength >= hit > 0:
        health, enemyHealth = normal_hit (hit, enemyStrength, health, enemyHealth)
    elif hit <= 0:
        health = light_hit (enemyStrength, health)
    elif strength < hit:
        health, enemyHealth = over_hit (enemyStrength, health, enemyHealth, strength)
    if enemyHealth <= 0:
        print ("Поздравляю, враг побежден. Можешь забрать себе все, что найдешь у него.")
        loot = {"name": "Меч", "type": "Оружие", "damage":15}
        inventory.append(loot)
        player_won = True
        return health, inventory, player_won, enemyHealth
    elif health <= 0:
        print ("Ты побежден. Возможно, получиться в следующий раз.")
        inventory = []
        player_won = False
        return health, inventory, player_won, enemyHealth
    else:
        player_won = None
        return health, inventory, player_won, enemyHealth



print ("Ты отправляешься дальше и встречаешь первого врага.\n"
       "Понятно, что это враг. Он сморит на тебя зловеще.\n"
       "Еще мгновение и вот он уже бросился на тебя\n"
       "Его когти проходят в миллиметре от твоей шеи и рвут твой шарф\n")

while (health >=0 and enemyHealth >=0) or player_won == None:
    health, inventory, player_won, enemyHealth = fight(health, strength, enemyHealth, enemyStrength, inventory)

print ("Сейчас у тебя в инвентаре: ")
if inventory == []:
    print ("пусто.")
else:
    for index, item in enumerate(inventory, start=1):
        print (f"{index}. {item['name']}")

print ("Конец")
