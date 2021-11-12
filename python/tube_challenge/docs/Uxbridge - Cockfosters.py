x = """
Uxbridge Underground Station
06:25
Hillingdon Underground Station
06:27
Ickenham Underground Station
06:30
Ruislip Underground Station
06:31
Ruislip Manor Underground Station
06:33
Eastcote Underground Station
06:37
Rayners Lane Underground Station
06:41
South Harrow Underground Station
06:43
Sudbury Hill Underground Station
06:46
Sudbury Town Underground Station
06:49
Alperton Underground Station
06:52
Park Royal Underground Station
06:55
North Ealing Underground Station
06:57
Ealing Common Underground Station
07:00
Acton Town Underground Station
07:06
Hammersmith (Dist&Picc Line) Underground Station
07:08
Barons Court Underground Station
07:11
Earl's Court Underground Station
07:13
Gloucester Road Underground Station
07:18
Knightsbridge Underground Station
07:19
Hyde Park Corner Underground Station
07:22
Green Park Underground Station
07:23
Piccadilly Circus Underground Station
07:25
Leicester Square Underground Station
07:26
Covent Garden Underground Station
07:28
Holborn Underground Station
07:30
Russell Square Underground Station
07:32
King's Cross St. Pancras Underground Station
07:35
Caledonian Road Underground Station
07:37
Holloway Road Underground Station
07:38
Arsenal Underground Station
07:40
Finsbury Park Underground Station
07:42
Manor House Underground Station
07:45
Turnpike Lane Underground Station
07:47
Wood Green Underground Station
07:50
Bounds Green Underground Station
07:54
Arnos Grove Underground Station
07:57
Southgate Underground Station
08:00
Oakwood Underground Station
08:04
Cockfosters Underground Station
"""

x = [x for x in x.splitlines() if x.strip()!='']
#for v in x: print(v)
st = [v for v in x[0::2]]
tm = [v.replace(":", '') for v in x[1::2]]
print(st)
print(tm)

import json
v = { "piccadilly_uxbridge": st, "timings": tm }
print(repr(v))
