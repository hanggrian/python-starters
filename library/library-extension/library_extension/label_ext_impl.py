from tkinter import Label

from library.label_impl import LabelImpl


class LabelExtImpl(LabelImpl):
    def __init__(self, label: Label):
        super().__init__(label)

    def get_position(self) -> str:
        return f'({self.label.winfo_pointerx()},{self.label.winfo_pointery()})'
