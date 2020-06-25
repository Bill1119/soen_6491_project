
import json

# Windows (Note the double \ where necessary)
# input_file_name = 'refactorings_40fd7ad244b350d657ca4f1a9efe667c52697327_3ca48892811538e911eb3c5bafd60b4d9ca92483.csv'
# input_file_name = 'refactorings_4581a4520315657a4219b37c81f5db80e4a4e43c_40fd7ad244b350d657ca4f1a9efe667c52697327.csv'
input_file_name = 'refactorings3_3to3_4_37f8fe84d934a92fe784c62e706b7aacf6fa4f97_4777c3a5e4291af2420db57d008152c70c4a8f24.csv'
# input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\common-rng-1_1_to_1_2\\'
# input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\common-rng-1_0_to_1_1\\'
input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\commons-lang\\'

input_path = input_file_location + '\\' + input_file_name
output_file_name = 'parsed_' + input_file_name.split('.')[0] + '_dict.json'
output_file_location = input_file_location
output_path = input_file_location + '\\' + output_file_name
# Linux/Mac (Comment out above 5 lines and uncomment the 5 below)
# input_file_location = '/home/steve/Steve/Desktop/'
# input_path = input_file_location + '/' + input_file_name
# output_file_location = input_file_location
# output_file_name = input_file_name + '_filtered'
# output_path = input_file_location + '/' + output_file_name

uninteresting_refactoring_types = ['Rename Method', 'Rename Parameter', 'Rename Attribute', 'Rename Variable']


def extract_mappings():
    with open(input_path, 'r') as f:
        refactoring_instances = f.readlines()[1:]
    f.close()

    refactoring_dict = {}

    #count = 0
    for refactoring_instance in refactoring_instances:
        # print(refactoring_instance)
        instance_dict = {}
        refactoring_instance_details = refactoring_instance.split(';')
        commit = refactoring_instance_details[0]
        refactoring_type = refactoring_instance_details[1]
        refactoring_mapping = refactoring_instance_details[2]
        refactoring_mapping = refactoring_mapping.replace('\n', '')
        location = refactoring_instance_details[2].split(' in class ')[-1].replace('\n', '')
        file = refactoring_instance_details[2].split('.')[-1].replace('\n', '')

        if refactoring_type not in uninteresting_refactoring_types:
            instance_dict['commit'] = commit
            instance_dict['refactoring_type'] = refactoring_type
            instance_dict['refactoring_mapping'] = refactoring_mapping
            instance_dict['file'] = file
            instance_dict['location'] = location
            instance_dict['refactoring_instance'] = refactoring_instance.replace('\n', '')
            if commit not in refactoring_dict:
                refactoring_dict[commit] = []
            refactoring_dict[commit].append(instance_dict)
            #count +=1
    with open(output_path, 'w+') as f:
        json.dump(refactoring_dict, f, indent=4)
    f.close()
    #print(count)


extract_mappings()
