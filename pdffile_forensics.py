import pikepdf

def main():
    # Get the PDF file from the command-line arguments
    pdf_filename = sys.argv[1]

    # Read the PDF file
    pdf = pikepdf.open(pdf_filename)

    # Extract the metadata
    metadata = pdf.metadata

    # Print the metadata
    print("----Metadata of the file----")
    for metadata_key in metadata:
        print(metadata_key + ":" + metadata[metadata_key])

if __name__ == "__main__":
    main()
'''
Scrape metadata from PDFs
Write a mini forensics tool to collect identifying information from PDF metadata.

This code will first get the PDF file from the command-line arguments. 
Then, it will read the PDF file and extract the metadata. 
Finally, it will print the metadata to the console.

'''


