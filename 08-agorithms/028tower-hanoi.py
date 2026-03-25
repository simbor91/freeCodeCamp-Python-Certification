# Algorithms
# 028 Certification Project: Implement the Tower of Hanoi Algorithm

def hanoi_solver(n):
    # 1. Inizializziamo i pioli come liste
    # Usiamo nomi chiari per mappare lo stato finale
    A = list(range(n, 0, -1))
    B = []
    C = []
    
    output = [f'{A} {B} {C}']

    n_moves = 0

    # 2. Definiamo la funzione ricorsiva INTERNA
    # Questa funzione può "vedere" e modificare A, B e C della funzione esterna
    def solve(disk_n, source, dest, aux):
        nonlocal n_moves

        if disk_n == 0:
            return f'{A} {B} {C}'
        
        if disk_n == 1:
            # Muoviamo fisicamente il disco
            disk = source.pop()
            dest.append(disk)
            n_moves += 1
            output.append(f'{A} {B} {C}')
            return

        # Sposta n-1 dischi sulla torre ausiliaria
        # prima chiamata ricorsiva: "parcheggiare" i dischi, quindi la destinazione momentanea è il piolo ausiliario.
        solve(disk_n - 1, source, aux, dest)

        # Sposta il disco più grande sulla destinazione
        disk = source.pop()
        dest.append(disk)
        n_moves += 1
        output.append(f'{A} {B} {C}')

        # Sposta gli n-1 dischi dall'ausiliaria alla destinazione finale
        # seconda chiamata ricorsiva: recuperare i dischi dal "parcheggio", quindi la sorgente momentanea è il polo aux
        solve(disk_n - 1, aux, dest, source)

    # 3. Avviamo la ricorsione interna
    solve(n, A, C, B)

    print(f'Number of total moves: {n_moves}')

    # Restituiamo tutto l'output come un'unica stringa leggibile
    return '\n'.join(output)

# Test con 3 dischi
print(hanoi_solver(3))