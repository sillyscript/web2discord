from bs4 import BeautifulSoup

def getText(data):
    reference = None
    rows = data.find_all('td')[2]
    date = data.find_all('td')[1].text
    row_soup = BeautifulSoup(str(rows), 'lxml')
    td_text = row_soup.td.get_text(separator="\n").strip()
    lines = [line.strip() for line in td_text.split('\n') if line.strip()]
    if len(lines) == 3:
        reference = lines[0]
        title = lines[1]
    else:
        title = lines[0]
    return title, reference, date

def getDriveLink(data):
    link = data.find_all('td')[3].a['href']
    return link

def scrape(body, tableRowNum):
    soup = BeautifulSoup(body, 'html.parser')
    tableRow = soup.find_all('tr')[tableRowNum]
    
    title, reference, date = getText(tableRow)
    link = getDriveLink(tableRow)
    return reference, title, link, date
    