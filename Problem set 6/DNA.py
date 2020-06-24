import csv
from sys import argv


class DnaTest(object):

    """CLASS HELP: the DNA test, simply give DNA sequence to the program, and it searches in the database to
       determine the person who owns the sample.

    type the following in cmd to run the program:
    python dna.py databases/small.csv sequences/1.txt """

    def __init__(self):
        # get filename from the command line without directory names "database" and "sequence"
        self.sequence_argv = str(argv[2][10:])
        self.database_argv = str(argv[1][10:])

        # Automatically open and close the database file
        with open(f"databases/{self.database_argv}", 'r') as database_file:
            self.database_file = database_file.readlines()

        # Automatically open and close the sequence file
        with open(f"sequences/{self.sequence_argv}", 'r') as sequence_file:
            self.sequence_file = sequence_file.readline()

        # Read CSV file as a dictionary, function: compare_database_with_sequence()
        self.csv_database_dictionary = csv.DictReader(self.database_file)
        # Read CSV file to take the first row, function: get_str_list()
        self.reader = csv.reader(self.database_file)
        # computed dictionary from the sequence file
        self.dict_from_sequence = {}

    # returns the first row of the CSV file (database file)
    def get_str_list(self):
        # get first row from CSV file
        self.keys = next(self.reader)

        # remove 'name' from list, get STR only.
        self.keys.remove("name")
        return self.keys

    # returns dictionary of computed STRs from the sequence file (key(STR): value(count))
    def get_str_count_from_sequence(self):  # PROBLEM HERE AND RETURN DICTIONARY FROM IT !
        for dna_seq in self.get_str_list():
            self.dict_from_sequence.update({dna_seq: self.sequence_file.count(dna_seq)})

    # compare computed dictionary with the database dictionaries and get the person name
    def compare_database_with_sequence(self):
        for dictionary in self.csv_database_dictionary:
            dict_from_database = dict(dictionary)
            dict_from_database.pop('name')

            # compare the database dictionaries with sequence computed dictionary
            shared_items = {k: self.dict_from_sequence[k] for k in self.dict_from_sequence if
                            k in dict_from_database and self.dict_from_sequence[k] == int(dict_from_database[k])}

            if len(self.dict_from_sequence) == len(shared_items):
                dict_from_database = dict(dictionary)
                print(dict_from_database['name'])
                break


# run the class and its functions (Program control)
if __name__ == '__main__':
    RunTest = DnaTest()
    RunTest.get_str_count_from_sequence()
    RunTest.compare_database_with_sequence()