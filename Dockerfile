FROM fedora
COPY primes.py primes.py
STOPSIGNAL SIGKILL
CMD python3 -u primes.py
