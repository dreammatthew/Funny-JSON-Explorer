from icons import *
class Draw():
    def draw_func(self, structure, icon, style):
        if style.get_style() == "tree":
            if isinstance(structure, Container):
                if structure.level == 0:
                    indent = "├─ "
                    print(f"{indent}{icon.get_icon(structure)}{structure.name}")
                else:
                    indent = "│  " + ' ' * (structure.level * 2) + "└─ "
                    print(f"{indent}{icon.get_icon(structure)}{structure.name}")
                for child in structure.children:
                    self.draw_func(child, icon, style)
            elif isinstance(structure, Leaf):
                indent = "│  " + '' * (structure.level * 2) + "├─ "
                print(f"{indent}{icon.get_icon(structure)}{structure.name}")

        elif style.get_style() == "rectangle":
            if isinstance(structure, Container):
                if structure.level == 0:
                    indent = "├─ "
                    output_string = f"{indent}{icon.get_icon(structure)}{structure.name}"
                    dashes_needed = 50 - len(output_string) - 1
                    dashes = '-' * dashes_needed + '│'
                    print(output_string + dashes)
                else:
                    indent = "│  " + ' ' * (structure.level * 2) + "├─ "
                    output_string = f"{indent}{icon.get_icon(structure)}{structure.name}"
                    dashes_needed = 50 - len(output_string) - 1
                    dashes = '-' * dashes_needed + '│'
                    print(output_string + dashes)
                for child in structure.children:
                    self.draw_func(child, icon, style)
            elif isinstance(structure, Leaf):
                indent = "│  " + '' * (structure.level * 2) + "├─ "
                output_string = f"{indent}{icon.get_icon(structure)}{structure.name}"
                dashes_needed = 50 - len(output_string) - 1
                dashes = '-' * dashes_needed + '│'
                print(output_string + dashes)

