#!/usr/bin/env python
# Selection sort alogrithm.

def selection_sort(sample):
    '''
    Selection sort alogrithm.
    Takes a sample list and returns sorted list.
    Returns False if sample is not a samplest.
    '''
    if isinstance(sample, (list)):
        for i in range(len(sample)):
            min_index = i
            j = i + 1
            while j < len(sample):
                if sample[j] < sample[min_index]:
                    min_index = j
                j += 1
            sample[i], sample[min_index] = sample[min_index], sample[i]
        return sample
    else:
        return False
