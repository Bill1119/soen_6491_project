import json


# TODO: Steps for the process (will want to consolidate scripts later)
# Need to run compute_test_coverage_intersection_half.py on the 1_X.csv file to obtain the 1_X_source_files.txt
# file. This will then be the input here and the output will go to
# refactoring_miner_results/commons-rng-1_X_to_1_Y_intersection.json
# Note: the 1_X.csv is obtained by running the test_class_mapping.py file on every .csv for individual test coverage in
# the test_coverage_results/1_X directory (will want to make a script to run on all .csv files in folder)


# csv_file_name = '1_2' # TODO: Change this for each test file in 1_1 each run to append
csv_file_name = '3_4' # TODO: Change this for each test file in 1_1 each run to append
csv_input_file_name = csv_file_name + '_source_files.txt'
csv_input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project'
csv_input_path = csv_input_file_location + '\\' + csv_input_file_name

# json_file_name = 'parsed_refactorings_40fd7ad244b350d657ca4f1a9efe667c52697327_3ca48892811538e911eb3c5bafd60b4d9ca92483_dict' # TODO: Change this for each test file in 1_1 each run to append
# json_file_name = 'parsed_refactorings_4581a4520315657a4219b37c81f5db80e4a4e43c_40fd7ad244b350d657ca4f1a9efe667c52697327_dict' # TODO: Change this for each test file in 1_1 each run to append
json_file_name = 'parsed_refactorings3_3to3_4_37f8fe84d934a92fe784c62e706b7aacf6fa4f97_4777c3a5e4291af2420db57d008152c70c4a8f24_dict' # TODO: Change this for each test file in 1_1 each run to append
json_input_file_name = json_file_name + '.json'
# json_input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\common-rng-1_1_to_1_2'
# json_input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\common-rng-1_0_to_1_1'
json_input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\commons-lang'
json_input_path = json_input_file_location + '\\' + json_input_file_name


# json_output_file_name = '1_0_to_1_1_intersection' + '.json' # TODO: Uncomment this and comment above
json_output_file_name = '3_3_to_3_4_intersection' + '.json' # TODO: Uncomment this and comment above
# json_output_file_name = '1_1_to_1_2_intersection' + '.json' # TODO: Uncomment this and comment above
json_output_file_location = json_input_file_location
json_output_path = json_input_file_location + '\\' + json_output_file_name


def compute_intersection_dictionary():
    with open(csv_input_path, 'r') as f:
        source_files = f.readlines()
    f.close()

    with open(json_input_path, 'r') as f:
        refactoring_dict = json.load(f)
    f.close()

    intersection_dict = {}

    for commit_hash in refactoring_dict:
        for index, refactoring_entry in enumerate(refactoring_dict[commit_hash]):
            for source_file in source_files:
                if refactoring_dict[commit_hash][index]["file"].rstrip() in source_file.rstrip():
                    intersection_dict[commit_hash] = refactoring_dict[commit_hash]

    print(len(intersection_dict))
    with open(json_output_path, 'w+') as f:
        json.dump(intersection_dict, f, indent=4)
    f.close()


compute_intersection_dictionary()
