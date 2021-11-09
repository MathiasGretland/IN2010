""" 
Avgjørelsesproblem - Ja eller nei. I 2010: "Er listen sortert?" eller "Finnes det en sti mellom to par av noder i en graf?"
Problem/spørsmål: "Er listen sortert?" Instans: Lista vi snakker om, f.eks.: [1,2,3]
Problem/spørsmål: "Finnes det en sti mellom to par av noder i en graf?" Instans: Graf, to noder a og b

-Finn et element i en liste. Instans: [1,2,3], elm: 8 <--- Dette går ikke, og derfor må vi omskrive:
Omskrive: Inneholder listen L elementet e? Instans: [1,2,3], elm 8

Er som oftest en algoritme som avgjør dette for oss.

-------------------------------------------------------------------------------------------------------------------

Kompleksitetsklasser - En måte å sortere problemene etter hvor vanskelig de er å løse

Løs et utdelt sudoku-brett

P: løsninger kan bli effektivt beregnet
Effektiv vil si: At det kan løses på polynomisk tid, altså f.eks.: O(n^tall) og bedre, O(n^tall) < O(n^2) < O(nlog(n)) < O(n) < O(log(n)) < O(1)
Alle alg. fra IN2010 kan brukes til å løse problemer i P

NP: Problemer som kan verifiseres i polynomisk tid
Hva vil det si å verifisere? Formelt: En algoritme som verifiserer et problem:
- Tar instansen ("tingen" vi skal sjekke om er et JA eller NEI for dette problemet, f.eks en liste),
- og et sertifikat (typ et løsningsforslag) som input

De fleste problemer som kan løses i P, kan også løses i NP, men ikke motsatt. 

P = NP? eller P != NP? De fleste tolker at P != NP

EKSEPMEL: Sudoku
- Instans: et uferdig brett
- Spørsmål: finnes det en gyldig løsning for dette brettet?

- Sertifikat: Et utfylt brett
- Sjekk om sertifikatet er en gyldig løsning

------------------------------------------------------------------------------------------------------------------------------------

Reduksjoner - "Oversette" fra et problem til et annet: Altså hvis en instans x er en JA-instans av prob. A,
vil f(x) være en JA-instans av prob B. Hvis x er en NEI-instans av A, er f(x) en NEI-instans av B.

Instans: Naturlig tall n
Spørsmål: er n et oddetall?

Reduser til:

Instans: Naturlig tall n
Spørsmål: er n et partall?

Her må vi gjøre om på Instans, altså her vil reduseringen bli, Instans: naturlig tall n+1

Fordi da vil f.eks.: hvis n = 5 så vil svaret bli JA begge deler fordi 5+1 er et partall på den nederste.

------------------------------------------------------------------------------------------------------------------------

#Dette under er ikke like viktig
NP-komplett, NP-hard

NP-komplett 
- Problemet må være i NP
- For alle problemer i NP, så kan B polynomtid-reduseres til A. 
- Problemet er minst like vanskelig (eller vanskeligere) enn alle andre problemer i NP-gruppa.

NP-hard
- For alle problemer i NP, så kan B polynomtid-reduseres til A. 
- Problemet er minst like vanskelig (eller vanskeligere) enn alle andre problemer i NP-gruppa.

"""