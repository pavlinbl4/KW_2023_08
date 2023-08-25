import pyperclip

from bad_words_job import add_bad_words_from_list
from best_keywords import keywords_optimization
from checkbox_output import create_checkbox_list
from lematization import lema
from lists_difference import list_dif
from new_input_window import create_input_window
from write_keywords import write_keywords


def main() -> str:
    data_from_gui = create_input_window("Enter text here")  # get text from GUI window

    result = data_from_gui[0]
    lemma_switch = data_from_gui[1]

    # if window was closed - stop program
    if not result:
        quit()

    # turn lemmatization
    if lemma_switch == 1:
        lema_result_lst = lema(result[0])
        lema_result_str = ','.join(lema_result_lst)
        good_keywords_str = keywords_optimization(lema_result_str)
    else:
        # keywords optimisation
        good_keywords_str = keywords_optimization(", ".join(result))

    # convert to list
    good_keywords_lst = good_keywords_str.split(', ')

    # select keyword that you want via GUI and convert them to  the string
    selected_keywords_list = create_checkbox_list(good_keywords_lst, "Select_keywords")
    rezult_str = ", ".join(selected_keywords_list)

    # copy keywords to clip
    pyperclip.copy(rezult_str)

    # write keywords to txt file
    write_keywords(rezult_str, '/Users/evgeniy/Documents/keywords/keywords in work.txt')

    # find "bad word" in unused keywords
    unused_keywords_list = list_dif(good_keywords_lst, selected_keywords_list)
    bad_words_list = create_checkbox_list(unused_keywords_list, 'Select "BAD WORDS"')

    print(f'{bad_words_list = }')

    #  save "bad words"  to file
    add_bad_words_from_list(bad_words_list, '/Users/evgeniy/Documents/keywords/bad_words.txt')

    print(f'{rezult_str = }')

    return rezult_str


if __name__ == '__main__':
    main()
