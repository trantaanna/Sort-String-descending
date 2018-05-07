import csv

def read_from_file(filename):
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
                sorted_row = sorted(row,reverse=True)
                #Store sorted row in an array/list
                result_content.append(sorted_row)
        except csv.Error as e:
            print('File {} line {}: {}'.format(filename, reader.line_num, e))

    return result_content

def write_to_file(content, filename):
    #Open file to write
    with open (filename, 'wb') as f:
        writer = csv.writer(f)
        try:
            writer.writerows(content)   #write to file 
        except csv.Error as e:
            print('Error encounter while writing to file: '.format(e))


if __name__ == "__main__":
    content = read_from_file('input.csv')
    write_to_file(content, 'output.csv')