import csv
import time
import os


###############################################################
#                      Writer to csv file API
###############################################################

# PRIVATE

class QuestionsWriterToFile:
    @staticmethod
    def writer_data(question_list: list, name_csv: str) -> None:
        """
        The method writes data to the csv file.
        :param question_list:
        :param name_csv:
        :return: None
        """
        with open(name_csv, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for x in question_list:
                csv_writer.writerow(x)


class ListOfQuestionsToWriteInTheCsvFile:
    @staticmethod
    def get_questions() -> list[list]:
        return [['Questions', 'Reply'], ['For Unix, the epoch is January 1, 1970, 00:00:00 (UTC)', 'T'],
                ['E.g. on most Unix systems, the clock “ticks” only 50 or 1000 times a second.', 'F'],
                ['To find out what the epoch is on a given platform, look at gmtime(0).', 'T'],
                ['time.altzone, Nonzero if a DST timezone is defined ?', 'F'],
                ['UTC is Daylight Saving Time, an adjustment of the timezone by (usually) one hour during part'
                 'of the year.', 'F']]


class CsvFileChecker:
    @staticmethod
    def is_data_in_csv_file(csv_name: str) -> bool:
        """
        The method checks the presence of data in the CSV file.
        :param csv_name:
        :return: True or False
        """
        return os.stat(csv_name).st_size == 0  # True


class ReaderToCsvFile:
    @staticmethod
    def reader_data(name_csv_file: str) -> list[list]:
        """
        The method reads data from the csv file.
        :param name_csv_file:
        :return: lists in the list
        """
        with open(name_csv_file) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            list_of_questions = list(csv_reader)
        return list_of_questions


class InputUser:
    @staticmethod
    def entered_data(text: str) -> input():
        return input(text + ': ')[:1].upper()


class TheTextThatOutputsTheInput:
    @staticmethod
    def start_and_end_text() -> str:
        return 'To start the game, press the "s" key. ' \
               'To end the game, press the "q" key: '

    @staticmethod
    def answers_and_exit_text() -> str:
        return 'Please enter T or F if it is false. ' \
               'To end the game, press the "q" key: '


class InformationTextForTheUser:
    @staticmethod
    def excellent_text() -> str:
        return 'Excellent!' \
               '__________________________________________________________'

    @staticmethod
    def not_correct_text() -> str:
        return 'Not correct :( Maybe you will be lucky next time!' \
               '________________________________________________________________'

    @staticmethod
    def good_bye_text() -> str:
        return 'Good bye!'

    @staticmethod
    def congratulations_total_score(total_score: int) -> str:
        return f'Congratulations! You total score is: {total_score}'

    @staticmethod
    def congratulations_total_time(start_time, end_time):
        return f', total time is {end_time - start_time} second.'

    @staticmethod
    def please_correct_data_text() -> str:
        return 'Please enter the correct data!'


class SortingQuestionsInTheCycle:
    @staticmethod
    def loop(name_csv_file):
        total_score = 0
        for question in ReaderToCsvFile.reader_data(name_csv_file):
            print(TheTextThatOutputsTheInput.answers_and_exit_text())
            user_input = input(question[0])[:1].upper()
            print('__________________________________________________________')
            if user_input == question[1]:
                total_score += 1
                print(InformationTextForTheUser.excellent_text())
            elif user_input != question[1]:
                print(InformationTextForTheUser.not_correct_text())
                new_list = [question[0], question[1]]
                while True:
                    print(TheTextThatOutputsTheInput.answers_and_exit_text())
                    user_input2 = input(new_list[0])[:1].upper()
                    print('__________________________________________________________')
                    if user_input2 == new_list[1]:
                        total_score += 1
                        print(InformationTextForTheUser.excellent_text())
                        break
                    else:
                        print(InformationTextForTheUser.not_correct_text())
                        break
            elif user_input == 'Q':
                print(InformationTextForTheUser.good_bye_text())
                time.sleep(1)
                break
            else:
                print(InformationTextForTheUser.not_correct_text())
        print(InformationTextForTheUser.congratulations_total_score(total_score))


# PUBLIC

def write_question_to_csv_file(file_name: str):
    if CsvFileChecker.is_data_in_csv_file(file_name):
        QuestionsWriterToFile.writer_data(ListOfQuestionsToWriteInTheCsvFile.get_questions(), file_name)


def reader_to_csv_file(file_name: str):
    if not CsvFileChecker.is_data_in_csv_file(file_name):
        ReaderToCsvFile.reader_data(file_name)


def go_through_the_questions(name_csv_file: str):
    match InputUser.entered_data(TheTextThatOutputsTheInput.start_and_end_text()):
        case 'S':
            start_time = time.monotonic()
            SortingQuestionsInTheCycle.loop(name_csv_file)
            end_time = time.monotonic()
            time.sleep(1)
            print(InformationTextForTheUser.congratulations_total_time(start_time, end_time))
        case 'Q':
            print(InformationTextForTheUser.good_bye_text())
            quit()
        case _:
            InformationTextForTheUser.not_correct_text()


###############################################################
#   
###############################################################

# MAIN FUN
FILE_NAME = 'test22.csv'

write_question_to_csv_file(FILE_NAME)
reader_to_csv_file(FILE_NAME)
go_through_the_questions(FILE_NAME)
