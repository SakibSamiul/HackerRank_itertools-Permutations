from itertools import permutations

def itertoolPermuation(S, k):

    p = sorted(permutations(S, int(k)))

    for i in list(p):
        print(''.join((i)))

if __name__ == '__main__':
    S, k = list(input().split())
    result = itertoolPermuation(S, k)