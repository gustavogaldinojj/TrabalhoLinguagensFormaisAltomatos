def lema_bombeamento(language_fn, p, w, max_i=5):
    if len(w) < p:
        raise ValueError("A cadeia w deve ter tamanho >= p.")

    print(f"Cadeia w: '{w}' (tamanho {len(w)})\n")
    violacao = False

    for split_x_end in range(1, p + 1):
        for split_y_end in range(split_x_end + 1, p + 1):
            x = w[:split_x_end]
            y = w[split_x_end:split_y_end]
            z = w[split_y_end:]

            if len(y) == 0:
                continue  # y precisa ter tamanho > 0

            print(f"Testando de divisão: x='{x}', y='{y}', z='{z}'")

            for i in range(0, max_i + 1):
                bombeamento_w = x + y * i + z
                result = language_fn(bombeamento_w)
                status = "PERTENCE" if result else "NAO PERTENCE"
                print(f"  i={i}: '{bombeamento_w}' -> {status}")

                if not result:
                    violacao = True

            print()

    if violacao:
        print("\nRESULTADO: Há uma quebra do lema de bombeamento. A linguagem pode não ser regular.")
    else:
        print("\nRESULTADO: Nenhuma quebra encontrada nas divisões testadas. O lema de bombeamento não foi violado (não prova irregularidade).")


# Exemplos:
if __name__ == "__main__":
    def letras_anbn(s):
        a_count = 0
        b_count = 0
        stage = 'a'
        for c in s:
            if stage == 'a':
                if c == 'a':
                    a_count += 1
                elif c == 'b':
                    stage = 'b'
                    b_count += 1
                else:
                    return False
            elif stage == 'b':
                if c == 'b':
                    b_count += 1
                else:
                    return False
        return a_count == b_count and a_count > 0

    w = 'aaaaabbbbb'  # n = 5
    p = 5

    lema_bombeamento(letras_anbn, p, w)
