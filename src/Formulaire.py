from tkinter import Frame, Label, Checkbutton, Button, BooleanVar


class Formulaire(Frame):

    def __init__(self, master, dic: dict,  **kwargs):
        # bg='#faf7f2'
        Frame.__init__(self, master=master, **kwargs)

        max_col = len(max(list(dic.values()), key=lambda a: len(a)))-1

        for i in range(len(dic) * 2 + 1):
            self.rowconfigure(i, weight=1)
        for i in range(max_col):
            self.columnconfigure(i, weight=1)
        self.grid(row=1, column=0, sticky='news')

        self.retour = {}

        self.labels = []
        self.check_buttons = []
        self.values = []
        self.values_bak = []

        keys = list(dic.keys())
        for i in range(len(keys)):
            key = keys[i]

            typev, *values = dic[key]

            v = typev()

            self.labels.append(Label(self, text=key))
            self.values.append(v)
            self.values_bak.append(values)
            self.labels[-1].grid(row=i*2, column=0, columnspan=max_col, padx=5, pady=5, sticky='new')

            for j in range(len(values)):
                if typev == BooleanVar:
                    self.check_buttons.append(Checkbutton(self, text=values[j], variable=v, onvalue=j == 0,
                                                          offvalue=j != 0))
                else:
                    self.check_buttons.append(Checkbutton(self, text=values[j], variable=v, onvalue=values[j]))
                self.check_buttons[-1].grid(row=i * 2 + 1, column=j, padx=5, pady=5, sticky='new')

        self .bouton_soumettre = Button(self, text="Ajouter ce robot", activebackground='green',
                                        command=self._retourner_valeurs)
        self .bouton_soumettre.grid(row=6, column=0, padx=20, pady=20, sticky='new')

    def _retourner_valeurs(self):
        dic = {}

        for l in range(len(self.labels)):
            res = self.values[l].get()
            text = self.labels[l].config()['text'][-1]
            dic[text] = self.values_bak[l][0] if type(res) != bool and res not in self.values_bak[l] else res

        for cb in self.check_buttons:
            cb.deselect()
        print(dic)

        self.retour = dic
