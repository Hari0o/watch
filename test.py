from asyncio import AbstractChildWatcher


def mutate_string(string, position, character):
    a=list(string)
    a[position]=character
    a=''.join(a)
    return a

if __name__ == '__main__':
    s = input()
    i,c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)