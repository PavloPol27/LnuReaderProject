from resources.fitz import Document


def read_book(file):
    """
    This function allows you to read book
    
    :file: must be string formatted .pdf or .epub or .fb2 file.
        Other formats will raise exception.
    """
    if file.endswith('.pdf') or file.endswith('.epub') or file.endswith('.fb2'):
        return Document(file)
    else:
        # DOTO write normal Exception
        raise Exception("Wrong file format")


def show_page(doc: Document, page_num=0):
    """
    This function allows you to read any page of your file in html format.
    
    :doc: Document with all pages.
    
    :page_num: Number of document page, default value = 0.
                Wrong number raise exception.
    """
    
    if page_num < 0 or page_num >= doc.page_count:
        raise Exception("Wrong page")
        
    load_page = doc.loadPage(page_num)
    page = load_page.getText('html')
    return str(page)
