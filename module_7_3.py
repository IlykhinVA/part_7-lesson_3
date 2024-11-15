class WordsFinder:
    file_names = []
    point_for_remove = '`~!@#№$%^&*()-_=+/[{]};:,<.>?'

    def __init__(self, *file_name):
        self.add_file_list(file_name)
        self.file_name = file_name

    def add_file_list(self, file_name):
        for new_name in file_name:
            WordsFinder.file_names.append(new_name)

    def get_all_words(self):
        all_words = {}
        for current_file_name in WordsFinder.file_names:
            long_line = ''
            with open(current_file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    long_line = long_line + ' ' + line.strip()
            long_line = long_line.lower()
            for current_point in WordsFinder.point_for_remove:
                if current_point in long_line:
                    long_line = long_line.replace(current_point, '')

            all_words.update({current_file_name: long_line.split()})
        return all_words

    def find(self, word):
        control_word = word.lower()
        find_dict = {}
        dict_word = WordsFinder.get_all_words(self)
        for verify_item in dict_word:
            verify_list = dict_word.get(verify_item)
            for verify_word in verify_list:
                if verify_word == control_word:
                    find_dict.update({verify_item: control_word + ' - ' + str(
                        verify_list.index(control_word) + 1) + ' слово по счету'})
                    return find_dict

    def count(self, word):
        control_word = word.lower()
        count_dict = {}
        dict_word = WordsFinder.get_all_words(self)
        for verify_item in dict_word:
            verify_list = dict_word.get(verify_item)
            count_dict.update({verify_item: control_word + ' - найдено ' + str(
                verify_list.count(control_word)) + ' раз'})
            return count_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
