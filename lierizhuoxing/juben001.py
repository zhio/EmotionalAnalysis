import pandas as pd
import matplotlib.pyplot as plt
good_word = [{}, {}, {'JU': 1}, {}, {'E': 1}, {'E': 1, 'JU': 1, 'HAO': 1}, {'JU': 1, 'E': 2, 'LE': 2, 'AI': 1}, {'HAO': 1}, {'E': 2, 'JU': 1, 'HAO': 2, 'JIN': 1}, {}, {'JU': 1, 'E': 2}, {'E': 1}, {'JU': 1, 'E': 1, 'HAO': 1}, {'E': 1}, {'E': 1, 'LE': 1, 'HAO': 1}, {'JU': 1, 'E': 4, 'JIN': 1, 'HAO': 2}, {}, {}, {}, {'E': 3, 'AI': 2, 'JIN': 2, 'HAO': 4}, {'E': 1, 'AI': 1}, {'E': 1, 'HAO': 3}, {'JU': 2, 'E': 5, 'LE': 1, 'HAO': 5}, {'E': 1}, {'E': 1, 'HAO': 1}, {'E': 1}, {'HAO': 1}, {'JU': 1}, {'E': 1, 'JU': 1, 'nan': 1}, {'JU': 2, 'AI': 1, 'E': 3, 'HAO': 2}, {'HAO': 1}, {}, {'E': 1, 'HAO': 1}, {'E': 1}, {'AI': 1, 'JU': 3, 'E': 6, 'LE': 3, 'HAO': 7, 'JIN': 1}, {}, {}, {'JU': 1}, {}, {'LE': 1, 'HAO': 1}, {'AI': 2, 'E': 4}, {}, {'HAO': 1, 'nan': 1}, {'JU': 3, 'E': 1, 'LE': 1, 'HAO': 1}, {}, {'LE': 1, 'nan': 1}, {}, {'JIN': 2}, {}, {'AI': 2}, {}, {'AI': 1, 'E': 1, 'JU': 1}, {'JU': 1}, {'AI': 1}, {'JIN': 1}, {'AI': 1, 'E': 2}, {'JU': 1}, {'AI': 1, 'E': 1, 'JIN': 1}, {'E': 1, 'JU': 1}, {'E': 1}, {'E': 1, 'LE': 1}, {'AI': 1, 'E': 1, 'HAO': 1, 'nan': 1}, {'E': 1, 'JU': 1, 'HAO': 1}, {}, {}, {}, {'HAO': 1}, {'HAO': 1}, {}, {'AI': 1, 'JU': 1, 'E': 8, 'HAO': 1}, {'JU': 1}, {'E': 3, 'LE': 1, 'HAO': 1}, {'E': 1}, {'JU': 1}, {}, {'E': 1, 'HAO': 1}, {'E': 1, 'LE': 2}, {'AI': 1, 'E': 1, 'HAO': 1}, {}, {'JU': 2, 'LE': 1}, {}, {'AI': 1, 'JU': 1, 'E': 1, 'JIN': 1}, {'HAO': 1}, {}, {}, {'JU': 2, 'E': 1, 'LE': 1, 'HAO': 1}, {}, {'HAO': 4}, {'E': 1, 'HAO': 1}, {'E': 2, 'HAO': 1}, {'E': 1, 'AI': 2, 'LE': 2, 'HAO': 1}, {'AI': 2, 'JU': 1, 'E': 3, 'LE': 1, 'HAO': 2}, {'HAO': 1}, {'HAO': 1}, {'AI': 1, 'E': 1, 'HAO': 1}, {'JU': 1, 'LE': 1, 'HAO': 1}, {'AI': 2, 'LE': 2, 'HAO': 2}, {'E': 5, 'AI': 1, 'LE': 1, 'HAO': 7}, {'JU': 1, 'E': 1, 'HAO': 1}, {'JU': 1, 'JIN': 2, 'HAO': 1}, {'JU': 1, 'HAO': 1}, {'LE': 1}, {'E': 2}, {'E': 1}, {}, {}, {}, {'JU': 1, 'E': 2, 'HAO': 2}, {'E': 1}, {'JU': 1, 'E': 1, 'HAO': 1}, {'AI': 1, 'E': 1, 'HAO': 4}, {'LE': 1, 'HAO': 1}, {'AI': 2, 'E': 1, 'JU': 1, 'HAO': 2, 'JIN': 1, 'LE': 1, 'nan': 1}, {'E': 3, 'AI': 1, 'LE': 1}, {'AI': 1}, {}, {'HAO': 1}, {'AI': 1}, {'AI': 1, 'E': 2}, {'E': 1}, {'E': 1, 'HAO': 2}, {'JU': 1, 'E': 1, 'HAO': 1}, {'HAO': 1}, {'JU': 1, 'E': 1, 'HAO': 1}, {'AI': 1, 'E': 4, 'JU': 1, 'JIN': 1, 'HAO': 3}, {'AI': 1, 'JU': 3, 'E': 3, 'LE': 1, 'JIN': 1, 'HAO': 2}, {'E': 2, 'LE': 3, 'HAO': 1}, {}, {'AI': 2, 'E': 1, 'LE': 2, 'JIN': 1, 'HAO': 1}, {'AI': 2, 'E': 1, 'HAO': 2}, {'E': 1, 'LE': 4, 'HAO': 1, 'nan': 1}, {'AI': 3, 'E': 1, 'LE': 1, 'JIN': 1, 'HAO': 3, 'nan': 1}, {}, {'AI': 1, 'E': 1, 'LE': 3}, {'HAO': 1}, {'JU': 1, 'E': 2, 'AI': 1, 'LE': 1, 'HAO': 1}, {'AI': 1, 'E': 3, 'JIN': 1, 'HAO': 1}, {'JU': 1, 'E': 1, 'LE': 1, 'HAO': 1}, {'LE': 1, 'HAO': 2}, {}, {'E': 1}, {'AI': 1}, {}, {'AI': 2, 'E': 1, 'LE': 2, 'HAO': 4}]
print(good_word)
le = []
hao = []
nu = []
ai = []
ju = []
eee = []
jin = []
for word in good_word:

    le.append(word.get('LE',0))
    hao.append(word.get('HAO',0))
    nu.append(word.get('NU',0))
    ai.append(word.get('AI',0))
    ju.append(word.get('JU',0))
    eee.append(word.get('E',0))
    jin.append(word.get('JIN',0))

print('乐',le)
print('好',hao)
print('怒',nu)
print('哀',ai)
print('惧',ju)
print('恶',eee)
print('惊',jin)
plt.subplot(711)
plt.plot(le)
plt.subplot(712)
plt.plot(hao)
plt.subplot(713)
plt.plot(nu)
plt.subplot(714)
plt.plot(ai)
plt.subplot(715)
plt.plot(ju)
plt.subplot(716)
plt.plot(eee)
plt.subplot(717)
plt.plot(jin)

plt.show()