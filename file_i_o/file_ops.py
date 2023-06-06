sample_file = open('sample.txt')

# file_content = sample_file.read()

# print(sample_file.read())
# sample_file.seek(0)
# # print(sample_file.read())
# print(sample_file.readline())
# sample_file.seek(0)
# print(sample_file.readlines())
#
# for line in sample_file.readlines():
#     print(line)
# sample_file.close()

try:
    with open('sample13.txt') as sample:
        content = sample.read()
        print(content)
except FileNotFoundError as err:
    print(f"File sample13.txt does not exist")
    print(err)

# with open('sample2.txt', 'a') as sample:
#     content = "This is new text"
#     sample.write(content)

# with open('created_from_python.txt', 'x') as sample:
#     content = "This file is created from Python"
#     sample.write(content)
