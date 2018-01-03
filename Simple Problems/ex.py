def main():
    base_word = 'stairs'

    num_sounds_lists = int('2')
    k = 0
    ef = ['erres airs ears ares aires', 'eet eat']
    sounds = set()
    for i in range(0, num_sounds_lists):
        sound_list = ef[k].split()
        for sound in sound_list:
            if sound_in_word(sound, base_word):
                sounds.update(set(sound_list))
               # print(sounds)
        k+=1

    num_phrases = int('2')
    phrases = ['apples and pears', 'plates of meat']
    k = 0
    print('-------------')
    for i in range(num_phrases):
        last_word =phrases[k].split()[-1]
        found = False

        for sound in sounds:
            if sound_in_word(sound, last_word):
                print("YES")
                found = True
                break
        if not found:
            print("NO")
        k+=1

def sound_in_word(sound, word):
   # print(word)
    if len(sound) > len(word):
        print(sound)
        return False
   # print(sound)
    if word[len(word) - len(sound):] == sound:
        print(sound)
        return True
    return False

if __name__ == '__main__':
    main()