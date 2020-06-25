
# file_name = '1_2' # TODO: Change this for each test file in 1_1 each run to append
file_name = '3_4' # TODO: Change this for each test file in 1_1 each run to append
# input_file_name = 'test_coverage_results\\1_2\\' + file_name + '.csv'
input_file_name = file_name + '.csv' # TODO: Uncomment this and comment above
input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project'
input_path = input_file_location + '\\' + input_file_name
# output_file_name = input_file_name.split('.')[0] + '1_2' + '.csv'
# output_file_name = '1_2' + '_source_files' + '.txt' # TODO: Uncomment this and comment above
output_file_name = '3_4' + '_source_files' + '.txt' # TODO: Uncomment this and comment above
output_file_location = input_file_location
output_path = input_file_location + '\\' + output_file_name


def compute_test_coverage_intersection_half():
    with open(input_path, 'r') as f:
        tests_and_fiels_tested = f.readlines()
    f.close()

    source_files = []

    for line in tests_and_fiels_tested:
        details = line.split(',')
        source_files.append(details[1])
    source_files = list(set(source_files))

    with open(output_path, 'a+') as f:
        for file in source_files:
            f.write(file)
    f.close()


compute_test_coverage_intersection_half()