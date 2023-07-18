import csv

def export_to_csv(keywords_list, filename='keywords.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Keyword", "Score"])
        for keyword in keywords_list:
            writer.writerow(keyword)