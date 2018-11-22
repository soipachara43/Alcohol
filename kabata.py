""" PSIT KABATA """
def kabata(s):
    """ BAKA """
    if s.find('baka' != -1):
        return 'no'
    for sound in ['bakka', 'ka', 'ba', 'ta']:
        s = s.replace(sound, '')
    return 'no' if s else 'yes'

def main():
    """ ... """
    for _ in range(int(input())):
        print(kabata(input()))
main()
