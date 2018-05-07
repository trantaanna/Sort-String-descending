import csv

class SortStringObject:
    def __init__(self):
        print "Hello"

    def read_from_file(self, filename):
        '''

        :param filename: STRING
        :return: ARRAY/LIST content of rows
        '''
        # array/list to hold each content of each row
        result_content = []
        # open and read file
        with open('input.csv', 'rb') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    #Sort each row decendeing alphabetical order
                    print('My row: {}'.format(row))
                    sorted_row = sorted(row,reverse=True)
                    print('Sorted: {}'.format(sorted_row))
                    #Store sorted row in an array/list
                    result_content.append(sorted_row)
            except csv.Error as e:
                print('File {} line {}: {}'.format(filename, reader.line_num, e))

        return result_content

    def write_to_file(self, filename, content):
        #Open file to write
        with open (filename, 'wb') as f:
            writer = csv.writer(f)
            try:
                writer.writerows(content)   #write to file
            except csv.Error as e:
                print('Error encounter while writing to file: '.format(e))


if __name__ == "__main__":
    my_sort_string = SortStringObject()
    content = my_sort_string.read_from_file('input.csv')
    my_sort_string.write_to_file('output.csv', content)