import glob
import pandas

from hello.decision_module.constants import INTERESTING_FEATURES

path = './bs_bosch_data/*.csv'
files = glob.glob(path)

ids_file = open("ids.txt", "w+")
for name in files:
    dataframe = pandas.read_csv(name)
    column_names = dataframe.columns.values
    concatinated_string = ''

    for word in column_names:
        concatinated_string += word

    for feature in INTERESTING_FEATURES:
        if feature in concatinated_string:
            ids_file.write(name.split('/')[2] + "\n")
            break

ids_file.close()
