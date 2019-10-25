import csv
import dateutil.parser
from os import listdir
from os.path import isfile, join
import argparse
import datetime


class ImportData:
    def __init__(self, data_csv):
        self._time = []
        self._value = []
        self._roundtime = []
        self._roundtimeStr = []
        with open(data_csv, "r") as fhandle:
            reader = csv.DictReader(fhandle)
            for row in reader:
                try:
                    self._time.append(dateutil.parser.parse(row['time']))
                except ValueError:
                    print('Bad input format for time')
                    print(row['time'])
                self._value.append(row['value'])
            fhandle.close()


    def linear_search_value(self, key_time):
        out = []
        for i in range(len(self._roundtimeStr)):
            curr = self._roundtimeStr[i]
            if key_time == curr:
                out.append(self._value[i])
        return out


    def binary_search_value(self, key_time):
        out = []
        lo = -1
        hi = len(self._time)
        while (hi - lo > 1):
            mid = (hi + lo) // 2
            if key_time == self._time[mid]:
                return self._time[mid]
            if (key_time < self._time[mid]):
                hi = mid
            else:
                lo = mid
        out.append(self._value[mid])
        return out

def roundTimeArray(self, obj, resolution):
    # Inputs: obj (ImportData Object) and res (rounding resoultion)
    # objective:
    # create a list of datetime entries and associated values
    # with the times rounded to the nearest rounding resolution (res)
    # ensure no duplicated times
    # handle duplicated values for a single timestamp based on instructions in
    # the assignment
    # return: iterable zip object of the two lists
    # note: you can create additional variables to help with this task
    # which are not returned
    #Adam - The difference here is we are making an array
    for times in self._time:
        minminus = datetime.timedelta(minutes = (times.minute % resolution))
        minplus = datetime.timedelta(minutes=resolution) - minminus
        if (times.minute % resolution) <= resolution/2:
            newtime = times - minminus
        else:
            newtime=times + minplus
        self._roundtime.append(newtime)
        self._roundtimeStr.append(newtime.strftime("%m/%d/%Y %H:%M"))


def printArray(data_list, annotation_list, base_name, key_file):
    # combine and print on the key_file
    base_data = []
    key_idx = 0
    for i in range(len(annotation_list)):
        if annotation_list[i] == key_file:
            base_data = zip(data_list[i]._roundtimeStr, data_list[i]._value)
            print('base data is: '+annotation_list[i])
            key_idx = i
            break
        if i == len(annotation_list):
            print('Key not found')



    file = open(base_name+'.csv','w')
    file.write('time,')

    file.write(annotation_list[key_idx][0:-4]+', ')

    non_key = list(range(len(annotation_list)))
    non_key.remove(key_idx)

    for idx in non_key:
        file.write(annotation_list[idx][0:-4]+', ')
    file.write('\n')


    for time, value in base_data:
        file.write(time+', '+value+', ')
        for n in non_key:
            if time in data_list[n]._roundtimeStr:
                file.write(str(data_list[n].linear_search_value(time))+', ')
            else:
                file.write('0, ')
        file.write('\n')
    file.close()

if __name__ == '__main__':

    #adding arguments
    parser = argparse.ArgumentParser(description = 'A class to import, combine, and print data from a folder.',
                                     prog='dataImport')

    parser.add_argument('--folder_name', type=str, help='Name of the folder')

    parser.add_argument('--output_file', type=str, help='Name of Output file')

    parser.add_argument('--sort_key', type=str, help='File to sort on')

    parser.add_argument('--number_of_files', type=int,
                        help="Number of Files", required=False)

    args = parser.parse_args()

    folder_path = args.folder_name



    files_lst = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]




    data_lst = []
    for files in files_lst:
        data_lst.append(ImportData(files))

    #create two new lists of zip objects
    # do this in a loop, where you loop through the data_lst
    data_5 = [] # a list with time rounded to 5min
    data_15 = [] # a list with time rounded to 15min


    #print to a csv file
    printArray(data_5, files_lst, args.output_file+'_5', args.sort_key)
    printArray(data_15, files_lst, args.output_file+'_15', args.sort_key)
