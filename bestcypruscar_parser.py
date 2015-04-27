import requests
from bs4 import BeautifulSoup

links_set = set()

for i in range(1):
    r = requests.get('http://www.bestcypruscar.com/index.php?rind=%s&ord=sys_creation_date&sens=DESC' % (40 * i))
    soup = BeautifulSoup(r.text)
    link_list = soup.find_all('a')
    filtered_link_list = [
        link for link in link_list
        if '/carDetails.php?' in link['href'] and not 'SOLD' in str(link)
    ]
    links_set.update([link['href'] for link in filtered_link_list])
print 'Total: %s' % len(links_set )

def get_data_from_carDetails(url):
    print url
    data_dict = dict()

    # link = 'http://www.bestcypruscar.com/i%s' % url
    link = url
    r = requests.get(link)
    soup = BeautifulSoup(r.text)

    if len(soup.find_all('p', class_='TitluMasina')):
        titlu_masina = str(soup.find_all('p', class_='TitluMasina')[0])[25:]
        data_dict['title'] = titlu_masina[:titlu_masina.find('<')].strip()

    names = ['year', 'color', 'milage', 'engine', 'gears', 'power']

    celula_alb = soup.find_all('td', class_='TextCelulaAlb')

    # print unicode(r.text)
    # print celula_alb
    for index, name in enumerate(names):
        # print index
        item = str(celula_alb[index])
        item = item.replace('<td class="TextCelulaAlb">', '')
        item = item.replace('</td>', '')
        item = item.strip()
        data_dict[name] = item

    detail_td = str(soup.find_all('tr')[10])
    detail_td = detail_td.replace('<tr>\n<td colspan="4">', '')
    detail_td = detail_td.replace('</br></td>\n</tr>', '')
    detail_td = detail_td.replace('<br><u>Other details from owner:</u>', '')
    detail_td = detail_td.strip()
    data_dict['detail' ] = detail_td

    price_td = str(soup.find_all('tr')[12])
    price_td = price_td.replace('<tr>\n<td align="center" colspan="4"><b>', '')
    price_td = price_td.replace('</b></td>\n</tr>', '')
    price_td = price_td.replace('PRICE: ', '')
    data_dict['price' ] = price_td

    contact_td = str(soup.find_all('tr')[14])
    contact_td = contact_td.replace('<tr>\n<td colspan="4"> <b>Contact:</b>', '')
    contact_td = contact_td.replace('</td>\n</tr>', '')
    contact_td = contact_td.strip()
    data_dict['contact'] = contact_td

    posted_text_index = r.text.find('Posted on:')
    posted_on = r.text[posted_text_index+11:posted_text_index+22]
    data_dict['posted_on'] = posted_on
    del soup
    return data_dict



for link_href in links_set:
    print '------------------'
    print link_href
    data = get_data_from_carDetails(link_href)
    for item in data.items():
        print item
