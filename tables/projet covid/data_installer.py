import urllib.request as urllib2

def download_file(url, file_name):
    '''
    Download a file from url and copy it locally with file_name as name.
    '''
    try:
        # Open URL and download the file
        response = urllib2.urlopen(url)
        with open(file_name, 'wb') as output:
            output.write(response.read())
        
        return True
    except Exception as e:
        print(f'Erreur: {e}')
        return False

# Main code
if __name__ == '__main__':
    # URL of the file to download
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    file_name = "time_series_covid19_confirmed_global.csv"

    if download_file(url, file_name):
        print(f'Téléchargement de {file_name} terminé avec succès')
    else:
        print(f'Téléchargement de {file_name} impossible')
