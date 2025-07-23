def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")


def create_dict(a):
    no_freq = {}
    n=len(a)-1
    for i in range(n):
        if a[i] not in no_freq.keys():
            no_freq[a[i]] =1
        else:
            no_freq[a[i]] +=1
    print(no_freq)


if __name__ == '__main__':
    print(count_vowels('aeioullsdmswa'))
    print(sum([1,1]))    #sum(iterable, start=0)

    arr = [1,1,1,13,33,34,4,4,4,5,56,6]
    create_dict(arr)