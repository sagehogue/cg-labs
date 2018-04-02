# nailed v1 

def get_data():
    permiss = input('Please input a data list or type "td" to use test data.\n: ')
    if permiss == 'td':
        data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    else:
        data = permiss
    return data

def peaks(dataset):
    peak_list = []
    for i in range(len(dataset)-1):
        # while i+1 == True:
        if dataset[i] > dataset[i - 1] and dataset[i] > dataset[i + 1]:
            peak_list.append(i)
    return peak_list

def valleys(dataset):
    valley_list = []
    for i in range(len(dataset)-1):
        # while i+1 == True:
        if dataset[i] < dataset[i - 1] and dataset[i] < dataset[i + 1]:
            valley_list.append(i)
    return valley_list

def peaks_n_valleys(dataset):
    p_list = peaks(dataset)
    v_list = valleys(dataset)
    return 'There are peak(s) in the dataset at indice(s) {}\nThere are valley(s) in the dataset at indice(s) {}'.format(p_list, v_list)

our_data = get_data()
print(peaks_n_valleys(our_data))
#Returns the indices of peaks.
#A peak has a lower number on both the left and the right.

#Returns the indices of ‘valleys’. A valley
#is a number with a higher number on both the left and the right.

#peaks_and_valleys - uses the above two functions to compile a single
#list of the peaks and valleys in order of appearance in the original data.
