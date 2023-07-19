
from Processors import ChatProcessor
import csv


# Open the CSV file
with open('PRIME_EVAL.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)

    # Read the first line to get the headers
    headers = next(reader)

    # prep the output file
    outfile = open('results.csv', 'a', newline='')
    writer = csv.writer(outfile)
    writer.writerow(['query', 'model', 'response', 'ref_answer', 'extracted_answer'])

    gpt35old = 0
    gpt35new = 0
    gpt4old = 0
    gpt4new = 0
    # Iterate over the rest of the lines
    for line in reader:
        # Split the line into columns (a list of values)
        columns = dict(zip(headers, line))

        # Access column values like this:
        model = columns['model']
        model = model.split('/')[-1]
        if model == "gpt-3.5-turbo-0301":
          gpt35old = gpt35old + 1
          if gpt35old > 100:
            continue
        if model == "gpt-3.5-turbo-0613":
          gpt35new = gpt35new + 1
          if gpt35new > 100:
            continue
        if model == "gpt-4-0314":
          gpt4old = gpt4old + 1
          if gpt4old > 100:
            continue
        if model == "gpt-4-0613":
          gpt4new = gpt4new + 1
          if gpt4new > 100:
            continue


        # temperature = columns['temperature']
        # etc.

        # Your code here
        p = ChatProcessor(model)
        p.start_messages = [{"role":"system", "content": "You are an expert mathematician and careful reasoner that produces highly accurate results."}]
        p.messages = [{"role":"system", "content": "You are an expert mathematician and careful reasoner that produces highly accurate results."}]
        p.CREATE_TITLES=False
        r = p.generate_response(columns['query'])

        # Lowercase the last_response for case insensitive match
        response_lower = r['last_response'].lower()
        
        # Check for the presence of the specific strings
        matches = {"yes": "[yes]" in response_lower or "is a prime number" in response_lower,
                   "no": "[no]" in response_lower or "is not a prime number" in response_lower}
        
        # Classify the response
        if sum(matches.values()) == 1:  # Only one match
            classification = next(key for key, value in matches.items() if value)
        elif sum(matches.values()) == 0 or sum(matches.values()) > 1:  # No match or more than one match
            classification = "ambiguous"


        writer.writerow([columns['query'], model, r['last_response'], columns['ref_answer'], classification])

    outfile.close()

        

