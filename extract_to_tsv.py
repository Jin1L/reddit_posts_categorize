import argparse
import json
import csv
import random

RAND_NUM = []
def generate_random_number(num):
    return random.randint(0, num)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-o", "--output", required=True, help="Output file that we would like to save our data into")
    parser.add_argument("-j", "--json", required=True, help="JSON file that we will use to extract data")
    parser.add_argument("-n", "--number", required=True, help="Number of posts that we would like to output")

    args = parser.parse_args()

    output_file = args.output
    json_file_path = args.json
    num_posts_to_outuput = args.number

    with open(json_file_path, 'r') as file:
        json_file = json.load(file)

    length_json = len(json_file["data"]["children"])

    with open(output_file, 'w', newline='') as tsv_file:
        tsv_writer = csv.writer(tsv_file, delimiter='\t')  # Set the delimiter to '\t' for TSV

        if int(num_posts_to_outuput) >= length_json:
            for data in json_file["data"]["children"]:

                name = data["data"]["name"]
                title = data["data"]["title"]
                code = ""

                tsv_writer.writerow([name,title,code])

        else:
            while len(RAND_NUM) != int(num_posts_to_outuput):
                num = int(num_posts_to_outuput) - 1
                random_number = generate_random_number(num)

                while True:
                    if random_number in RAND_NUM:
                        random_number = generate_random_number(num)
                    else:
                        RAND_NUM.append(random_number)
                        break

                data = json_file["data"]["children"][random_number]

                name = data["data"]["name"]
                title = data["data"]["title"]
                code = ""

                tsv_writer.writerow([name,title,code])

if __name__ == "__main__":
    main()
