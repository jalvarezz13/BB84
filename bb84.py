import random


def random_bits(n):
    return [random.randint(0, 1) for _ in range(n)]


def random_bases(n):
    return [random.choice(["Z", "X"]) for _ in range(n)]


def measure(qubits, bob_bases):
    results = []
    for (bit, basis), b_basis in zip(qubits, bob_bases):
        if basis == b_basis:
            results.append(bit)  # Mide correctamente
        else:
            results.append(random.randint(0, 1))  # Resultado aleatorio
    return results


def sift(alice_bits, alice_bases, bob_results, bob_bases):
    sifted_alice, sifted_bob = [], []
    for a_bit, a_basis, b_bit, b_basis in zip(alice_bits, alice_bases, bob_results, bob_bases):
        if a_basis == b_basis:
            sifted_alice.append(a_bit)
            sifted_bob.append(b_bit)
    return sifted_alice, sifted_bob


if __name__ == "__main__":
    random.seed(17112018)  # Para reproducibilidad

    n = 50  # Número de fotones simulados
    alice_bits = random_bits(n)
    alice_bases = random_bases(n)
    qubits = list(zip(alice_bits, alice_bases))

    bob_bases = random_bases(n)
    bob_results = measure(qubits, bob_bases)

    # Sifting
    alice_key, bob_key = sift(alice_bits, alice_bases, bob_results, bob_bases)

    print(f"{'Bits originales de Alice:':25} {alice_bits[:20]}")
    print(f"{'Bases de Alice:':25} {alice_bases[:20]}")
    print(f"{'Bases de Bob:':25} {bob_bases[:20]}")
    print(f"{'Resultados de Bob:':25} {bob_results[:20]}")

    print("\n--- RESULTADOS ---")
    print(f"{'Clave sifted de Alice:':22} {alice_key}")
    print(f"{'Clave sifted de Bob:':22} {bob_key}")
    print(f"{'Coincidencia:':22} {sum(a == b for a, b in zip(alice_key, bob_key))} / {len(alice_key)}")
