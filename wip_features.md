USERS:
- admin

DB:
- azienda (nome, partita iva, settore, città, indirizzo, cap, provincia, nazione, sito web, note)
- fattura (emittente, destinatario, data, numero, importo, tipologia di fattura, scadenza, stato pagamento, note)
- prodotti (nome, quantità, descrizione, da riordinare o meno)

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
- modifica prodotto
- carica prodotto
- possibilità di generare report 
- possibilità di esportare su excel

FORM:
- form di inserimento aziende
- form di inserimento fatture
- form di inserimento prodotti


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
- ~~aggiungere vista per tenere traccia di pagamenti aperti (interessante https://stackoverflow.com/questions/72782959how-to-sum-with-condition-in-a-django-queryset)~~
- ~~ vista dei pagamenti scaduti attivi e passivi ~~
- razionalizzare nomi url, viste, template in modo che seguano una logica condivisa tra loro
- ~~generare reportistica CSV:~~ 
- gestione merci e magazzino 
    - ~~generare modello per le merci~~ 
    - ~~generare vista per inserirle ex novo~~
    - ~~generare vista per modificarle~~ 
    - ~~generare funzione per riordinarle~~
    - ~~capire come si riflette su fatture (siamo qui, stiamo provando a gestire il tutto) provare con https://stackoverflow.com/questions/68506395/how-can-i-update-the-field-of-a-model-from-another-model-field-in-django e https://stackoverflow.com/questions/29166148/how-to-update-a-model-instance-in-another-model-save-method-in-django ~~
    - ~~funziona ma ritorna una cifra apparentemente a cazz tenendo in memoria tutti i precedenti~~
    - ~~testare e aggiungere if nel modello per fatture attive-passive~~
    - ~~aggiungere autochecl per refill quantità~~
    - attenzione, se faccio per modificare la fattura ma non modifico la quantità, viene comunque presa in modo additivo, da ragionare (non so bene come fare ma ci penso su) 
    - ~~riportare anche poi su modifica fatture lo stesso metodo~~
    - ~~creato modello, viste, url, link, ma tutto da testare e sistemare da zero pian pianino e con calma~~
    - aggiungere filtered views
    - capire come ritornare CSV con i campi sensati senza fare esplodere il metodo __str__

- aggiornare lista features

DOCS & REFS:
- https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query  
- https://docs.djangoproject.com/en/4.0/howto/outputting-pdf/ 
- https://stackoverflow.com/questions/53339813/django-link-to-download-csv-in-template
- https://stackoverflow.com/questions/29166148/how-to-update-a-model-instance-in-another-model-save-method-in-django

