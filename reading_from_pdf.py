# To work with pdf files, firstly you need to install two modules below
# pip install fitz
# pip install PyMuPDF
import fitz


def read_pdf(file):
    """ Function to read file using module fitz
    This function allow you to read any page of your file in its original language
    and show how many pages are in the file.
    """
    doc = fitz.Document(file)
    page_count = doc.pageCount
    print(f'Pages in your file: {page_count}')
    n = int(input("Enter number of page you want to look for: "))
    load_page = doc.loadPage(n-1)
    page = load_page.getText()  # read a page
    page = str(page)
    return page


def main():
    print(read_pdf('c++_trofumenko.pdf'))


if __name__ == '__main__':
    main()