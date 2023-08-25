from datetime import datetime
import os


def write_keywords(final, file_path: str):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(file_path, 'a') as text_file:
        text_file.write('\n')
        text_file.write(datetime.now().strftime("%Y-%m-%d") + '\n')
        text_file.write(final)


if __name__ == '__main__':
    write_keywords("one, two, tree", '/Volumes/big4photo/Documents/Kommersantttt/text.txt')
