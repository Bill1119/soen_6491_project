
# Windows (Note the double \ where necessary)
# input_file_name = 'all_refactorings_master.csv'
# input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\spring'
# input_path = input_file_location + '\\' + input_file_name
# output_file_name = input_file_name.split('.')[0] + '_filtered' + '.csv'
# output_file_location = input_file_location
# output_path = input_file_location + '\\' + output_file_name
# Linux/Mac (Comment out above 5 lines and uncomment the 5 below)
# input_file_location = '/home/steve/Steve/Desktop/'
# input_path = input_file_location + '/' + input_file_name
# output_file_location = input_file_location
# output_file_name = input_file_name + '_filtered'
# output_path = input_file_location + '/' + output_file_name

file_name = 'BaseProviderTest' # TODO: Change this for each test file in 1_1 each run to append
# input_file_name = 'test_coverage_results\\1_2\\' + file_name + '.csv'
input_file_name = 'test_coverage_results\\1_1\\' + file_name + '.csv' # TODO: Uncomment this and comment above
input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project'
input_path = input_file_location + '\\' + input_file_name
# output_file_name = input_file_name.split('.')[0] + '1_2' + '.csv'
# output_file_name = '1_2' + '.csv'
output_file_name = '1_1' + '.csv' # TODO: Uncomment this and comment above
output_file_location = input_file_location
output_path = input_file_location + '\\' + output_file_name

# Add any other uninteresting types here after defined (list is still TBD)
project_specific_source_location = '/src/main/java'


def filter_out_mappings():
    # with open(input_path, 'r') as f:
    #     headers = f.readlines()[0:1][0]
    # f.close()
    print('input_path: ', input_path)
    with open(input_path, 'r') as f:
        test_coverage_instances = f.readlines()[1:]
    f.close()

    with open(output_path, 'a+') as f:
        # f.write(str(headers))
        for test_coverage_instance in test_coverage_instances:
            test_coverage_instance_details = test_coverage_instance.split(',')
            if project_specific_source_location in test_coverage_instance_details[0] \
                    and float(test_coverage_instance_details[3]) > 0.0:
                class_name = test_coverage_instance_details[2]
                output = file_name[0:-3] + ',' + class_name + '\n'
                # output = file_name + ',' + class_name + '\n' #TODO: Uncomment this and comment above
                f.write(output)
    f.close()


filter_out_mappings()
