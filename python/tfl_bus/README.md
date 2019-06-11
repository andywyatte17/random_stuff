## Useful Links

  - tfl.gov.uk/tfl/syndication/feeds/bus-sequences.csv?app_id=&app_key=
  - https://www.google.com/search?q=site%3Atfl.gov.uk+51057+bus
  - https://duckduckgo.com/?q=site%3Atfl.gov.uk+51057+bus&ia=web

### pip google

    #!/usr/env/bin python3
    # pip google
    from googlesearch import search
    for url in search('site:tfl.gov.uk bus 51057', stop=5):
        print(url)