# Keylogger

## Lokaverkefni Öryggi tölvukerfa
Þetta forrit er gert sem hluti af lokaverkefni í "Öryggi tölvukerfa" í Háskóla Íslands.  
Við notuðumst við Python til að gera keylogger sem grípur allar strokur lyklaborðsins og skilar í textaskrá.

## Notkun forritsins
Í upphafi er best að setja upp miðað við virtual env.

Þegar er búið að sækja öll dependencies, er nóg að keyra skrána keylogger.py
*sudo keylogger.py*

Keylogger.py finnur út hvaða tegund af stýrikerfi er í gangi og velur viðeigandi subprocess.
Annað hvort linux.py eða windows.py.

Sá subprocess ræsir svo keylogger og scheduler sem að sendir login til okkar á 12 tíma fresti, 
eyðir loginum út og stofnar annan. 


## Made by :
Ómar Þór Arnarsson & Viktor Þór Freysson
otha3@hi.is & vthf1@hi.is
