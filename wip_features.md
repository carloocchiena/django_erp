USERS:
- admin

DB:
- azienda (nome, partita iva, settore, città, indirizzo, cap, provincia, nazione, sito web, note)
- fattura (emittente, destinatario, data, numero, importo, tipologia di fattura, scadenza, stato pagamento, note)

HOME:
- scegli tra le diverse funzioni possibili, logout, help

LOGIN:
- login (creazione utenti solo da backend admin)

VISTE:
- viste di tutte le aziende, con pagina di dettaglio
- vista delle fatture attive scadute e non scadute (con indicazione se scadute o meno) suddivise per azienda
- vista delle fatture passive scadute e non scadute (con indicazione se scadute o meno) suddivise per azienda
- modifica azienda
- modifica fattura
- possibilità di generare report 
- possibilità di esportare su excel

FORM:
- form di inserimento aziende
- form di inserimento fatture


TO BE DONE:
- review completa UI
- ~~pagina di dettaglio delle aziende~~
- ~~fix trattino tra i btn della home~~
- fix la validazione dei dati dentro i form
- ~~fix i valori di default nei menu dropdown~~
- ~~gestire vista fatture scadute e non scadute~~
- ~~gestire vista fatture attive e passive~~
- ~~aggiungere vista aggiornamento aziende~~
- ~~sistemare flusso login-logout in ogni sua parte (template, view)~~
- ~~gestire \ integrare search bar (https://stackoverflow.com/questions/57554020/django-search-form-for-filtering, https://django-filter.readthedocs.io/en/main/guide/usage.html e questo fatto veramente bene, passo passo https://www.youtube.com/watch?v=nle3u6Ww6Xk)~~
- ~~sistemare campo di ricerca per data in aziende e fatture (partire da https://django-filter.readthedocs.io/en/stable/search.html?q=icontains&check_keywords=yes&area=default)~~
- ~~sistemare UI pagine di ricerca~~
- ~~aggiungere nuovo db per gestire pagamenti~~
- ~~aggiungere filtro per pagamenti passivi e attivi~~
- aggiungere vista per tenere traccia di pagamenti aperti (interessante https://stackoverflow.com/questions/72782959/how-to-sum-with-condition-in-a-django-queryset)
- ~~ vista dei pagamenti scaduti attivi e passivi ~~
- razionalizzare nomi url, viste, template in modo che seguano una logica condivisa tra loro

- generare reportistica CSV: 
    - https://rb.gy/exhd1o
    - https://docs.djangoproject.com/en/4.0/howto/outputting-pdf/ 
    - partiamo intanto dal CSV https://docs.djangoproject.com/en/4.0/howto/outputting-csv/ , direi di creare una funzione che, preso un oggetto, ne ritorna il csv con il nome dell'oggetto, così la possiamo chiamare ovunque, vediamo. Dovrà anche essere un pulsante addizionale immagino sulle varie pagine.
    - qui una valida traccia https://studygyaan.com/django/how-to-export-csv-file-with-django 
    - anche qui fatta con CBV https://stackoverflow.com/questions/16286666/send-a-file-through-django-class-based-views 
    - ho trovato una possibile strada, anche capendo come generare url dinamici descrittivi, vediamo come proseguire
    - ok ok ci sono, devo discriminare qui creando un url dinamico che in base al contenuto passato, genera la lista fatture o aziende (e via di conseguenza) https://stackoverflow.com/questions/53339813/django-link-to-download-csv-in-template 
    - ripulire poi file views e functions dopo averci messo mano


DOCS & REFS:
- https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query  

