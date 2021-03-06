import random
import sys

monster_counter = 0
hp = 10
attack = 10

monster_hp = 0
monster_attack = 0


def choice_player() -> str:
    """Выбор игрока."""
    pl_choice = input()
    while pl_choice != "1" and pl_choice != "2":
        pl_choice = input()
        if pl_choice != "1" and pl_choice != "2":
            print("Ты должен ввести 1 или 2")

    return pl_choice


def hero() -> None:
    """Показывает текущие параметры героя."""
    print("Показатель очков здоровья героя:", str(hp), "HP")
    print("Показатель атаки героя:", str(attack), "damage")


def monster() -> None:
    """Генерирует нового монстра и показывает его параметры."""
    global monster_hp
    global monster_attack
    monster_hp = random.randint(1, 5)
    monster_attack = random.randint(1, 5)
    print("Показатель очков здоровья монстра:", str(monster_hp), "HP")
    print("Показатель атаки монстра:", str(monster_attack), "damage")


def apple() -> None:
    """Создает яблоко и увеличивает хп."""
    increase_hp = random.randint(1, 5)
    global hp
    print("вы нашли яблоко, очки здоровья увеличены на", str(increase_hp), "HP")
    hp = hp + increase_hp
    print("Текущий показатель здоровья равен ", str(hp), "HP")


def sword() -> None:
    """Подбор меча и выбор игрока, брать его или нет."""
    increase_attack = random.randint(1, 25)
    global attack

    print(
        "Вы нашли клинок, с уроном",
        str(increase_attack),
        "\nЧто вы будете делать с этим клинком? "
        "\n1 - заменить свой старый клинок, с "
        "уроном",
        str(attack),
        "\n" "2 - пройти мимо",
    )
    print("MEЧ", str(increase_attack), "\n")
    current_choice = choice_player()

    if current_choice == "1":
        attack = increase_attack
        print(
            "вы подобрали клинок и выбросили старый, ваша атака героя стала равна",
            str(increase_attack),
        )
    elif current_choice == "2":
        print("вы отказались подбирать клинок, ваша атака не изменилась")


def skirmish_with_monster() -> None:
    """Встреча с монстром."""
    global monster_counter
    global hp
    print(
        "БОЙ",
        str(monster_hp),
        str(monster_attack),
        "\n1 - атаковать чудовище\n2 - убежать",
    )
    fight_or_not = choice_player()
    if fight_or_not == "1":
        print("деремся")
        fight()
        if hp > 0:
            monster_counter = monster_counter + 1
        else:
            print("ПОРАЖЕНИЕ")
            sys.exit()

    elif fight_or_not == "2":
        dices = random.randint(0, hp)
        hp = hp - dices
        print("ты убежал, при этом потерял", dices, "единиц здоровья\n")


def fight() -> None:
    """Сражение с монстром."""
    global hp
    global monster_hp

    while hp > 0 and monster_hp > 0:
        hp = hp - monster_attack
        monster_hp = monster_hp - attack


def game() -> None:
    """Процесс игры."""
    global monster_counter
    global hp
    while monster_counter <= 10 or hp >= 1:
        print("")
        print("Монстров убито", str(monster_counter))
        hero()
        events = random.randint(1, 3)
        if events == 1:
            apple()
        elif events == 2:
            monster()
            skirmish_with_monster()
            if hp <= 0:
                print("ПОРАЖЕНИЕ")
                sys.exit()
        else:
            sword()

        if hp <= 0 or monster_counter == 10:
            break

    if monster_counter == 10 and hp > 0:
        print("ПОБЕДА")
        sys.exit()
    elif hp <= 0 and monster_counter <= 10:
        print("ПОРАЖЕНИЕ")
        sys.exit()


# game()
