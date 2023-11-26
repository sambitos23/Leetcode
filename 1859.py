def short_sentence(input_str: str) -> str:
    words = input_str.split(" ")
    ans = [None] * len(words)
    for i in words:
        index = int(i[-1])-1
        ans[index] = i[:-1]
    ans = ' '.join(ans)
    return ans

if __name__ == '__main__':
    print(short_sentence("the3 there2 Sambit1"))


#  Using Shorting
def short_sentence(input_str: str) -> str:
    spl = input_str.split(" ")
    words = sorted(spl, key=lambda w: w[-1])
    word = [w[:-1] for w in words]
    ans = " ".join(word)

    return ans

if __name__ == '__main__':
    print(short_sentence("the3 there2 Sambit1"))