Tar filnavnet til input, operasjon som skal bli utført og hvilke sorteringsalgoritmer som skal brukes som command-line argument.

Algoritmene som er implementert er insertion sort, merge sort, heap sort og bubble sort.


Formatet på command-line argumentene er slik:

python sort.py input_file sort *Sorteringsalgoritmer separert med mellomrom*

python sort.py input_file stats *Sorteringsalgoritmer separert med mellomrom*


Eksempler:

"python sort.py data.in sort insert merge heap bubble"

"python sort.py data.in stats merge bubble"