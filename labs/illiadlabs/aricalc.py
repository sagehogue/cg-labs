
def get_text_byline():
    with open('illiad.txt', 'r', encoding='utf-8') as f:
        txt_file = f.readlines()
        return txt_file

def get_alltext():
    with open('illiad.txt', 'r', encoding='utf-8') as f:
        the_txt = f.read()
        return the_txt

def wordnum(input):
    wordlist = []
    for i in input:
        wordlist.append(i.split())
    return len(wordlist)

def charnum(input):
    stripsen = ''
    strisen = ''
    bad_list = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
    for line in input:
        stripsen += line.strip()
    for strippedline in stripsen:
        if strippedline in bad_list:
            strisen += stripsen.replace(strippedline, ' ')
    listofchar = strisen.split()
    return len(listofchar)

    # charlist = []
    # for i in input:
    #     cur_i = i.replace(' ', '')
    #     charlist.append(cur_i)
    # return c



def sentcount(input):
    sentences = input
    sentencecount = []
    for i in sentences:
        if i in '.?!':
            sentencecount.append('<endsent>')
    return len(sentencecount)

    # file_sentences = file_string
    # sentences = ''
    # for i in file_sentences:
    #     if i in '.!?':
    #         sentences += '<EndSentence>'
    #     else:
    #         sentences += i

        # if i in punc_splitlist:
        #     box_of_split += input.split(i)
        # sent_count = Counter(input.split())


def calc_ari(wordnum, charnum,):
    step1 = (charnum / wordnum) * 4.17


line_target = get_text_byline()
lump_target = get_alltext()

words = wordnum(line_target)
characters = charnum(line_target)
sentences = sentcount(lump_target)
print(words, characters, sentences)

# The score is computed by multiplying the number of characters divided by the number of words by 4.17,
# adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43.
# If the result is a decimal, always round up.
# Scores greater than 14 should be presented as having the same age and grade level as scores of 14.
something is wrong