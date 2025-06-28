import terminalio
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from displayio import Display
from displayio import Group


class DisplayAbstraction:
    def __init__(self, display: Display) -> None:
        self.display = display

    def update(self, newValue):
        pass


class Grid12(DisplayAbstraction):
    """docstring for Grid12"""

    def __init__(self, display: Display):
        super(Grid12, self).__init__(display)

        self.titleText = ""

        self.labelTexts = []
        while len(self.labelTexts) < 12:
            self.labelTexts.append("")

        print(f"{len(self.labelTexts)=}")

        self.main_group = Group()
        self.display.root_group = self.main_group
        self.titleLabel = label.Label(
            y=4,
            font=terminalio.FONT,
            color=0x0,
            text=" " * 22,
            background_color=0xFFFFFF,
        )
        self.layout = GridLayout(
            x=0, y=5, width=128, height=54, grid_size=(3, 4), cell_padding=5
        )
        self.labels = []
        for _ in range(12):
            self.labels.append(label.Label(terminalio.FONT, text=" " * 7))

        for index in range(12):
            x = index % 3
            y = index // 3
            self.layout.add_content(
                self.labels[index], grid_position=(x, y), cell_size=(1, 1)
            )

        self.main_group.append(self.titleLabel)
        self.main_group.append(self.layout)

    def update(self, newValue):
        if "title" in newValue:
            self.updateTitle(newValue["title"])
        if "labels" in newValue:
            self.updateLabels(newValue["labels"])

    def updateTitle(self, newValue):
        if self.titleText != newValue:
            self.titleLabel.text = f"{newValue:^22}"
        self.titleText = newValue

    def updateLabel(self, index, newValue):
        if self.labelTexts[index] != newValue:
            self.labels[index].text = f"{newValue:<7}"
        self.labelTexts[index] = newValue

    def updateLabels(self, valueList: list[str]):
        for i in range(12):
            self.updateLabel(
                index=i,
                newValue=valueList[i] if i < len(valueList) else "",
            )
