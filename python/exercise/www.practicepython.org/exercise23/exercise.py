import requests

from bs4 import BeautifulSoup


def downloadToLocal(remote_url, file_name):
    r = requests.get(remote_url)

    with open(file_name, "w") as input_file:
        input_file.write(r.text.encode("utf-8"))
    input_file.close()


def extract_set_from_file(file_name):
    result = []
    with open(file_name, "r") as input_file:
        read_line = input_file.readline()
        while read_line:
            result.append(int(read_line[:-1]))
            read_line = input_file.readline()
    input_file.close()

    return result


file_a_url = "http://www.practicepython.org/assets/happynumbers.txt"
file_a_name = "happynumbers.txt"
file_b_url = "http://www.practicepython.org/assets/primenumbers.txt"
file_b_name = "primenumbers.txt"

downloadToLocal(file_a_url, file_a_name)
downloadToLocal(file_b_url, file_b_name)
set_a = set(extract_set_from_file(file_a_name))
set_b = set(extract_set_from_file(file_b_name))

print sorted(set_a & set_b)
