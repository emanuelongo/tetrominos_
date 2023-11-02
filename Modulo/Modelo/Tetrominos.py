class Tridominos:
    def __init__(self):
        self.tablero_i_0 = None
        self.tablero_i_90 = None
        self.tablero_i_180 = None
        self.tablero_i_270 = None

        self.tablero_o_0 = None
        self.tablero_o_90 = None
        self.tablero_o_180 = None
        self.tablero_o_270 = None

        self.tablero_t_0 = None
        self.tablero_t_90 = None
        self.tablero_t_180 = None
        self.tablero_t_270 = None

        self.tablero_s_0 = None
        self.tablero_s_90 = None
        self.tablero_s_180 = None
        self.tablero_s_270 = None

        self.tablero_z_0 = None
        self.tablero_z_90 = None
        self.tablero_z_180 = None
        self.tablero_z_270 = None

        self.tablero_j_0 = None
        self.tablero_j_90 = None
        self.tablero_j_180 = None
        self.tablero_j_270 = None

        self.tablero_l_0 = None
        self.tablero_l_90 = None
        self.tablero_l_180 = None
        self.tablero_l_270 = None

    def tridomino_i(self):
        self.tablero_i_0 = [". . @ .", ". . @ .", ". . @ .", ". . @ ."]
        for m in self.tablero_i_0:
            print(m)
        self.rotar_90_grados_i()

    def tridomino_o(self):
        self.tablero_o_0 = [". . . .", ". @ @ .", ". @ @ .", ". . . ."]
        for m in self.tablero_o_0:
            print(m)
        self.rotar_90_grados_o()

    def tridomino_t(self):
        self.tablero_t_0 = [". . . .", ". @ @ @", ". . @ .", ". . . ."]
        for m in self.tablero_t_0:
            print(m)
        self.rotar_90_grados_t()

    def tridomino_s(self):
        self.tablero_s_0 = [". . . .", ". . @ @", ". @ @ .", ". . . ."]
        for m in self.tablero_s_0:
            print(m)
        self.rotar_90_grados_s()

    def tridomino_z(self):
        self.tablero_z_0 = [". . . .", ". @ @ .", ". . @ @", ". .  ."]
        for m in self.tablero_z_0:
            print(m)
        self.rotar_90_grados_z()

    def tridomino_j(self):
        self.tablero_j_0 = [". . @ .", ". . @ .", ". @ @ .", ". .  ."]
        for m in self.tablero_j_0:
            print(m)
        self.rotar_90_grados_j()

    def tridomino_l(self):
        self.tablero_l_0 = [". @ . .", ". @ . .", ". @ @ .", ". . . ."]
        for m in self.tablero_l_0:
            print(m)
        self.rotar_90_grados_l()

    def rotar_90_grados_i(self):
        while True:
            pregunta_90 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_90 == "n":
                break
            elif pregunta_90 == "s":
                self.tablero_i_90 = [". . . .", "@ @ @ @", ". . . .", ". . . ."]
                for m in self.tablero_i_90:
                    print(m)
                break

        while True:
            pregunta_180 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_180 == "n":
                break
            elif pregunta_180 == "s":
                self.tablero_i_180 = [". . @ .", ". . @ .", ". . @ .", ". . @ ."]
                for m in self.tablero_i_180:
                    print(m)
                break

        while True:
            pregunta_270 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_270 == "n":
                break
            elif pregunta_270 == "s":
                self.tablero_i_270 = [". . . .", "@ @ @ @", ". . . .", ". . . ."]
                for m in self.tablero_i_270:
                    print(m)
                break

        pregunta_seguir_jugando = input("¿Desea mirar otros tridominos (Ingresa s para Sí o n para No)?: ")
        if pregunta_seguir_jugando == "s":
            seguir_jugando = input("Ingresa la letra que deseas ver del tridominó (i, o, t, s, z, j, l): ")

            if seguir_jugando == "i":
                self.tridomino_i()

            elif seguir_jugando == "o":
                self.tridomino_o()

            elif seguir_jugando == "t":
                self.tridomino_t()

            elif seguir_jugando == "s":
                self.tridomino_s()

            elif seguir_jugando == "z":
                self.tridomino_z()

            elif seguir_jugando == "j":
                self.tridomino_j()

            elif seguir_jugando == "l":
                self.tridomino_l()
        elif pregunta_seguir_jugando == "n":
            while True:
                print("")
                print("Hasta pronto")
                break

    def rotar_90_grados_o(self):
        while True:
            pregunta_o_90 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_o_90 == "n":
                break
            elif pregunta_o_90 == "s":
                self.tablero_o_90 = [". . . .", ". @ @ .", ". @ @ .", ". . . ."]
                for m in self.tablero_o_90:
                    print(m)
                break

        while True:
            pregunta_o_180 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_o_180 == "n":
                break
            elif pregunta_o_180 == "s":
                self.tablero_o_180 = [". . . .", ". @ @ .", ". @ @ .", ". . . ."]
                for m in self.tablero_o_180:
                    print(m)
                break

        while True:
            pregunta_o_270 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_o_270 == "n":
                break
            elif pregunta_o_270 == "s":
                self.tablero_o_270 = [". . . .", ". @ @ .", ". @ @ .", ". . . ."]
                for m in self.tablero_o_270:
                    print(m)
                break

        pregunta_seguir_jugando = input("¿Desea mirar otros tridominos (Ingresa s para Sí o n para No)?: ")
        if pregunta_seguir_jugando == "s":
            seguir_jugando = input("Ingresa la letra que deseas ver del tridominó (i, o, t, s, z, j, l): ")

            if seguir_jugando == "i":
                self.tridomino_i()

            elif seguir_jugando == "o":
                self.tridomino_o()

            elif seguir_jugando == "t":
                self.tridomino_t()

            elif seguir_jugando == "s":
                self.tridomino_s()

            elif seguir_jugando == "z":
                self.tridomino_z()

            elif seguir_jugando == "j":
                self.tridomino_j()

            elif seguir_jugando == "l":
                self.tridomino_l()
        elif pregunta_seguir_jugando == "n":
            while True:
                print("")
                print("Hasta pronto")
                print("======")
                break

    def rotar_90_grados_t(self):
        while True:
            pregunta_t_90 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_t_90 == "n":
                break
            elif pregunta_t_90 == "s":
                self.tablero_t_90 = [". . @ .", ". @ @ .", ". . @ .", ". . . ."]
                for m in self.tablero_t_90:
                    print(m)
                break

        while True:
            pregunta_t_180 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_t_180 == "n":
                break
            elif pregunta_t_180 == "s":
                self.tablero_t_180 = [". . . .", ". . @ .", ". @ @ @", ". . . ."]
                for m in self.tablero_t_180:
                    print(m)
                break

        while True:
            pregunta_t_270 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_t_270 == "n":
                break
            elif pregunta_t_270 == "s":
                self.tablero_t_270 = [". @ . .", ". @ @ .", ". @  .", ". . . ."]
                for m in self.tablero_t_270:
                    print(m)
                break

        pregunta_seguir_jugando = input("¿Desea mirar otros tridominos (Ingresa s para Sí o n para No)?: ")
        if pregunta_seguir_jugando == "s":
            seguir_jugando = input("Ingresa la letra que deseas ver del tridominó (i, o, t, s, z, j, l): ")

            if seguir_jugando == "i":
                self.tridomino_i()

            elif seguir_jugando == "o":
                self.tridomino_o()

            elif seguir_jugando == "t":
                self.tridomino_t()

            elif seguir_jugando == "s":
                self.tridomino_s()

            elif seguir_jugando == "z":
                self.tridomino_z()

            elif seguir_jugando == "j":
                self.tridomino_j()

            elif seguir_jugando == "l":
                self.tridomino_l()
        elif pregunta_seguir_jugando == "n":
            while True:
                print("")
                print("Hasta pronto")
                break

    def rotar_90_grados_s(self):
        while True:
            pregunta_s_90 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_s_90 == "n":
                break
            elif pregunta_s_90 == "s":
                self.tablero_s_90 = [". @ . .", ". @ @ .", ". . @ .", ". . . ."]
                for m in self.tablero_s_90:
                    print(m)
                break

        while True:
            pregunta_s_180 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_s_180 == "n":
                break
            elif pregunta_s_180 == "s":
                self.tablero_s_180 = [". . . .", ". . @ @", ". @ @ .", ". . . ."]
                for m in self.tablero_s_180:
                    print(m)
                break

        while True:
            pregunta_s_270 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_s_270 == "n":
                break
            elif pregunta_s_270 == "s":
                self.tablero_s_270 = [". @ . .", ". @ @ .", ". . @ .", ". . . ."]
                for m in self.tablero_s_270:
                    print(m)
                break

        pregunta_seguir_jugando = input("¿Desea mirar otros tridominos (Ingresa s para Sí o n para No)?: ")
        if pregunta_seguir_jugando == "s":
            seguir_jugando = input("Ingresa la letra que deseas ver del tridominó (i, o, t, s, z, j, l): ")

            if seguir_jugando == "i":
                self.tridomino_i()

            elif seguir_jugando == "o":
                self.tridomino_o()

            elif seguir_jugando == "t":
                self.tridomino_t()

            elif seguir_jugando == "s":
                self.tridomino_s()

            elif seguir_jugando == "z":
                self.tridomino_z()

            elif seguir_jugando == "j":
                self.tridomino_j()

            elif seguir_jugando == "l":
                self.tridomino_l()
        elif pregunta_seguir_jugando == "n":
            while True:
                print("")
                print("Hasta pronto")
                break

    def rotar_90_grados_z(self):
        while True:
            pregunta_z_90 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_z_90 == "n":
                break
            elif pregunta_z_90 == "s":
                self.tablero_z_90 = [". . @ .", ". @ @ .", ". @ . .", ". . . ."]
                for m in self.tablero_z_90:
                    print(m)
                break

        while True:
            pregunta_z_180 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_z_180 == "n":
                break
            elif pregunta_z_180 == "s":
                self.tablero_z_180 = [". . . .", ". @ @ .", ". . @ @", ". . . ."]
                for m in self.tablero_z_180:
                    print(m)
                break

        while True:
            pregunta_z_270 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_z_270 == "n":
                break
            elif pregunta_z_270 == "s":
                self.tablero_z_270 = [". . @ .", ". @ @ .", ". @ . .", ". . . ."]
                for m in self.tablero_z_270:
                    print(m)
                break

        pregunta_seguir_jugando = input("¿Desea mirar otros tridominos (Ingresa s para Sí o n para No)?: ")
        if pregunta_seguir_jugando == "s":
            seguir_jugando = input("Ingresa la letra que deseas ver del tridominó (i, o, t, s, z, j, l): ")

            if seguir_jugando == "i":
                self.tridomino_i()

            elif seguir_jugando == "o":
                self.tridomino_o()

            elif seguir_jugando == "t":
                self.tridomino_t()

            elif seguir_jugando == "s":
                self.tridomino_s()

            elif seguir_jugando == "z":
                self.tridomino_z()

            elif seguir_jugando == "j":
                self.tridomino_j()

            elif seguir_jugando == "l":
                self.tridomino_l()
        elif pregunta_seguir_jugando == "n":
            while True:
                print("")
                print("Hasta pronto")
                break

    def rotar_90_grados_j(self):
        while True:
            pregunta_j_90 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_j_90 == "n":
                break
            elif pregunta_j_90 == "s":
                self.tablero_j_90 = [". . . .", ". @ . .", ". @ @ @", ". . . ."]
                for m in self.tablero_j_90:
                    print(m)
                break

        while True:
            pregunta_j_180 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_j_180 == "n":
                break
            elif pregunta_j_180 == "s":
                self.tablero_j_180 = [". @ @ .", ". @ . .", ". @ . .", ". . . ."]
                for m in self.tablero_j_180:
                    print(m)
                break

        while True:
            pregunta_j_270 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_j_270 == "n":
                break
            elif pregunta_j_270 == "s":
                self.tablero_j_270 = [". . . .", ". @ @ @", ". . . @", ". . . ."]
                for m in self.tablero_j_270:
                    print(m)
                break

        pregunta_seguir_jugando = input("¿Desea mirar otros tridominos (Ingresa s para Sí o n para No)?: ")
        if pregunta_seguir_jugando == "s":
            seguir_jugando = input("Ingresa la letra que deseas ver del tridominó (i, o, t, s, z, j, l): ")

            if seguir_jugando == "i":
                self.tridomino_i()

            elif seguir_jugando == "o":
                self.tridomino_o()

            elif seguir_jugando == "t":
                self.tridomino_t()

            elif seguir_jugando == "s":
                self.tridomino_s()

            elif seguir_jugando == "z":
                self.tridomino_z()

            elif seguir_jugando == "j":
                self.tridomino_j()

            elif seguir_jugando == "l":
                self.tridomino_l()
        elif pregunta_seguir_jugando == "n":
            while True:
                print("")
                print("Hasta pronto")
                break

    def rotar_90_grados_l(self):
        while True:
            pregunta_l_90 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_l_90 == "n":
                break
            elif pregunta_l_90 == "s":
                self.tablero_l_90 = [". . . .", ". @ @ @", ". @ . .", ". . . ."]
                for m in self.tablero_l_90:
                    print(m)
                break

        while True:
            pregunta_l_180 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_l_180 == "n":
                break
            elif pregunta_l_180 == "s":
                self.tablero_l_180 = [". @ @ .", ". . @ .", ". . @ .", ". . . ."]
                for m in self.tablero_l_180:
                    print(m)
                break

        while True:
            pregunta_l_270 = input("¿Desea girar su figura 90 grados? (ingresa s para Sí o n para No): ")
            if pregunta_l_270 == "n":
                break
            elif pregunta_l_270 == "s":
                self.tablero_l_270 = [". . . .", ". @ . .", ". @ @ @", ". . . ."]
                for m in self.tablero_l_270:
                    print(m)
                break

        pregunta_seguir_jugando = input("¿Desea mirar otros tridominos (Ingresa s para Sí o n para No)?: ")
        if pregunta_seguir_jugando == "s":
            seguir_jugando = input("Ingresa la letra que deseas ver del tridominó (i, o, t, s, z, j, l): ")

            if seguir_jugando == "i":
                self.tridomino_i()

            elif seguir_jugando == "o":
                self.tridomino_o()

            elif seguir_jugando == "t":
                self.tridomino_t()

            elif seguir_jugando == "s":
                self.tridomino_s()

            elif seguir_jugando == "z":
                self.tridomino_z()

            elif seguir_jugando == "j":
                self.tridomino_j()

            elif seguir_jugando == "l":
                self.tridomino_l()
        elif pregunta_seguir_jugando == "n":
            while True:
                print("")
                print("Hasta pronto")
                break

    def __eq__(self, other):
        if self.tablero_s_0 == other.tablero_z_0:
            print("Son iguales")
        else:
            print("No tiene iguales")


if __name__ == "__main__":
    opcion_seguir_jugando = input("Ingresa la letra que deseas ver del tridominó (i, o, t, s, z, j, l): ")
    self = Tridominos()

    if opcion_seguir_jugando == "i":
        self.tridomino_i()

    elif opcion_seguir_jugando == "o":
        self.tridomino_o()

    elif opcion_seguir_jugando == "t":
        self.tridomino_t()

    elif opcion_seguir_jugando == "s":
        self.tridomino_s()

    elif opcion_seguir_jugando == "z":
        self.tridomino_z()

    elif opcion_seguir_jugando == "j":
        self.tridomino_j()

    elif opcion_seguir_jugando == "l":
        self.tridomino_l()
