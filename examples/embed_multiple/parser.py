'''
Created on Jun 9, 2016

@author: fredrik
'''

def find_tags(file_name):
    with open(file_name, 'r') as f:

        all_tags = []

        for line in f:
            if 'IBPLOT' in line and line[0] != '#' and line[0] != '<':
                plot_info = line[8:-1].split(';')

                new_plot_info = []
                n = 0
                for element in plot_info:
                    if element[0]==' ':
                        element = element[1:]
                    if element[-1]==' ':
                        element = element[:-1]
                    if element[-1] == ']' and n == len(plot_info) -1:
                        element = element[:-1]
                    new_plot_info.append(element)
                    n += 1
                all_tags.append(new_plot_info)

    return all_tags
