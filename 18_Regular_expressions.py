import re
from operator import itemgetter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def my_count_num_word(sentence):
     # 文字列をスペースで区切ってリストを作成⇒タプルに変換⇒リストに変換
     # タプルから取り出すそれが文字列にfindall flags = re.I でてきたリストのlen = num of that words 
     # (num of that words,words)のタプルを作成しそれを持つリストを作成　
     # リストをkey=lambda x: type x is int でソート
     word_list = re.split(' ' or '. ',sentence)
     word_set = set(word_list)
     print(word_set)
     ex_word_list = list(word_set)
     print(ex_word_list)
     num_of_words_list = []
     for item in ex_word_list:
         ex_word_list.remove(item)
         regex_pattern = rf'{item}'
         if item == 'I':
             words = re.findall(regex_pattern, sentence)
         else:
             words = re.findall(regex_pattern, sentence, re.I)
         num_of_words = len(words)
         num_of_words_list.append((num_of_words,words[0]))
     sorted_list = sorted(num_of_words_list,key=itemgetter(0),reverse=True)
     for i in range(len(sorted_list)):
         print(sorted_list[i])

# count_num_word(paragraph)

# Geminiの解答
import re
from operator import itemgetter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def count_num_word(sentence):
    # 1. 正規表現で単語に分解（スペースやドットを区切りにする）
    # \W+ は「英数字以外」を意味するので、記号をきれいに除外できます
    word_list = re.findall(r'\b\w+\b', sentence.lower()) 
    
    # 2. set() で重複を消して、検索用のリストを作る
    unique_words = set(word_list)
    
    num_of_words_list = []
    for item in unique_words:
        # 3. 単純にその単語が何個あるか数える
        count = word_list.count(item)
        num_of_words_list.append((count, item))
        
    # 4. ソートして表示
    sorted_list = sorted(num_of_words_list, key=itemgetter(0), reverse=True)
    
    for count, word in sorted_list:
        print((count, word))

count_num_word(paragraph)
# r'\b\w+\b' は単語を見つけ出す定石の書き方

points = ['-12', '-4', '-3', '-1', '0', '4', '8']
num_points = [int(i) for i in points]
sorted_points = sorted(num_points)
print(sorted_points)
difference = sorted_points[-1] - sorted_points[0]
print(difference)

def is_valid_variable(name):
    return name.isidentifier()

print(is_valid_variable('first_name'))
print(is_valid_variable('1-name'))
print(is_valid_variable('first-name'))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

ex_sentence = re.sub(r'[%$@&;#!]','',sentence)
print(ex_sentence)

def most_frequent_words(bun):
    split_words = re.findall(r'\b\w+\b',bun.lower())
    unique_words = set(split_words)
    result = []
    for item in unique_words:
        num_count = split_words.count(item)
        result.append((num_count,item))
    sorted_result = sorted(result,key=itemgetter(0),reverse=True)
    return sorted_result

print(most_frequent_words(ex_sentence))

# もっとも熱いコード
from collections import Counter

def most_frequent_words(bun):
    # 単語のリストを作る
    words = re.findall(r'\b\w+\b', bun.lower())
    
    # Counterに入れるだけで (単語: 個数) の辞書ができる
    counts = Counter(words)
    
    # most_common() を使うと、多い順のタプルリストが手に入る
    return counts.most_common()

# 実行結果
# [(8, 'as'), (5, 'and'), (4, 'teaching'), ...]