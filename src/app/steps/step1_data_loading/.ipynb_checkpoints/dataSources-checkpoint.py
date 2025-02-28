import os
import json
from langchain.document_loaders import PyPDFDirectoryLoader

# data_path_input = "data/input/Data_Insurance/NorthAmerica"
data_load_output = "data/output/data_load.json"

def dataLoadPdf(data_path_input, data_load_output):
    try:
        # Create the output directory if it does not exist
        output_dir = os.path.dirname(data_load_output)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        loader = PyPDFDirectoryLoader(data_path_input)
        data = loader.load()
        data_dict = []
        for doc in data:
            doc_dict = {
                "page_content": doc.page_content
            }
            data_dict.append(doc_dict)

        with open(data_load_output, 'w') as f:
            json.dump(data_dict, f, indent=4)
        return f"Data saved to {data_load_output}\nStatus: Success"
        #print(f"Data saved to {data_load_output}")
        #print("Status: Success")
    except Exception as e:
        # print(f"Status: Error - {str(e)}")
        return f"Status: Error - {str(e)}"

# # Example usage:
# dataLoadPdf(data_path_input, data_load_output)