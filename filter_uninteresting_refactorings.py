
# Windows (Note the double \ where necessary)
input_file_name = 'all_refactorings_master.csv'
input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\spring'
input_path = input_file_location + '\\' + input_file_name
output_file_name = input_file_name.split('.')[0] + '_filtered' + '.csv'
output_file_location = input_file_location
output_path = input_file_location + '\\' + output_file_name
# Linux/Mac (Comment out above 5 lines and uncomment the 5 below)
# input_file_location = '/home/steve/Steve/Desktop/'
# input_path = input_file_location + '/' + input_file_name
# output_file_location = input_file_location
# output_file_name = input_file_name + '_filtered'
# output_path = input_file_location + '/' + output_file_name

# Add any other uninteresting types here after defined (list is still TBD)
uninteresting_refactoring_types = ['Rename Method', 'Rename Parameter', 'Rename Attribute', 'Rename Variable']


def filter_out_uninteresting():
    with open(input_path, 'r') as f:
        refactoring_instances = f.readlines()[1:]
    f.close()

    with open(output_path, 'w+') as f:
        for refactoring_instance in refactoring_instances:
            refactoring_instance_details = refactoring_instance.split(';')
            if refactoring_instance_details[1] not in uninteresting_refactoring_types:
                line = str(refactoring_instance_details[0]) \
                       + ',' + str(refactoring_instance_details[1]) \
                       + ',' + str(refactoring_instance_details[2])
                f.write(line)
    f.close()


filter_out_uninteresting()
