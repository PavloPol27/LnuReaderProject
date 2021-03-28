import requests, PyPDF2, io

def getPDF_by_link(url):
    
    """
    This function allows you to download PDF file by giving a link to it
    
    :url: must be string URL link where PDF file is stored
        Other formats will raise exception.
    """
    
    if(url[-4:]!= '.pdf'):
        raise Exception("URL doesn't contain PDF file.")
    
    response = requests.get(url)
    
    with io.BytesIO(response.content) as open_pdf_file:
        read_pdf = PyPDF2.PdfFileReader(open_pdf_file)
        
        out = PyPDF2.PdfFileWriter() 
      
        # Open encrypted PDF file with the PdfFileReader 
        file = read_pdf
          
        # Store correct password in a variable password. 
        password = "zero"
          
        # Check if the opened file is actually Encrypted 
        if file.isEncrypted: 
          
            # If encrypted, decrypt it with the password 
            file.decrypt(password) 
          
            # Now, the file has been unlocked. 
            # Iterate through every page of the file 
            # and add it to our new file. 
            for idx in range(file.numPages): 
                
                # Get the page at index idx 
                page = file.getPage(idx) 
                  
                # Add it to the output file 
                out.addPage(page) 
              
            # Open a new file "myfile_decrypted.pdf" 
            with open("myfile_decrypted.pdf", "wb") as f: 
                
                # Write our decrypted PDF to this file 
                out.write(f) 
          
            # Print success message when Done 
            print("File decrypted Successfully.") 
        else: 
            
            # If file is not encrypted, print the  
            # message 
            print("File already decrypted.")        