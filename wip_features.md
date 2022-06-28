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
- gestire vista fatture scadute e non scadute
- ~~gestire vista fatture attive e passive~~
- ~~aggiungere vista aggiornamento aziende~~
- ~~sistemare flusso login-logout in ogni sua parte (template, view)~~
- ~~gestire \ integrare search bar (https://stackoverflow.com/questions/57554020/django-search-form-for-filtering, https://django-filter.readthedocs.io/en/main/guide/usage.html e questo fatto veramente bene, passo passo https://www.youtube.com/watch?v=nle3u6Ww6Xk)~~
- ~~sistemare campo di ricerca per data in aziende e fatture (partire da https://django-filter.readthedocs.io/en/stable/search.html?q=icontains&check_keywords=yes&area=default)~~
- ~~sistemare UI pagine di ricerca~~
- generare reportistica (https://rb.gy/exhd1o)
- ~~aggiungere nuovo db per gestire pagamenti~~
- aggiungere filtro per pagamenti passivi e attivi
- aggiungere vista per tenere traccia di pagamenti aperti


doc reading list:

