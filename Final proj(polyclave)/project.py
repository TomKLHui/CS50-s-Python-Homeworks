import argparse
import sys
import csv

def main():
    parser = argparse.ArgumentParser(prog='Guesswho',description='Find and use the most informative character for efficient classification.')
    parser.add_argument('file', type=argparse.FileType('r'),default='data.csv', help='csv file with columns for feature and row for item(possible output)')
    args = parser.parse_args()

    ##test if file input valid
    if is_csv_file(args.file.name)==False:
        sys.exit(f"Error: '{args.file.name}' is not a CSV file")
    try:
        reader = csv.DictReader(args.file)
    except FileNotFoundError:
        sys.exit("File does not exist")

    ## turn csv to list of dict
    listdict=[row for row in reader]

    while len(listdict)!=1 and len(listdict[0])!=1:
        if len(listdict)==0:
            sys.exit("You exhausted all possibilites, you lose.")
        best_k=find_target_key(listdict)
        ans=input(f"Is his/her {best_k}? (Yes/No/Not sure)").strip().capitalize()
        if ans not in ["Yes","No","Not sure"]:
            print("Please input valid answer (Yes/No/Not sure)")
            continue
        if ans == "Not sure":
            listdict=remove_feature(listdict,best_k)
            continue
        listdict=perform_filter(listdict,best_k,ans)
        #still need to remove feature after usage
        listdict=remove_feature(listdict,best_k)

    ##Final results
    if len(listdict)==1:
        print(f"I guess the person is {listdict[0]['name']}")
    if len(listdict[0])==1:
        names=[]
        for i in listdict:
            names.append(i["name"])
        print(f"We used up all possible criterias, but it could be the following people:")
        print(names)


def is_csv_file(filename):
    return filename.lower().endswith('.csv')

#find one desirable feature to classify
def find_target_key(list_of_dict):
    target_count = len(list_of_dict) / 2
    key_counts = {key: sum(1 for d in list_of_dict if key != 'name' and d.get(key) == 'Yes') for key in list_of_dict[0].keys() if key != 'name'}
    best_key = min(key_counts, key=lambda x: abs(key_counts[x] - target_count))
    return best_key

#filter according to answer
def perform_filter(list_of_dict, best_key, ans):
    filtered_dict = [d for d in list_of_dict if d.get(best_key) == ans]
    return filtered_dict

#remove feature
def remove_feature(list_of_dict,best_key):
    filtered_dict = [d.copy() for d in list_of_dict if best_key in d]
    for d in filtered_dict:
        d.pop(best_key)
    return filtered_dict
if __name__ == "__main__":
    main()
