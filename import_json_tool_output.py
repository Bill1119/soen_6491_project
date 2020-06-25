
import json

input_file_name = '1_1_to_1_2.json'
input_file_location = 'C:\\Users\\Steve\\git\\soen_6491_project\\refactoring_miner_results\\common-rng-1_1_to_1_2\\'
path = input_file_location + input_file_name

# input file was manually parsed (will not scale... )
# Needed to remove console prints (this CAN be achieved using regex to replace lines)
# Also needed to modify output of the refactoringminer api output:
# System.out.println("\"" + commitId + "\" : " );
# System.out.println(ref.toJSON());
# The above two lines added formar of the "<key> : " before the value in the form of "<commit_hash> : "
# Also necessary to add commas "," between the json entries
# Finally, the outer { and } in the first line and last line are necessary to add
# TODO: Important notes are that this required some manual parsing. Need to automate all of this
# TODO: After testing, it appears that even with manual parsing, the format is still not good


def read_json_input():
    print('path: ', path)
    with open(path) as f:
        tool_results = json.load(f)
        print('tool_results: ')
        print(tool_results)
    f.close()
    for key in tool_results:
        print(tool_results[key])


read_json_input()
